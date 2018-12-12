#!/usr/bin/env python

from plumbum import cli
from importlib import import_module
from contextlib import redirect_stdout
from io import StringIO
import copy
import numpy as np
import inspect
import json
from pathlib import Path
import types

from plumbum import colors
from plumbum.colorlib import htmlcolors

import sys
if '.' not in sys.path:
    sys.path.append('.')

class Score:
    '''
    curscore: the current score (between 0 and maxscore)
    maxscore: the maximum possible score
    times: the number of scores that make up this score
    '''
    __slots__ = "curscore maxscore times".split()
    @classmethod
    def empty(cls):
        self = cls(0)
        self.maxscore = 0
        self.times = 0
        return self

    def __init__(self, score=1, maxscore=1):
        self.curscore = score
        self.maxscore = maxscore
        self.times = 1

    def __mul__(self, value):
        out = copy.copy(self)
        out.curscore *= value
        out.maxscore *= value
        return out

    def __add__(self, other):
        out = copy.copy(self)
        out.curscore += other.curscore
        out.maxscore += other.maxscore
        out.times += other.times
        return out

    def __str__(self):
        if self.maxscore > 0:
            return f'{self.curscore} of {self.maxscore} ({self.curscore/self.maxscore:2.0%})'
        else:
            return f'{self.curscore} of ???'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.curscore},{self.maxscore})'


    @property
    def color(self):
        if self.maxscore == 0 or self.curscore == 0:
            return self.colors.red
        elif self.curscore >= self.maxscore:
            return self.colors.green
        else:
            return self.colors.yellow

    def nullify(self):
        self.curscore = 0


