#!/usr/bin/env python

from plumbum import cli
from importlib import import_module
from contextlib import redirect_stdout
from io import StringIO
import copy
import math
import numpy as np

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

    def __init__(self, score=1):
        if score < 0 or score > 1:
            raise ValueError(f"Score not in range 0 <= {score} <= 1")
        self.curscore = score
        self.maxscore = 1
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
        elif self.curscore == self.maxscore:
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

    @property
    def colors(self):
        return htmlcolors if self.html else colors

    @property
    def indent(self):
        return "&nbsp;&nbsp;" if self.html else " "

    def main(self, *infiles: cli.ExistingFile):
        for infile in infiles:
            (colors.blue | colors.bold).print(infile.stem)
            print()
            try:
                self.each(infile)
            except Exception as e:
                if len(infiles) > 1:
                    self.colors.fatal.print("Failed:", infile.stem)
                    self.colors.fatal.print(self.indent, e)
                else:
                    raise
            print()

    def each(self, infile: cli.ExistingFile):
        Score.colors = self.colors
        self.total_score = Score.empty()

        base = 'ipynb.fs.' + ('full' if self.full else 'defs') + '.' + infile.stem
        if self.hide:
            tmp = StringIO()
            with redirect_stdout(tmp):
                self.mod = import_module(base)
        else:
            self.mod = import_module(base)

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
                color.print(self.indent, f'Score', self.score)

                self.total_score += self.score
                del self.score

        if hasattr(self.__class__, "TOTAL"):
            self.total_score.maxscore = self.__class__.TOTAL

        color = self.total_score.color
        color.print('Score', self.total_score)

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
            return funct_wrapper
        else:
            return funct
        
    def get_variable(self, name):
        return getattr(self.mod, name, "")
    
    def get_answer(self, name, points):
        pts = self.get_variable(name)
        failed = points - pts
        if pts:
            self.success(msg="Instructor grade", factor=pts)
        if failed:
            self.failure("Instructor grade", factor=failed)

    def success(self, *, msg=None, factor=1):
        self.score += Score() * factor
        if self.verbose:
            self.colors.success.print('Scoring problem', self.score.times, 'with', factor, 'points')

    def failure(self, error, *, score=0, msg=None, factor=1):
        self.score += Score(score) * factor
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
        if item is None:
            return self.failure(f'"{inside}" not in None', msg=msg, factor=factor)
        if inside in item:
            return self.success(msg=msg, factor=factor)
        else:
            return self.failure(f'"{inside}" not in "{item}"', msg=msg, factor=factor)

    def compare(self, item, other, *, msg=None, factor=1):
        ans = item == other
        if isinstance(ans, np.ndarray):
            ans = np.all(ans)
        if ans:
            return self.success(msg=msg, factor=factor)
        else:
            return self.failure(f'"{item}" != "{other}"', msg=msg, factor=factor)

    def compare_close(self, item, other, *, msg=None, factor=1, rel_tol=1e-9, abs_tol=0.0):
        ans = np.isclose(item, other, rtol=rel_tol, atol=abs_tol)
        if isinstance(ans, np.ndarray):
            ans = np.all(ans)
        if ans:
            return self.success(msg=msg, factor=factor)
        else:
            return self.failure(f'"{item}" != "{other} within allowed limits"', msg=msg, factor=factor)

    def valid(self, item, *, msg=None, factor=1):
        if item:
            return self.success(msg=msg, factor=factor)
        else:
            return self.failure('Expected non-null input', msg=msg, factor=factor)

    def raises(self, exception, function, *args, factor=1, msg=None, **kargs):
        'Call a function with arguments, half score if some other exception is raised'
        try:
            function(*args, **kargs)
            return self.failure(self.indent, f'Expected {function.__name__} to raise {exception.__name__} and it didn\'t raise anything', msg=msg, factor=factor)
        except exception as e:
            return self.success(factor=factor, msg=msg)
        return self.failure(self.indent, f'Expected {function.__name__} to raise {exception} and it raised something else (half credit)', score=.5, msg=msg, factor=factor)

    def nullify(self, *, msg=None):
        'Clear the score with optional message'
        self.score.nullify()
        self.colors.red.print(self.indent, 'Problem failed')
        if msg:
            self.colors.red.print(self.indent, self.indent, f'{msg}')

