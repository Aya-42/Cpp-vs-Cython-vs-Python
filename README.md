# C++ vs Cython vs Python for Scientific Computing

## Overview

This assignment compares computational techniques using Python, Cython, and C++ across a series of numerical problems. The focus is on implementing efficient algorithms, enhancing understanding of different programming paradigms, and evaluating runtime performance.

runtime table



#### Environment Setup

- **Python**: Version 3.8+, with libraries NumPy, matplotlib for computations and plotting. scipy for famous functions, pandas for plotting, csv to write data, panda to read it
- **Cython**: Setup with Python for performance enhancements. Use of Cython compiler for building optimized code.
- **C++**: GCC compiler (version 9+) for C++17 standards. Use standard libraries only.

#### File Structure

- **Repository Root**:
  - `README.md`: Project overview and setup instructions.
  - `requirements.txt`: List of Python dependencies.
- **1.1_Inverse_Sampling_Transform**:
  - `problem1.py`, `problem2.py`, ..., `problem6.py`: Python implementations.
- **Cython**:
  - `problem1.pyx`, `setup1.py`, ..., `problem6.pyx`, `setup6.py`: Cython files and setup scripts.
- **C++**:
  - `problem1.cpp`, ..., `problem6.cpp`: C++ source files for each problem.
  - `Makefile`: Compilation instructions.
  - `#include "utils.h"`
- **Results**:
  - `data/`: Output data files used for generating plots.
  - `plots/`: Generated plots in PNG or PDF format. 



## 1.1



### Problem 1.1: Inverse Transform Sampling

The objective of this problem is to demonstrate how to generate random numbers from a non-uniform distribution using inverse transform sampling. Our approach involves sampling from a Lorentzian distribution using the transformation \$ x = \frac{\Gamma}{\tan(\pi (u - 0.5))}$, where \(u) is uniformly distributed between 0 and 1, and $\Gamma{} = 1$ represents the half-width at half-maximum (HWHM).

Initial profiling pointed to the inverse transform function as the main bottleneck. Despite optimizations in Python and Cython, the biggest speed boost came from implementing the function in C++, achieving a dramatic change in the order of magnitude. Figure (1) shows a histogram of sampled values against the theoretical Lorentzian PDF, visually validating our method's accuracy.

![](D:\Google%20Drive\2.T\.HPC\C++%20vs%20Cython%20vs%20Python\1.1_Inverse_Transform_Sampling\plots\Figure_1.png)

Runtime Comparison

- **Python**: (2.19) seconds.
- **Cython**: (1.74) seconds, showing improved efficiency through compilation optimizations.
- **C++**: (0.0000141) seconds, dramatically faster due to lower-level system access and optimized memory management, the implementation was vectorized and did not use for loops, which helped achieve this runtime.

## 1.2

Python execution time: 0.14697027206420898
Cython execution time: 0.03648805618286133
Python relative error calculation time: 0.009775400161743164
Cython relative error calculation time: 0.0016863346099853516

![](D:\Google%20Drive\2.T\.HPC\C++%20vs%20Cython%20vs%20Python\1.2_Numerical_Integration\plots\Figure_1.png)

![](D:\Google%20Drive\2.T\.HPC\C++%20vs%20Cython%20vs%20Python\1.2_Numerical_Integration\plots\Figure_2.png)

![](D:\Google%20Drive\2.T\.HPC\C++%20vs%20Cython%20vs%20Python\1.2_Numerical_Integration\plots\Figure_3.png)

## 1.4

Python bifurcation calculation time: 0.1191098690032959
Python Lyapunov calculation time: 0.379544734954834
Cython bifurcation calculation time: 0.030930519104003906
Cython Lyapunov calculation time: 0.0015032291412353516

Bifurcation calculation time: 0.0111693 s
Lyapunov calculation time: 0.0106237 s



![](D:\Google%20Drive\2.T\.HPC\C++%20vs%20Cython%20vs%20Python\1.4_Nonlinear_Dynamics\plots\bifurcation_data_c_bifurcation.png)

![](D:\Google%20Drive\2.T\.HPC\C++%20vs%20Cython%20vs%20Python\1.4_Nonlinear_Dynamics\plots\lyapunov_data_cy_lyapunov.png)

## 1.6

Time taken by Python code: 0.04189586639404297

Time taken by Cython code: 0.0009586811065673828

Time taken by C++ code: 0.0041156s

![](D:\Google%20Drive\2.T\.HPC\C++%20vs%20Cython%20vs%20Python\1.6_Implicit_ODE_Solver\plots\Figure_1.png)



## Runtime Analysis





## Results and Discussion

challenges I faced, tools I used, goals for this assignment, my thinking