class Grader(cli.Application):
    full = cli.Flag('--full', help="Run the full notebook instead of just definitions")
    hide = cli.Flag('--hide', help="Hide the output (usually combined with --full)")
    verbose = cli.Flag('--verbose', help="Add a printout for each success, too")
    html = cli.Flag('--html', help="Use HTML for colors")
    quick = cli.Flag('--quick', help="Only run minimal cells")

    @property
    def colors(self):
        return htmlcolors if self.html else colors

    @property
    def indent(self):
        return "&nbsp;&nbsp;" if self.html else " "

    def main(self, *infiles: cli.ExistingFile):
        for i, infile in enumerate(infiles):
            (colors.blue | colors.bold).print(infile.stem)
            print()
            try:
                self.each(infile, i)
            except Exception as e:
                if len(infiles) > 1:
                    self.colors.fatal.print("Failed:", infile.stem)
                    self.colors.fatal.print(self.indent, e)
                else:
                    raise
            print()

    def each(self, infile: cli.ExistingFile, i: int = 0):
        Score.colors = self.colors
        self.total_score = Score.empty()
        
        if infile.suffix == '.ipynb':
            if self.quick:
                self.mod = self.each_quick(infile)
            else:
                self.mod = self.each_ipynb(infile)
        elif infile.suffix == '.py':
            self.mod = self.each_py(infile)
        else:
            print("Filetype not supported:", infile)
            
        (self.colors.info | self.colors.bold).print(
                getattr(self.mod, 'EID', 'None'), ":",
                getattr(self.mod, 'NAME', 'None'))

        if not hasattr(self.mod, 'EID'):
            self.penalty('EID missing!', 1)

        if not hasattr(self.mod, 'NAME'):
            self.penalty('NAME missing!', 1)

        if getattr(self.mod, "SYNTAX", "") == "FAILURE":
            self.penalty("File would not run without changes!", 2)

        for i in range(10):
            if hasattr(self, f'process{i}'):
                self.score = Score.empty()
                self.colors.info.print(f'Problem set {i}:')

                try:
                    getattr(self, f'process{i}')()
                except Exception as e:
                    self.colors.fatal.print(self.indent, f'Failed to run problem {i}: {e.__class__.__name__}("{e}")')
                    self.score.maxscore = 0
                color = self.score.color

                msg = getattr(self.mod, f"PROBLEM_MSG", "")
                if msg:
                    color.print(self.indent, msg)

                color.print(self.indent, f'Score', self.score)

                self.total_score += self.score
                del self.score


        if hasattr(self.__class__, "TOTAL"):
            self.total_score.maxscore = self.__class__.TOTAL

        color = self.total_score.color
        color.print('Score', self.total_score)
        
    def each_ipynb(self, infile):
        # Support unusual filenames and filter out Magics
        with infile.open() as f:
            txt = f.read()
        txt = txt.replace("%matplotlib", "#%matplotlib")
        with open('tempimport.ipynb', 'w') as f:
            f.write(txt)

        base = 'ipynb.fs.' + ('full' if self.full else 'defs') + '.tempimport'
        if self.hide:
            tmp = StringIO()
            with redirect_stdout(tmp):
                imp = import_module(base)
        else:
            imp = import_module(base)
        
        Path('tempimport.ipynb').unlink()
        return imp
        
    def each_py(self, infile):
        return __import__(infile)
    
    def each_quick(self, infile):
        with open(infile) as f:
            j = json.load(f)
            mod = types.SimpleNamespace()
            
        for cell in j['cells']:
            if cell['cell_type'] == 'code':
                source = ''.join(cell['source'])
                if 'NAME' in source or 'EID' in source or '_PTS' in source or '_MSG' in source:
                    exec(source)
                    loc = list(locals().keys())
                    for item in loc:
                        if item.endswith('_PTS') or item.endswith('_MSG') or item == "NAME" or item == "EID":
                            setattr(mod, item, locals()[item])
                            
        return mod
                    
            

    def get_class(self, name):
        if not hasattr(self.mod, name):
            return lambda *args, **kargs: object
        else:
            return getattr(self.mod, name)

    def get_function(self, name):
        if not hasattr(self.mod, name):
            return lambda *args, **kargs: None
        else:
            funct = getattr(self.mod, name)

        if self.hide:
            def funct_wrapper(*args, **kargs):
                tmp = StringIO()
                with redirect_stdout(tmp):
                    return funct(*args, **kargs)
            funct_wrapper.__doc__ = funct.__doc__
            return funct_wrapper
        else:
            return funct

    def get_variable(self, name):
        return getattr(self.mod, name, "")

    def get_answer(self, name, points):
        pts = self.get_variable(name + "_PTS")
        msg = self.get_variable(name + "_MSG")
        if not msg:
            msg = "Instructor grade"
            
        if pts is True:
            pts = points
        if pts is "":
            raise RuntimeError(name + "_PTS missing, not graded")
        if points == pts:
            self.success(msg=msg, factor=pts)
        else:
            self.failure(error=msg, score=pts, factor=points)

    def success(self, *, msg=None, factor=1):
        self.score += Score(factor, factor)
        if self.verbose:
            self.colors.success.print('Scoring problem', self.score.times, 'with', factor, 'points')

    def failure(self, error, *, score=0, msg=None, factor=1):
        self.score += Score(score, factor)
        self.colors.fatal.print(self.indent, f'Test case {self.score.times} ({score}/{factor}): {error}')
        if msg:
            self.colors.fatal.print(self.indent, self.indent, msg)

    def penalty(self, msg, factor=1):
        self.total_score.curscore -= factor
        self.colors.fatal.print(self.indent, f'{msg}: {-factor}')


    # Comparison methods
    # All methods should either pass on msg and factor
    # as keyword only arguments

    def compare_in(self, item, inside, *, msg=None, factor=1):
        if msg is None:
            msg = ''.join(inspect.stack()[1].code_context).strip()
        if item is None:
            return self.failure(f'"{inside}" not in None', msg=msg, factor=factor)
        if inside in item:
            return self.success(msg=msg, factor=factor)
        else:
            return self.failure(f'"{inside}" not in "{item}"', msg=msg, factor=factor)

    def compare(self, item, other, *, msg=None, factor=1):
        ans = item == other
        if msg is None:
            msg = ''.join(inspect.stack()[1].code_context).strip()
        if isinstance(ans, np.ndarray):
            ans = np.all(ans)
        if ans:
            return self.success(msg=msg, factor=factor)
        else:
            return self.failure(f'"{item}" != "{other}"', msg=msg, factor=factor)

    def compare_close(self, item, other, *, msg=None, factor=1, rel_tol=1e-9, abs_tol=0.0):
        try:
            ans = np.isclose(item, other, rtol=rel_tol, atol=abs_tol)
        except ValueError as e:
            return self.failure(str(e), msg=msg, factor=factor)
        if isinstance(ans, np.ndarray):
            ans = np.all(ans)
        if msg is None:
            msg = ''.join(inspect.stack()[1].code_context).strip()
        if ans:
            return self.success(msg=msg, factor=factor)
        else:
            return self.failure(f'"{item}" != "{other} within allowed limits"', msg=msg, factor=factor)

    def valid(self, item, *, msg=None, factor=1):
        if msg is None:
            msg = ''.join(inspect.stack()[1].code_context).strip()
        if item:
            return self.success(msg=msg, factor=factor)
        else:
            return self.failure('Expected non-null input', msg=msg, factor=factor)

    def raises(self, exception, function, *args, factor=1, msg=None, **kargs):
        'Call a function with arguments, half score if some other exception is raised'
        try:
            function(*args, **kargs)
            return self.failure(self.indent, f'Expected {function.__name__} to raise {exception.__name__} and it didn\'t raise anything', msg=msg, factor=factor)
        except:
            return self.success(factor=factor, msg=msg)
        return self.failure(self.indent, f'Expected {function.__name__} to raise {exception} and it raised something else (half credit)', score=.5, msg=msg, factor=factor)

    def nullify(self, *, msg=None):
        'Clear the score with optional message'
        self.score.nullify()
        self.colors.red.print(self.indent, 'Problem failed')
        if msg:
            self.colors.red.print(self.indent, self.indent, f'{msg}')


# Test: Doesn't seem to work with ipynb
def patch_inf_function(function, iters: int):
    src = inspect.getsource(function)
    src = src.replace('while True', f'for _ in range({iters})')
    exec(src)
    return locals()[function.__name__]

