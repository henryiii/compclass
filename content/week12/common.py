import numpy as np
from iminuit import Minuit
import math

np.random.seed(42)

dist = np.hstack([
    np.random.normal(loc=1, scale=2., size=500_000),
    np.random.normal(loc=1, scale=.5, size=500_000)
])

default_params = dict(
    f_0=.5,
    error_f_0=.01,
    limit_f_0=(0,1),

    mean=1.5,
    error_mean=.01,
    limit_mean=(-10,10),

    sigma=.4,
    limit_sigma=(0,1),
    error_sigma=.01,

    sigma2=3.,
    error_sigma2=.01,
    limit_sigma2=(1,3),
)


class Compare:
    def __init__(self, value):
        self.value = value
        
    def __eq__(self, other):
        if other == self.value:
            return True
        
        frac = abs(other - self.value) / self.value
        print(f'Missed by: {frac:.3}')
        return frac < .00001

likelyhood_answer = Compare(4976157.922404283)

def run_and_print(minuit):
    minuit.print_level=0
    a,b = minuit.migrad()
    print("FCN: {nfcn}\nis_valid: {is_valid}\nfval: {fval}\nedm: {edm}\n".format(**a))