from libc.math cimport tan, pi
import numpy as np
cimport numpy as np


cpdef np.ndarray[np.float64_t, ndim=1] lorentzian_transform_optimized(np.ndarray[np.float64_t, ndim=1] u, double gamma=1):
    cdef Py_ssize_t i
    cdef Py_ssize_t n = u.shape[0]
    cdef np.ndarray[np.float64_t, ndim=1] results = np.empty(n, dtype=np.float64)

    for i in range(n):
        results[i] = gamma / tan(pi * (u[i] - 0.5))

    return results

