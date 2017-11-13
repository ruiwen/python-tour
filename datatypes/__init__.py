from sys import version_info

__all__ = [
      #   'integers', 'integers_py2',
      #   'strings', 'strings_py2',
      #   'lists',
      #   'dicts',
      #   'sets',
      #   'generators', 'generators_py2'
    ]

if version_info.major == 3:
    from . import integers, strings, generators
else:
    from . import integers_py2 as integers
    from . import strings_py2 as strings
    from . import generators_py2 as generators

from . import lists, dicts, sets


