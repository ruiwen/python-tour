

if __name__ == "__main__":
    from sys import argv, version_info

    # Running Python 3
    name, mod_name, fn_name, *args = argv

    import importlib

    pkg = importlib.import_module('datatypes')
    mod = getattr(pkg, mod_name)
    fn = getattr(mod, fn_name)
    fn(*args)

