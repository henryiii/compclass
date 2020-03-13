## Installing


You should run:

```bash
conda env create
conda activate compclass
```

## Building

To run all the (runnable) notebooks:

```bash
cat runnable.txt | xargs jupyter nbconvert --execute --inplace
```

Then, to build the book:

```bash
jupyter-book create compclass --config _config.yml --toc _data/toc.yml --content-folder classes --extra-files images
jupyter-book build compclass/
```

## Maintaining 

To cleanup (using fish syntax):

```fish
pip install nbtoolbelt
nbtb clean --inplace -e -o -m collapsed,scrolled -v **.ipynb
```

Note that I added `-g "kernelspec"` as well originally to remove the incorrect kernel names.

You can force to black (fish syntax):

```fish
jupytext --pipe black **.ipynb
```

