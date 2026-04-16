from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np

ext = Extension(
    name="mymodule",
    sources=["mymodule.pyx"],
    include_dirs=[np.get_include()],         # NumPy C headers
    # extra_compile_args=["-fopenmp", "-O3"],  # OpenMP + max optimization
    # extra_link_args=["-fopenmp"],            # Link OpenMP runtime
    # # If you also use OpenCL, add:
    # # libraries=["OpenCL"],
    # # library_dirs=["/usr/lib/x86_64-linux-gnu"],
)

setup(
    name="mymodule",
    ext_modules=cythonize(
        [ext],
        compiler_directives={
            "language_level": "3",
            "boundscheck": False,   # Skip index bounds checking (faster)
            "wraparound": False,    # Skip negative indexing (faster)
            "cdivision": True,      # Use C division (no Python ZeroDivisionError)
        }
    ),
)