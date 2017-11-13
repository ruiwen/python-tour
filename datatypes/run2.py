
if __name__ == "__main__":
    from sys import argv, version_info

    # Running Python 2
    name = argv[0]
    mod_name = argv[1]
    fn_name = argv[2]
    args = argv[3:]

    import importlib

    pkg = importlib.import_module('datatypes')
    mod = getattr(pkg, mod_name)
    fn = getattr(mod, fn_name)
    fn(*args)
