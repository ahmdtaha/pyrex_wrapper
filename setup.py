

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
# from __future__ import unicode_literals
from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension
from glob import glob


import numpy


sourcefiles = ['pyxtutorial.pyx',"msrc.cpp"]
#sourcefiles.append("msrc.cpp")

extensions = [Extension("pyxtutorial", sourcefiles , include_dirs=[numpy.get_include()])]

setup(
  name = "pyxtutorial",
  version="1.0",
  description="Sample Python Rex Wrapper for C++ code",
  author="Ahmed Taha",
  ext_modules=cythonize(extensions),
  include_dirs=[numpy.get_include()]
)