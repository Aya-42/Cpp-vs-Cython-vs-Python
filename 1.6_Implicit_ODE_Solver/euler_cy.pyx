import numpy as np
cimport numpy as cnp

def backward_euler_optimized(double y0, double t_end, double dt):
    cdef int n_steps = int(t_end / dt) + 1
    cdef cnp.ndarray[cnp.float64_t, ndim=1] times = np.linspace(0, t_end, n_steps)
    cdef cnp.ndarray[cnp.float64_t, ndim=1] ys = np.zeros(n_steps, dtype=np.float64)
    ys[0] = y0

    cdef int i
    for i in range(1, n_steps):
        ys[i] = ys[i-1] / (1 + dt)

    return times, ys