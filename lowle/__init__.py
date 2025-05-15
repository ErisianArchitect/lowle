from types import ModuleType

import os
import sys
import inspect
import importlib
from importlib.util import spec_from_file_location, module_from_spec

from pathlib import Path

class insert_into:
    def __init__(self, mapping: dict, key):
        self.mapping = mapping
        self.key = key

    def __call__(self, target):
        self.mapping[self.key] = target
        return target

def _resolve_path(path: str | os.PathLike)->Path:
    if isinstance(path, Path):
        return path
    else:
        return Path(path)

def current_module():
    frame = inspect.currentframe().f_back
    name = frame.f_globals.get('__name__', None)
    return sys.modules.get(name, None)

def parent_frame():
    return inspect.currentframe().f_back.f_back

def imp(path: Path, add_to_sys_modules: bool = False)->ModuleType:
    """Shorthand for `import`. This will import a module from a path."""
    path = _resolve_path(path)
    spec = spec_from_file_location(path.name, path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    if add_to_sys_modules:
        sys.modules[path.name] = module
    return module

def this_module_directory()->Path:
    frame = inspect.currentframe().f_back
    file_name = frame.f_globals.get('__file__')
    file_path = Path(file_name)
    return file_path.parent