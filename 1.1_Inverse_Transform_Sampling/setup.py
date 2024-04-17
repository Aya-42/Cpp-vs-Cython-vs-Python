# setup.py

from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy

# Get the location of the header files for NumPy
numpy_include = numpy.get_include()


setup(
    name='lorentzian_sampling_cy',
    ext_modules=cythonize(
        Extension(
            "lorentzian_sampling_cy",                             # Name of the module
            # Cython source file
            sources=["lorentzian_sampling_cy.pyx"],
            # Include NumPy headers
            include_dirs=[numpy_include]
        ),
        annotate=True  # Enable generation of the annotation file
    ),
    zip_safe=False,
)
