#!/usr/bin/env python3

# https://github.com/Lasagne/Lasagne/blob/master/docs/conf.py

import inspect
import sys
from os import path

from types import ModuleType


def linkcode_helper(domain, info,
                    package: ModuleType,
                    github_url: str,
                    tag: str = 'master'):
    # Resolve function for the linkcode extension.
    if domain != 'py' or not info['module']:
        return None
    # try to find the file and line number, based on code from numpy:
    # https://github.com/numpy/numpy/blob/master/doc/source/conf.py#L286
    github_url = github_url.removesuffix('/')
    obj = sys.modules[info['module']]
    for part in info['fullname'].split('.'):
        try:
            obj = getattr(obj, part)
        except Exception:
            return None
    try:
        fn = inspect.getsourcefile(obj)
    except Exception:
        fn = None
    if not fn:
        return None
    fn = path.relpath(fn, start=path.dirname(
        path.dirname(package.__file__)))
    try:
        source, lineno = inspect.getsourcelines(obj)
        fn += f'#L{lineno}-L{lineno + len(source) - 1}'
    except Exception:
        pass
    return f'{github_url}/blob/{tag}/{fn}'
