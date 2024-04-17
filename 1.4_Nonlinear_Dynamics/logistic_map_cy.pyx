from libc.math cimport log, fabs
import numpy as np
cimport numpy as np
import csv
import os


cdef double logistic_map_optimized(double x, double r):
    return r * x * (1 - x)


cpdef list compute_bifurcation_optimized(double[:] r_values, int num_generations, double initial_x=0.5, int transients=500):
    cdef list data = []
    cdef double x
    cdef int i, j
    cdef double r
    for r in r_values:
        x = initial_x
        # Transient iterations
        for i in range(transients):
            x = logistic_map_optimized(x, r)
        # Collect data after transients
        for j in range(num_generations - transients):
            x = logistic_map_optimized(x, r)
            data.append([r, x])
    return data


cpdef list compute_lyapunov_optimized(double[:] r_values, int num_generations, double initial_x=0.5):
    cdef list data = []
    cdef double x, derivative, lyapunov_sum
    cdef int i
    cdef double r
    for r in r_values:
        x = initial_x
        lyapunov_sum = 0
        for i in range(num_generations):
            x = logistic_map_optimized(x, r)
            derivative = r * (1 - 2 * x)
            if derivative != 0:
                lyapunov_sum += log(fabs(derivative))
        data.append([r, lyapunov_sum / num_generations])
    return data
