from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy

# Getting the location of NumPy headers
numpy_include = numpy.get_include()

setup(
    name='logistic_map_cy',
    ext_modules=cythonize(
        Extension(
            "logistic_map_cy",                             # Name of the module
            sources=["logistic_map_cy.pyx"],               # Cython source file
            # Include NumPy headers
            include_dirs=[numpy_include]
        ),
        annotate=True  # Enable generation of the annotation file
    ),
    zip_safe=False,
)
