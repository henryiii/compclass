## Installing


You should run:

```bash
conda env create
conda activate compclass
```

## Building

```bash
jupyter-book create compclass --config _config.yml --toc _data/toc.yml --content-folder classes --extra-files images
jupyter-book build --execute compclass/
```

## Maintaining 

To cleanup (using fish syntax):

```fish
pip install nbtoolbelt
nbtb clean --inplace -e -o -m collapsed,scrolled -v **.ipynb
```

Note that I added `-g "kernelspec"` as well originally to remove the incorrect kernel names.


