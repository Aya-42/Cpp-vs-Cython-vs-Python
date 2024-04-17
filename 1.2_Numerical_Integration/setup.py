# setup.py

from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy

# Get the location of the header files for NumPy
numpy_include = numpy.get_include()


setup(
    name='bessel_cy',
    ext_modules=cythonize(
        Extension(
            "bessel_cy",                             # Name of the module
            sources=["bessel_cy.pyx"],               # Cython source file
            # Include NumPy headers
            include_dirs=[numpy_include]
        ),
        annotate=True  # Enable generation of the annotation file
    ),
    zip_safe=False,
)
