# Computational Physics (draft syllabus)

## Class times:
M, W, F from 8:55 - 9:50 AM

## Introduction:
This course is designed to introduce students to modern computational methods for physics data analysis and modeling. Some programming experience will be useful, but is not required. The course uses Python and looks at a variety of common Scientific Python libraries. The aim of the course is to teach students how to solve problems and what to look for when searching for tools, rather than to teach all the details of specific tools. Common data manipulation and numerical analysis techniques will be investigated, with a strong focus on visualizing the results.

## Prerequisites:

Some knowledge of multi-dimensional calculus, linear algebra, and ordinary differential equations.

## Textbooks
Required textbook: *Computational Physics: Problem Solving with Python*, 3rd edition, by Landau, Páez, and Bordeianu [(free Enlarged eTextbook Python Third Edition)](https://www.eidos.ic.i.u-tokyo.ac.jp/~tau/lecture/computational_physics/docs/computational_physics.pdf)

Recommended textbook: *Python For Data Analysis*, 2nd Edition, by Wes McKinney (Author of the Pandas library). This book covers modern Python syntax and the Numpy, Matplotlib, and Pandas libraries from a data scientist's perspective.

## Expected outcome

Students should be able to solve a significant problem, use scientific Python tools, use git, and present their work. 

## Topics:

#### Scientific computing in Python
The course will cover basics needed for modern scientific computing, including the shell, git, and Python. Students will learn to manipulate non-uniform data and visualize the results. Students will learn how to design a solution to a problem and present it to others. The course will also cover performance topics; students will learn to watch for slow code and optimize code performance.

#### Mathematical topics that will be covered
Uncertainty and error: A look at making a calculation based on physical measurements and interpreting the results.

Linear algebra: An introduction to vector and matrix manipulations and some assorted linear algebra topics.

Differentiation and Integration:  Covering several integration and differentiation methods, Monte Carlo integration, as well as using packages.

Statistical distributions and fitting: Manually performing a linear regression, then using commonly used packages to perform the fitting. A look at correlation coefficients and visualization.

Differential equations.

Fourier analysis and filtering signals.

Machine Learning: A brief intro to Machine Learning, including a look at the toolkits for ML.

#### Term Project

Students will select and solve a specific problem and present the results.

## Schedule:

Chapters in the required book are noted when applicable.

| Week | Monday                       | Wednesday                  | Friday              |
|------|------------------------------|----------------------------|---------------------|
| 1  | 8-27  Introduction             | 8-29 Using Python          | 8-31 OO programming (4) |
| 2  | 9-03  *Labor day*              | 9-05 Numerical tools       | 9-07 Error accumulation (2) |
| 3  | 9-10  Plotting (3)             | 9-12 Advanced plotting (3) |  9-14 Using git |
| 4  | 9-17  Random numbers (5)       | 9-19 Monte Carlo (5)       | 9-21  **Project selection** |
| 5  | 9-24  Integration rules (6)    | 9-26 MC Integration (6)    | 9-28 Numerical differentiation (7) |
| 6  | 10-01 Vectorization (8)        | 10-03 Linear algebra (8)   | 10-05 Linear regression (8) |
| 7  | 10-08 Structured tabular data  | 10-10 Cuts and histograms  | 10-12 *Fall reading days* |
| 8  | 10-15 Generating distributions | 10-17 Minimization and fitting | 10-19 Fitting tools |
| 9  | 10-22 Confidence intervals     | 10-24 Markov Chain Monte Carlo | 10-26 Performance computing (14) |
| 10 | 10-29 Intro to ODEs (9)        | 10-31 Runge–Kutta algorithm (9) | 11-02 Solving ODE problems (9) |
| 11 | 11-05 Fourier Series (10)      | 11-07 Fourier transforms (10) | 11-09 **Project progress report** |
| 12 | 11-12 *Veterans day*           | 11-14 Filtering signals (10) | 11-16 Fast Fourier transform (10) |
| 13 | 11-19 **Review** | 11-21 **Student requested topics** | 11-23 *Thanksgiving* |
| 14 | 11-26 Static computation graphs | 11-28 Applied ML topics | 11-30 Sharing and documenting code |
| 15 | 12-03 **Term project presentations** | 12-05 **Term project presentations** | 12-07 **Term project presentations** |

Examinations week of 12-10.



<!--
The following are responses I've received to emails, to make sure I am addressing the comments.

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

-->
