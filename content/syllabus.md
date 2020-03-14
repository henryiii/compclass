# PHYS 5041/6041: Computational Physics

## Class information:
* Instructor: Henry Schreiner @ CERN in Geneva, Switzerland via WebEx.
* M, W, F from 8:55 - 9:50 AM in Geo/Phys Room 300/Hauck. Remote attendance (by request) and recorded lectures will be available.
* Office hours: 10AM-11AM Monday and Friday via video chat (WebEx or Skype, TBD).
* Course websites:
    - Blackboard: `meta_schreihf_2962 (Meta 18FS-Full) TOPICS IN PHYSICS (001)`
    - Lecture recordings: [uc.box.com/v/PES0765](https://uc.box.com/v/PES0765)
    - Source files: [github.com/henryiii/compclass](https://github.com/henryiii/compclass).

## Introduction:
This course is designed to introduce students to modern computational methods for physics data analysis and modeling. The course is intended for upper-level undergraduates and graduate students. The course was designed for physics students, but should also be appropriate for students in mathematics and other physical sciences.  Some programming experience will be useful, but is not required. The course uses Python and looks at a variety of common problems and Scientific Python libraries. The aim of the course is to teach students how to solve problems and what to look for when searching for tools, rather than to teach all the details of specific tools. Common data manipulation and numerical analysis techniques will be investigated, with a strong focus on visualizing the results.

## Prerequisites:

Some knowledge of multi-dimensional calculus, linear algebra, and ordinary differential equations.

## Textbooks
Required textbook: *Computational Physics: Problem Solving with Python*, 3rd edition, by Landau, Páez, and Bordeianu [(free Enlarged eTextbook Python Third Edition)](https://www.eidos.ic.i.u-tokyo.ac.jp/~tau/lecture/computational_physics/docs/computational_physics.pdf)

Recommended textbook: *Python For Data Analysis*, 2nd Edition, by Wes McKinney (Author of the Pandas library). This book covers modern Python syntax and the Numpy, Matplotlib, and Pandas libraries from a data scientist's perspective.

## Expected outcome

Students should be able to solve a significant problem, use scientific Python tools, use the git version control system, and present their work. 

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

## Grading
* Weekly problem set: 45%
* Term project:
    * Oral presentation: 20%
    * Writeup: 20%
* JiTT Quizzes: 15%

Just in Time Teaching (JiTT) quizzes will be due at midnight before the class they cover. 25% of the grade for the JiTT quizzes will be based solely on on-time completion. These will test preparation (reading the material in the book or other recommended sources) before the class begins, and will help shape the lecture to provide the most relevant information.

## Classroom Procedures/Policies

#### Technology use during/for class

The class will be interactive; registered students have access to OSC computing resources. Students are expected to either use the computers in the classroom or their personal devices. Lectures are designed as notebook that students can follow along with during the class.

#### Attendance Policy

You are expected to attend each class if you can, and watch the recording if you are not available (with prior permission). All materials should be turned in promptly before the set deadlines - please contact me if you need an extension *before* a deadline is passed.

#### Conduct

The University Rules, including the Student Code of Conduct, are applicable and should be followed in this class. Any violation will be dealt with on an individual basis according to the severity of the misconduct. For example, any material based heavily on outside sources should be attributed in a code comment or a similar manor.


## Schedule:

Chapters in the required book are noted when applicable. This is a tentative schedule and subject to change.

| Week | Monday                       | Wednesday                  | Friday              |
|------|------------------------------|----------------------------|---------------------|
| 1  | 8-27  Introduction             | 8-29 Using Python part 1   | 8-31 Using Python part 2 |
| 2  | 9-03  *Labor day*              | 9-05 OO programming (4)    | 9-07 Error accumulation (2) |
| 3  | 9-10  Numerical tools          | 9-12 Plotting (3)          | 9-14 Using git |
| 4  | 9-17  Random numbers (5)       | 9-19 Monte Carlo (5)       | 9-21  **Project selection** |
| 5  | 9-24  Integration rules (6)    | 9-26 MC Integration (6)    | 9-28 Numerical differentiation (7) |
| 6  | 10-01 Vectorization (8)        | 10-03 Linear algebra (8)   | 10-05 Linear regression (8) |
| 7  | 10-08 Structured tabular data  | 10-10 Cuts and histograms  | 10-12 *Fall reading days* |
| 8  | 10-15 Generating distributions | 10-17 Minimization and fitting | 10-19 Fitting tools |
| 9  | 10-22 Confidence intervals     | 10-24 Markov Chain Monte Carlo | 10-26 Performance computing (14) |
| 10 | 10-29 Intro to ODEs (9)        | 10-31 Runge–Kutta algorithm (9) | 11-02 Solving ODE problems (9) |
| 11 | 11-05 Fourier Series (10)      | 11-07 Fast Fourier Transform (10) | 11-09 **Project progress report** |
| 12 | 11-12 *Veterans day*           | 11-14 **Project progress report** | 11-16 Filtering signals (10) |
| 13 | 11-19 **Review**               | 11-21 **Student requested topics** | 11-23 *Thanksgiving* |
| 14 | 11-26 Static computation graphs | 11-28 Applied ML topics | 11-30 Sharing and documenting code |
| 15 | 12-03 **Term project presentations** | 12-05 **Term project presentations** | 12-07 **Term project presentations** |

Final writeup due during examinations week of 12-10.

------------------------- 

I reserve the right to update this syllabus as class needs arise. Be assured that I will communicate to you any changes to our schedule, syllabus or policies quickly and efficiently through Blackboard.
