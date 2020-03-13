
You should run:

```bash
conda env create
conda activate compclass
```

To cleanup (using fish syntax):

```fish
pip install nbtoolbelt
nbtb clean --inplace -g "kernelspec" -e -o -m collapsed,scrolled -v **.ipynb
```


