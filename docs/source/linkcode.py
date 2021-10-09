#!/usr/bin/env python3

# https://github.com/Lasagne/Lasagne/blob/master/docs/conf.py

import inspect
import os
import sys

from types import ModuleType


def linkcode_helper(domain, info,
                    package: ModuleType,
                    github_user: str,
                    github_repo: str = None,
                    tag: str = 'master'):
    # Resolve function for the linkcode extension.
    if domain != 'py' or not info['module']:
        return None
    github_repo = github_repo or package.__name__
    # try to find the file and line number, based on code from numpy:
    # https://github.com/numpy/numpy/blob/master/doc/source/conf.py#L286
    obj = sys.modules[info['module']]
    for part in info['fullname'].split('.'):
        obj = getattr(obj, part)
    fn = inspect.getsourcefile(obj)
    fn = os.path.relpath(fn, start=os.path.dirname(
        os.path.dirname(package.__file__)))
    try:
        source, lineno = inspect.getsourcelines(obj)
        fn += f'#L{lineno}-L{lineno + len(source) - 1}'
    except Exception as e:
        pass
    return f'https://github.com/{github_user}/{github_repo}/blob/{tag}/{fn}'
