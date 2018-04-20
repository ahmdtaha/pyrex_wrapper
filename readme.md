# Sample Python Rex Wrapper for C++ code
This is a simple tutorial for creating python wrapper for c++ code. Two simple C++ functions is wrapped and called from python code. One function takes parameter by value and reference.


## How to run
This tutorial is tested using python 3.6

```Shell
  git clone https://github.com/ahmdtaha/pyrex_wrapper.git
  cd pyrex_wrapper/
  python setup.py build_ext -i
  python pymain.py    # -viz option to visualize output
```


## Python Rex Wrapper Steps 
To create your own, here are the main steps

* Add the c function definition and implementation to a .h and .cpp file respectively-- similar to msrc.h, msrc.cpp
* Define python pyrex wrapper for the c functions in pyrex file (.pyx) -- similar to pyxtutorial.pyx. Pyrex is simply best described as "python with C data types". More information available in [wiki](https://wiki.python.org/moin/Pyrex) and [readthedocs.io](http://intermediate-and-advanced-software-carpentry.readthedocs.io/en/latest/c++-wrapping.html)
* Create setup.py to build the C++ code, generate the C++ shared library.