from libc.math cimport sin, cos, pi
from scipy.special.cython_special cimport j0
import numpy as np 
cimport numpy as np

cdef double f(double theta, double x):
    """Calculate the function to be integrated to produce the Bessel function, Cythonized."""
    return cos(x * sin(theta))


cpdef double trapezoid_rule(double x, int N):
    """Calculate the integral of the function using the trapezoid rule, Cythonized."""
    cdef double delta_theta = pi / N
    cdef double sum = 0.5 * (f(0, x) + f(pi, x))
    cdef int i
    
    for i in range(1, N):
        sum += f(i * delta_theta, x)
    
    return sum * delta_theta


cpdef double simpson_rule(double x, int N):
    """Calculate the integral of the function using Simpson's rule, Cythonized."""
    if N % 2 == 1:
        N += 1  # Simpson's rule requires an even number of intervals
        
    cdef double delta_theta = pi / N
    cdef double sum = f(0, x) + f(pi, x)
    cdef int i
    
    for i in range(1, N, 2):
        sum += 4 * f(i * delta_theta, x)
    
    for i in range(2, N-1, 2):
        sum += 2 * f(i * delta_theta, x)
    
    return sum * delta_theta / 3

cpdef calculate_relative_errors(double x_extremum, np.ndarray[np.int_t, ndim=1] N_values):
    """Calculate relative errors for a specific x value using both trapezoid and Simpson's rules."""
    cdef double actual_j0_extremum = j0(x_extremum)
    cdef list relative_errors_trap = []
    cdef list relative_errors_simp = []
    cdef double trap_approx, simp_approx
    cdef double rel_error_trap, rel_error_simp
    cdef int N

    for N in N_values:
        trap_approx = trapezoid_rule(x_extremum, N)  
        simp_approx = simpson_rule(x_extremum, N)  

        # Calculate relative errors for trapezoidal and Simpson's rule approximations
        rel_error_trap = np.abs((trap_approx - actual_j0_extremum) / actual_j0_extremum)
        rel_error_simp = np.abs((simp_approx - actual_j0_extremum) / actual_j0_extremum)

        # Append errors to lists
        relative_errors_trap.append(rel_error_trap)
        relative_errors_simp.append(rel_error_simp)

    return relative_errors_trap, relative_errors_simp






