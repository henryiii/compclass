#!/usr/bin/env python

from plumbum import cli, colors
from importlib import import_module
from contextlib import redirect_stdout
from io import StringIO
import copy

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
        return f'{self.curscore} of {self.maxscore} ({self.curscore/self.maxscore:2.0%})'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.curscore},{self.maxscore})'


    @property
    def color(self):
        if self.curscore == self.maxscore:
            return colors.green
        elif self.curscore == 0:
            return colors.red
        else:
            return colors.yellow

    def nullify(self):
        self.curscore = 0


class Grader(cli.Application):
    full = cli.Flag('--full', help="Run the full notebook instead of just definitions")
    hide = cli.Flag('--hide', help="Hide the output (usually combined with --full)")

    def main(self, infile: cli.ExistingFile):
        base = 'ipynb.fs.' + ('full' if self.full else 'defs') + '.' + infile.stem
        if self.hide:
            tmp = StringIO()
            with redirect_stdout(tmp):
                self.mod = import_module(base)
        else:
            self.mod = import_module(base)

        (colors.info | colors.bold).print(self.mod.EID, ":", self.mod.NAME)
        self.total_score = Score()
        for i in range(10):
            if hasattr(self, f'process{i}'):
                self.score = Score()
                colors.info.print(f'Problem set {i}:')

                getattr(self, f'process{i}')()
                color = self.score.color
                color.print(f'  Score', self.score)

                self.total_score += self.score
                del self.score

        color = self.total_score.color
        color.print('Score', self.total_score)

    def success(self, *, msg=None, factor=1):
        self.score += Score() * factor

    def failure(self, error, *, score=0, msg=None, factor=1):
        self.score += Score(score)
        colors.fatal.print(f'  Test case {self.score.times}: {error}')
        if msg:
            colors.fatal.print('    ' + msg)

    # Comparison methods
    # All methods should either pass on msg and factor
    # as keyword only arguments

    def compare_in(self, item, inside, *, msg=None, factor=1):
        if inside in item:
            return self.success(msg=msg, factor=factor)
        else:
            return self.failure(f'"{inside}" not in "{item}"', msg=msg, factor=factor)

    def compare(self, item, other, *, msg=None, factor=1):
        if item == other:
            return self.success(msg=msg, factor=factor)
        else:
            return self.failure('"{item}" != "{other}"', msg=msg, factor=factor)

    def valid(self, item, *, msg=None, factor=1):
        if item:
            return self.success(msg=msg, factor=factor)
        else:
            return self.failure('Expected non-null input', msg=msg, factor=factor)

    def raises(self, exception, function, *args, factor=1, msg=None, **kargs):
        'Call a function with arguments, half score if some other exception is raised'
        try:
            function(*args, **kargs)
            return self.failure(f'  Expected {function.__name__} to raise {exception.__name__} and it didn\'t raise anything', msg=msg, factor=factor)
        except exception:
            return self.success(factor=factor, msg=msg)
        return self.failure(f'  Expected {function.__name__} to raise {exception.__name__} and it raised something else (half credit)', score=.5, msg=msg, factor=factor)

    def nullify(self, *, msg=None):
        'Clear the score with optional message'
        self.score.nullify()
        colors.red.print('  Problem failed')
        if msg:
            colors.red.print(f'    {msg}')

