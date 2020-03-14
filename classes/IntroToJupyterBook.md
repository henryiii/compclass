![CompClass Logo](images/SimpleLogo.png)

Welcome to the CompClass website! This was prepared about a year after the
class was finished, in order to make it easier to navigate and view the course
materials. There have been some significant updates since the class was taught;
Python 3.7 is much more common and 3.8 is starting to take hold (and is used by
default for the rendering, though 3.7 is the maximum syntax used in the
examples and most code is 3.6 compatible). Python 2 is now officially at
End-of-Life.

This book was created with JupyterBook, and is based on the original Jupyter
notebooks.


## Usage: online

On any page, you can click the "Interact" button. This may take a minute or two
to start, but will drop you into a JupyterLab session with the current page
open. From here, you can explore and all the notebooks.

If you really don't want to leave the page, try the "Thebelab" button. That
will make all cells in the current page editable and runnable without leaving
the page.

## Usage: installing

If you want to run this locally, download
[miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html#)
for your OS. If you are on macOS and you use brew, then `brew cask install
miniconda` will do.

Download the [github repository](https://github.com/henryiii/compclass) with
your favorite download method, such as `git clone
https://github.com/henryiii/compclass` (or, if you use SSH, then
`git@github.com:henryiii/compclass`).

In the compclass directory, run:

```python
conda env create
```

This will create the "compclass" environment from the file `environment.yml`. Then you can run:

```bash
conda activate compclass
```

To use the environment. It will have everything you need!

## Using: What about the unrun notebooks?

There are a small number of notebooks that are not run by the Continuous Integration (CI) that builds this site. The reasons are listed below:


* `week9/2_mcmc`: Uses MCM3, which uses Theano, which is a discontinued ML
  tool. MCM3 is supposed to maintain it while using it, but I found it buggy on
  some systems.
* `week12/0_cupy_fractal`: Requires CuPy and a GPU
* `week12/1_PyBindNumba`: Requires IPyBind, which I didn't install (and
  building C++ on multiple systems is a bit tricky)
* `week12/1_Fitting`: Uses several ML frameworks not ready for Python 3.8
* `week12/1_guis`: Really not applicable to a notebook environment
* `week14/1_graphs`: Uses several ML frameworks not ready for Python 3.8
* `week14/2_ml`: Uses several ML frameworks not ready for Python 3.8

Also, note that several notebooks use interactive features of MPL (like
notebook/widget backends), and at least one uses Bokeh, which do not render
properly in a static webpage environment - view them in an interactive backend
for best effect.
