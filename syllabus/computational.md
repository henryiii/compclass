# Computational Physics

## Introduction:
This course is designed to introduce students to modern data analysis techniques and methods. Some programming experience recommended but not required. The course uses Python and looks at a variety of common Scientific Python libraries; though the aim of the course is to teach students how to solve problems and what to look for when searching for tools, rather than to teach the details of specific tools. Common data manipulation and numerical analysis techniques will be investigated, with a strong focus on visualizing the results.

## Prereqs: Calculus 1
Recommended textbook: Python For Data Analysis, 2nd Edition, by Wes McKinney (Author of the Pandas library)

## Topics:

Intro to Scientific Computing (Essentials Kit - like content)
Probably including basics of shell, git, python, and packaging. Depends a bit on whether I can run everything on OSC resources, which I’m hoping I can. This will mostly be “just enough” to get going, then will be included as necessary afterwords. This is “Essentials Kit” like content.

#### Linear Algebra
An introduction to vector and matrix manipulations (Numpy) and some linear algebra topics.

#### Data manipulation and visualization 
Moving into non-uniform data manipulation (Pandas - this is often the “R” section of similar courses) and plotting (Matplotlib). Quite a few examples here, such as making a selection, grouping, and categorizing.

#### Integration
Monte-carlo method, using SciPy integrators.

#### Performance
How to avoid slow code and optimize code performance. Loops vs. Vectors, brief look at adding Numba decorators to make even the “dumb” solution fast.

#### Fitting
Manually performing a linear regression, then using SciPy.Optimize [along with mention of other tools]. A look at correlation coefficients and visualization.

#### FFT
Numpy.fft

#### How to design a solution
A brief excursion into thinking of data as an object (a taste of OOP) and how to design a library to solve a specific problem. This topic will be very brief, and is intended to give the interested student an idea of what to look for and where.

#### ML
A brief intro to Machine Learning, including a look at one of the toolkits for ML. This is intended as a followup to the previous section, illustrating a good design, packaging conceptual ideas into ML layers.

#### Term Project
Students will select and solve a specific problem and present the results.


---

# Slava:

Needs of my students may not be typical but here they are:

1. Statistical methods and distributions fitting, including MLE, KS and chi squared, Bayesian and MCMC, bootstrap and jackknife, distributions algebra (products, etc.)
2. Programming in Mathematica and Matlab, including writing a toolbox, when necessary, such as for the confluent HypergeometricU function that my student just did.
3. Programming in high-level languages, such as Julia, C++, etc.

# Richard Gass

I tried to cover the numeric topics that I thought were most relevant to physics. I talked about numerical differentiation and integration, solution of ODE’s, root finding, and solving PDE’s by finite differences. I did not do finite elements but I might if I taught the course again.I tried to use examples that were reverent to physics. As you know Mathematica has a lot  of high level functions should a NIntegrate and these can be “black boxy”,  although no more in my option than a numerical library, so I tried to introduce each topic with a simple method such as Simpsons rule for numerical integration and then move on to using NIntegrate and talking about what could go wrong and how we would know that we should be suspicious. I talked a lot about sanity checking your results, testing against special cases an so-on. I tried to stick a balance between teaching computation and physics and I was never sure that I got it right or even if the was a "right” . I am in Maine for another week but I would be happy to talk at greater length when I get back.

# Colin Bishoff

Sorry for the slow reply. I was on vacation and just got back today. I did chat a bit with Mike this afternoon.

Here are some of the topics that I think are important to include:

* Plotting / data visualization, including time series, correlation (scatter) plots, histograms, etc.
* Non-linear curve fitting / chi^2 minimization
* FFT

A more advanced topic that could be a good fit is Markov Chain Monte Carlo (MCMC).

Not sure if you are planning to get into statistical methods, but on the data analysis side I could imagine getting into likelihood vs pdf, credible vs confidence intervals, Feldman-Cousins interval construction, etc.

A tool that is useful in astronomy is HEALPix (Hierarchical Equal-Area isoLatitude Pixelization), which is a nice way to pixelize the sphere that lends itself to efficient spherical harmonic transforms. There is a pretty good python module (https://healpy.readthedocs.io). Healpix can be used to visualize and manipulate maps of the sky that are sufficiently wide area that they can’t be treated as flat.

I think I sent you this link before, but here are the notebooks that I wrote for my astrophysics class last year:
https://github.com/cbischoff/phys4025

The computational techniques used for each exercise are

* color_vs_temperature: manipulating numpy arrays
* stellar_structure: numerical integration
* ligo: FFT
* kepler: curve fitting


I would be interested in seeing your syllabus once you have it.


