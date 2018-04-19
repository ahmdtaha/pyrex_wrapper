# distutils: language = c++
# distutils: sources = msrc.cpp
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
# from __future__ import unicode_literals
import numpy as np
cimport numpy as np
# Author: Deepak Pathak (c) 2016


cdef extern from "msrc.h":
    int add(int a,int b);

cdef extern from "msrc.h":
    void add(int a,int b,int * result);


def add_fn(a,b):
    return add(a,b)

def add_fn_ref(a,b,):
    cdef int result = -1
    add(a,b,&result)
    return result;
