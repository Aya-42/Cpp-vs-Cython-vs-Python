# C++ vs Cython vs Python for Scientific Computing

## Overview

[GitHub - Aya-42/Cpp-vs-Cython-vs-Python](https://github.com/Aya-42/Cpp-vs-Cython-vs-Python)

This assignment compares computational techniques using Python, Cython, and C++ across a series of numerical problems. The focus is on implementing efficient algorithms, enhancing understanding of different programming paradigms, and evaluating runtime performance.

## Environment Setup

- **Python**: Version 3.8+, with libraries NumPy, matplotlib for computations and plotting. Scipy for infamous functions. csv to write data, pandas to read it
- **Cython**: Setup with Python for performance enhancements. Use of Cython compiler for building optimized code.
- **C++**: GCC compiler (version 9+) for C++17 standards. Use standard libraries only.

### File Structure

- **Repository Root**:
  - `README.md`: Project overview
  
  - **1.n_Problem**:
  
  - `problem.py`, `plotting_script.py`: Python implementations.
  
  - `problem.pyx`, `setup.py`: Cython files and setup scripts.
  
  - `problem.cpp`: C++ source files for each problem.
  - `utils.h`:  Common function implementations that are often reused
  
  - `data/`: Output data files used for generating plots.
  - `plots/`: Generated plots in PNG or PDF format. 

## 1.1: Inverse Transform Sampling

The objective of this problem is to demonstrate how to generate random numbers from a non-uniform distribution using inverse transform sampling. Our approach involves sampling from a Lorentzian distribution using the transformation $x = \frac{\Gamma}{\tan(\pi (u - 0.5))}$, where u is uniformly distributed between 0 and 1, and $\Gamma{} = 1$ represents the half-width at half-maximum (HWHM). Figure (1) shows a histogram of sampled values against the theoretical Lorentzian PDF, visually validating our method's accuracy.

![.](1.1_Inverse_Transform_Sampling/plots/Figure_1.png "Figure (1)")

### Runtimes

Initial profiling pointed to the inverse transform function as the main bottleneck. Despite optimizations in Python and Cython, the biggest speed boost came from implementing the function in C++, achieving a dramatic change in the order of magnitude.

- **Python**: (2.19) seconds.
- **Cython**: (1.74) seconds, showing improved efficiency through compilation optimizations.
- **C++**: (0.0000141) seconds, dramatically faster due to lower-level system access and optimized memory management, the implementation was vectorized and did not use for loops, which helped achieve this runtime.

## 1.2: Numerical Integration of Bessel Function

The objective here is to approximate the Bessel function $ J_0(x)$ through numerical integration. We integrate the function $f(\theta) = \cos(x \sin(\theta))$ using the trapezoid and Simpson’s rule and compare the results against known values of $J_0(x)$. Shown in Figure (2) for different values of x.

![.](1.2_Numerical_Integration/plots/Figure_3.png "Figure (2)")


Figure (3) displays the results of approximating $J0​(x)$ using both the trapezoid and Simpson's rule across the domain $[0, 10]$, compared against values computed with standard library functions.

![.](1.2_Numerical_Integration/plots/Figure_1.png "Figure (3)")

In Figure (4), the log-log plot of relative errors showcases how the error diminishes with an increasing number of steps (N) for both the trapezoid and Simpson's methods in Python and Cython. From the slope of each curve, we can infer the convergence order. A steeper slope indicates a higher order of convergence and hence a more efficient approach to the true value. The plot suggests that the Simpson's method converges faster than the trapezoid method, evidenced by its flatter error curve, which indicates a lower error at equivalent step counts. ![.](1.2_Numerical_Integration/plots/Figure_2.png "Figure (4)")


### Runtimes

Profiling showed integration to be the most time-consuming process, with error computation also slowing things down. Cython was the quickest, likely due to its compiled nature and optimized numeric operations. C++ was slower, possibly due to less optimized code. An increase of performance in C++ is expected as we rely less and less on for loops and employ vectorization.

- **Cython**: \(0.095\) sec - the fastest, benefits from both Python's ease and C's speed.
- **C++**: \(0.148\) sec - slower, potentially from less efficient looping or lack of numerical optimizations.
- **Python**: \(0.355\) sec - the slowest, hindered by its overhead as an interpreted language.

### Problem 1.4: Nonlinear Dynamics and Logistic Map

The objective is to explore the chaotic behavior and bifurcation in the logistic map. The task involves iterating the logistic map for a range of values to observe the transition from stability to chaos, characterized by fixed points, periodic orbits, and chaotic regions. The bifurcation diagram (Figure 5) should visually present how, as the parameter ( r ) varies, the system transitions from order to chaos. As the parameter r increases, the logistic map evolves from steady-state fixed points to periodic cycles and then to chaotic behavior.

<img src="file:///D:/Google%20Drive/2.T/.HPC/C++%20vs%20Cython%20vs%20Python/1.4_Nonlinear_Dynamics/plots/bifurcation_data_c_bifurcation.png" title="" alt="" data-align="center">

Figure (6) shows a plot of the Lyapunov exponent across a range of ( r ) values. It moves from negative to positive at approximately 3.5, marking the onset of chaos.

<img src="file:///D:/Google%20Drive/2.T/.HPC/C++%20vs%20Cython%20vs%20Python/1.4_Nonlinear_Dynamics/plots/lyapunov_data_cy_lyapunov.png" title="" alt="" data-align="center">

### Runtimes

Profiling indicates that the iterative nature of the logistic map is the primary computational load. Across implementations, the Cython code proved to be the most efficient, leveraging NumPy’s optimized libraries, while the C++ implementation, lacking such optimizations and reliant on explicit loops, did not achieve the same level of performance. An increase of performance in C++ is expected as we rely less and less on for loops and employ vectorization.

- **Python:**
  
  - Bifurcation calculation took (0.119) seconds, with the overhead attributed to the high-level language features.
  
  - Lyapunov exponent calculation was (0.380) seconds, slower due to the intensive floating-point operations and function call overheads.

- **Cython**:
  
  - Bifurcation calculation time dropped to (0.031) seconds, showing improvement thanks to static typing and optimized number-crunching.
  - Lyapunov exponent calculation was remarkably fast at (0.0015) seconds, demonstrating Cython's ability to close the gap with lower-level languages.

- **C++**:
  
  - Bifurcation calculation completed in (0.011) seconds, and Lyapunov exponent calculation in (0.011) seconds, both benefitting from the highly efficient loops and arithmetic optimizations available in compiled C++ code., but not completely taking advantage of vectorization, and other optimization techniques, thus slower than Cython.

## 1.6: Implicit ODE Solver

The aim is to implement and examine the backward Euler method as an implicit solver for the exponential decay ODE. This problem evaluates the method's stability and accuracy, particularly in handling stiff ODEs. The figure would show a curve depicting how the relative error in the numerical solution of an ODE at t=16 changes with decreasing time step sizes on a logarithmic scale. Smaller time steps, resulting from larger n values, should correlate with reduced error, indicating higher numerical accuracy. The slope of the curve on this log-log plot can reveal the order of accuracy of the backward Euler method: a steeper slope suggests a higher-order accuracy. As n increases, we'd expect the curve to flatten out as the method reaches its limit of precision given the machine's floating-point arithmetic.<img src="file:///D:/Google%20Drive/2.T/.HPC/C++%20vs%20Cython%20vs%20Python/1.6_Implicit_ODE_Solver/plots/Figure_1.png" title="" alt="" data-align="center">

The time step (∆t) directly affects solution accuracy in the backward Euler method, with smaller steps yielding more precise results. Larger ∆t can compromise accuracy but maintains stability, making this method reliable for stiff ODEs where smaller steps are not computationally feasible.

### Runtimes

The computational load primarily comes from the iterative solver required in the backward Euler method. Across implementations, the Cython code proved to be the most efficient, leveraging NumPy’s optimized libraries, while the C++ implementation, lacking such optimizations and reliant on explicit loops, did not achieve the same level of performance. An increase of performance in C++ is expected as we rely less and less on for loops and employ vectorization.

- **Python**: \(0.0419\) seconds, slower due to interpreted nature.
- **Cython**: \(0.00096\) seconds, achieving significant performance gains through C-level optimizations.
- **C++**: \(0.00412\) seconds, faster than Python but surprisingly slower than Cython, possibly due to differences in compiler optimizations or overheads.
