
# Lists and iterables
# Lists are like general arrays and can be iterated over like in a simple for-loop
# but Python implements duck-typing, ie. so long as the datatype exposes the right
# methods/interface, it'll work just the same as another datatype that exposes the
# same methods.
#
# Some of the datatypes that can be interated over: lists, dicts, sets, strings
#
# List comprehensions are compact ways to express operations in a loop, particularly
# when the desired output is a list itself.
#
# eg. instead of this
#
# # Create a new list from 0 to 200, with every element multiplied by 5
# new_list = []
# for i in range(0, 200):
#   new_list.append(i * 5)
#
# you can do
#
# new_list = [ 5 * i for i in range(0, 200) ]
#
# More reading: https://stackoverflow.com/a/30245465

num_list = list(range(0, 10))

def list_iterate(items):
    """
    Iterates and prints each item in a given list, items
    """

    for idx, i in enumerate(items):
        # print("num: %s" % i)
        # print("num: {number}".format(number=i))
        print("num[{index:d}]: {number:d}".format(number=i, index=idx))

def list_comprehension(n):
    """
    Given a multiplier, n, multiplies each item in
    the list given by range(0, 5), by n,
    return results as a list
    """
    return [n * i for i in range(0, 5)]
