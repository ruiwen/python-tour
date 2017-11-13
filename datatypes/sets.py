
## Sets
# Good for efficiently testing membership/identifying common members
# Order is not guaranteed

# Set definition looks very similar to dict definition,
# exception that sets contain just a list of items, not a
# bunch of key-value pairs

ip_set = {
        "204.116.215.149",
        "216.171.221.207",
        "165.225.106.69",
        "187.189.71.144",
        "172.56.23.23",
        "72.193.140.203",
        "173.244.48.169",
        "71.15.113.163",
        "169.50.62.69",
        "37.221.161.243",
        "170.250.140.52",
        "50.248.94.189",
        "172.58.12.235",
        "121.69.48.132",
        "78.189.85.174",
        "110.84.221.234",
        "123.160.132.65",
        "185.172.110.221"
    }

# IPs whose first octet is under 125
low_set = {
        "72.193.140.203",
        "71.15.113.163",
        "37.221.161.243",
        "50.248.94.189",
        "121.69.48.132",
        "78.189.85.174",
        "110.84.221.234",
        "123.160.132.65",
    }

# IPs whose first octet is 125 and above
high_set = {
        "204.116.215.149",
        "216.171.221.207",
        "165.225.106.69",
        "187.189.71.144",
        "172.56.23.23",
        "173.244.48.169",
        "169.50.62.69",
        "170.250.140.52",
        "172.58.12.235",
        "185.172.110.221"
    }

def set_membership(s, item):
    return item in s

def set_difference(s, q):
    """
    Return non-overlapping elements
    Returns items in s that are _not_ in q
    To find items in one list that _don't belong_ in another list,
    construct two equivalent sets, then find their difference
    This trades memory/space for speed
    Note that this difference is only relative to the first set, ie. s,
    and will only show _items in s that are not in q_
    See set_symmetric_difference() to identify elements that are not in
    _both sets_ at once
    """
    return s - q

def set_intersect(s, q):
    """
    Return overlapping elements
    Returns items in s that are _in_ q
    So to find common items in two lists, construct to equivalent sets,
    then find the intersection, instead of doing nested for loops
    This trades memory/space for speed
    """
    return s & q

def set_symmetric_difference(s, q):
    """
    Returns _mutually non-overlapping_ elements
    Returns elements that do not appear in _both_ sets
    """
    return s.symmetric_difference(q)

