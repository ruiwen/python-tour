# Required for using unicode literals in Python2 code
# -*- coding: utf-8 -*-

## Strings

# One of the biggest differences between Python 2 and Python 3
# is with how strings are handled. In Python 2, string objects
# could contain normal ASCII characters or unicode characters,
# it just depended on whether the developer chose to interpret
# them as unicode or plain bytes. This was confusing as data streams
# could also be byte-strings, so dealing with data vs text data
# could be messy.
#
# In Python 3, strings are unicode only, which makes it clear
# when you're dealing with text data (in whichever unicode characterset),
# and further removing the need for explicit handling of unicode strings.
# In Python 3, byte arrays are reserved for dealing with data streams.
#
# In Python 2, developers had to keep in mind if they wanted to
# interpret the data as unicode, or keep in mind if they wanted
# to output a unicode string.
#
# The examples below show the differences between how regular
# strings are handled in Python 2 vs unicode strings (note the .decode() calls,
# and the 'u' prefixes, as well as the 'coding' line at the top of the file)
# Pass a_string and b_string into the functions to see how they react.

a_string = "hello world"
b_string = "世界您好"  # This is a unicode literal

def string_iterate(s):
    """Iterates characters in a given string, s"""
    for idx, i in enumerate(s.decode('utf-8')):
        # print("num: %s" % i)
        # print("num: {number}".format(number=i))
        print(u"num[{index:d}]: {number}".format(number=i, index=idx))

def string_count_characters(s):
    print(u"{label:>20}: {string}".format(label="Original string", string=s.decode('utf-8')))
    print(u"{label:>20}: {length}".format(label="Length (ascii bytes)", length=str(len(s))))
    print(u"{label:>20}: {length}".format(label="Length (unicode)", length=str(len(s.decode('utf-8')))))

### Slicing

def print_slices(s):
    print("Original string: {}".format(s.decode('utf-8')))
    print("Last item: {}".format(s.decode('utf-8')[-1]))
    print("Third last item: {}".format(s.decode('utf-8')[-3]))
    print("Last 3 items: {}".format(s.decode('utf-8')[-3:]))
    print("Exclude last 3 items: {}".format(s.decode('utf-8')[:-3]))
    print("Every other character: {}".format(s.decode('utf-8')[::2]))

