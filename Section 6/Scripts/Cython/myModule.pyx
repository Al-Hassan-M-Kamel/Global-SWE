
import numpy as np
cimport numpy as cnp
cimport cython

# Tell Cython we're using C math functions
from libc.math cimport sqrt, exp
from libc.stdlib cimport malloc, free

# ─────────────────────────────────────────────
# 1. Basic typed function (fastest form)
# ─────────────────────────────────────────────
cpdef double fast_dot(double[:] a, double[:] b):
    """Dot product of two arrays — fully typed, no Python overhead."""
    cdef int i, n = a.shape[0]
    cdef double result = 0.0
    for i in range(n):
        result += a[i] * b[i]
    return result