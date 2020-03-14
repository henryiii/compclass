from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from IPython.display import display_html

def read_pretty(filename):
    with open(filename) as f:
        code = f.read()

    formatter = HtmlFormatter()
    display_html('<style type="text/css">{}</style>{}'.format(
        formatter.get_style_defs('.highlight'),
        highlight(code, PythonLexer(), formatter)), raw=True)