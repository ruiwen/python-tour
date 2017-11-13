## Dicts

# Dictionaries are also known as hashes, hashmaps, or just generally maps.
# They map one value (the key) to another (the value).


a_dict = {"first": "hello", 2: "world", 3.0: "there"}

### Accessing values

def dict_items(d):
    print("Original dict: {}".format(d))
    values = {
        "label": "dict keys",
        "keys": str(d.keys()),
        "type": str(type(d.keys()))
    }
    print("{label:>15}: {keys:<50}, type: {type:<20}".format(**values))
    values = {
        "label": "dict values",
        "values": str(d.values()),
        "type": str(type(d.values()))
    }
    print("{label:>15}: {values:<50}, type: {type:<20}".format(**values))

    print("\n")
    for k, v in d.items():
        print("Key: {key:>10} | Value: {value:>8} | KeyType: {ktype:>15} | ValueType: {vtype:>10}".format(key=k, value=v, ktype=str(type(k)), vtype=str(type(v))))

### Dict Order
# Run this separately under Python 3.6, 3.5 and 2.7
# Python 3.6 should preserve = {1, 298, 278, 18} insertion order when iterated over
# However, this order-preservation in CPython 3.6 is an implementation detail
# and is not part of the language spec as yet.

def dict_order():

    d = {}
    d['one'] = 1
    d['two'] = 2
    d['three'] = 3
    print("dict items: %s" % str(d.items()))

    for k, v in d.items():
        print("key: %s, value: %s" % (k, v))

### Membership in Dicts
def dict_membership(d, key):
    return key in d

### Dict comprehensions

# Similar to list comprehensions, dictionaries in Python can similarly
# be created via a comprehension.

def dict_comprehensions(s, d, skip=None):
    """
    Given a prefix, s, and a dictionary, d,
    prefixes all keys in d with prefix s_,
    and returns a new dict

    If the set 'skip' is provided, skips appending
    the prefix to any key present in set 'skip'
    """

    # We set the default value of 'skip' to None
    # If 'skip' has been set (ie. is not a False-y) value, we use it,
    # otherwise, we set 'skip' to the empty set
    skip = skip or set()

    # This line also uses Python's pseudo-ternary form
    return {k if k in skip else "%s_%s" % (s, k): v for k, v in d.items()}

