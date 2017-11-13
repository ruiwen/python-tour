
# Enable sane integer division for Python2
# from __future__ import division

# In Python 3, integer division works as expected, ie.
# results are automatically translated into a float,
# leading to fewer surprises.
#
# In Python 2, integer division works like it would in
# C, where the fractional part is truncated if the inputs
# were not explicitly cast into floats beforehand
#
# Alternatively, the __future_ compatibility module
# exists to backport useful features back into the Python 2
# tree to allow developers who can't move off Python 2 to
# make use of more modern features

def int_division(a, b):
    return a/b

def int_division_cast(a, b):
    return float(a) / float(b)
