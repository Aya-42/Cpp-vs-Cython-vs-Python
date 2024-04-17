# setup.py

from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy

# Get the location of the header files for NumPy
numpy_include = numpy.get_include()


setup(
    name='euler_cy',
    ext_modules=cythonize(
        Extension(
            "euler_cy",                             # Name of the module
            sources=["euler_cy.pyx"],               # Cython source file
            # Include NumPy headers
            include_dirs=[numpy_include]
        ),
        annotate=True  # Enable generation of the annotation file
    ),
    zip_safe=False,
)
