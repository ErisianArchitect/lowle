import sys
import inspect

def currentmodule():
    frame = inspect.currentframe().f_back
    name = frame.f_globals.get('__name__', None)
    return sys.modules.get(name, None)