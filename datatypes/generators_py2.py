## Generators

# Using generators in Python is good way to save memory
# when iterating over potentially unbounded lists of items.
# Generators (as their name suggests) produce the values in their
# range one at a time, while also not holding on to values produced
# earlier. For example, when iterating integers from 1 to 1000000000,
# a generator will yield only 1 integer at a time, which doesn't
# put very much strain on the system.
# Conversely, a defining list of integers from 1 to 1000000000
# (eg. l = range(1, 1000000001)), will actually cause the system
# allocate memory for 1 billion integers, which may be problematic.
#
# When processing a very large file for example, we might not necessarily
# want to read the entire file into memory before processing, since
# a logfile may take up significant memory space, and starve our other processes.
# What we can do in this case is to wrap reading the file in a generator
# then request the content of the file in chunks of, say, 1024 bytes.
# For examples of the above, see https://stackoverflow.com/a/519653
#
# The example below shows the amount of memory (in bytes) required
# by the generator returned from large_dict.iteritems() vs the list retuned
# by large_dict.items(). The generator should be fairly lightweight
# as compared to the list.

### Difference in memory space between dict.iteritems() (generator) vs dict.items() (list) in Python2

def gen_sizeof():
    import sys
    large_dict = {str(idx): i for idx, i in enumerate(range(0, 200))}
    print("Original dict: %s" % large_dict)

    print("\n")
    # Get an list with items()
    items = large_dict.items()
    print("Using dict.items() producing a list")
    print("{label:>20}: {value:<20}".format(label="Type of items", value=str(type(items))))
    print("{label:>20}: {value:<20}".format(label="Number of items", value=str(len(items))))
    print("{label:>20}: {value:<20} bytes".format(label="Memory size of items", value=str(sys.getsizeof(items))))

    print("\n")

    # Get generator with iteritems()
    items = large_dict.iteritems()
    print("Using dict.iteritems() producing a generator")
    print("{label:>20}: {value:<20}".format(label="Type of items", value=str(type(items))))
    print("{label:>20}: {value:<20} bytes".format(label="Memory size of items", value=str(sys.getsizeof(items))))

