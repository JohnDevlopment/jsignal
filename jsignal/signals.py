"""Signals, objects which implement the command pattern."""

from __future__ import annotations
from ._types import _signal_function
from typing import Protocol, Any, cast, overload

class signal:
    """Implements the observer pattern."""

    __slots__ = ('name', '_observers', 'obj')

    def __init__(self, name, obj=None):
        """
        Construct a signal with the given name.
        """
        self.name = name
        self._observers = []
        self.obj = obj

        if obj is None:
            import inspect, sys

            # Get current frame
            frame = inspect.currentframe()
            if frame is None: return

            # Go up one level, to the function calling this one
            frame = frame.f_back
            if frame is None: return

            # Get the 'self' argument if present
            _locals = frame.f_locals
            obj = _locals.get('self')
            if obj is None:
                # Not present, use the module instead
                obj = sys.modules[frame.f_globals['__name__']]

            self.obj = obj

    def _form_signal_bind(self, fn, *args, **kw):
        return fn, args, kw

    @property
    def count(self):
        """Number of registered functions."""
        return len(self._observers)

    def connect(self, func, *binds, **kw):
        """Connect the signal."""
        if not callable(func):
            raise TypeError("First argument must be a function")

        bind = self._form_signal_bind(func, *binds, **kw)
        assert self._is_signal_bind(bind), "argument is not a signal binding"
        if bind in self._observers:
            # Error if duplicate binds
            raise ValueError("Already connected this signal to this function with the specified binds")

        self._observers.append(bind)

    def disconnect(self, func, *binds, **kw):
        """Disconnect the signal."""
        bind = self._form_signal_bind(func, *binds, **kw)
        assert self._is_signal_bind(bind), "argument is not a signal binding"
        self._observers.remove(bind)

    @staticmethod
    def _is_signal_bind(arg) -> bool:
        def _is_str_any_dict(arg):
            return map(lambda x: isinstance(str, x), arg.keys())

        match arg:
            case (fn, args, kw):
                return isinstance(arg, tuple) and \
                       isinstance(kw, dict) and \
                       all(_is_str_any_dict(kw))

        return False

    def emit(self, *args, **kw):
        """Emit the signal."""
        for obv in self._observers:
            assert self._is_signal_bind(obv), "argument is not a signal binding"

            # Is a signal bind (tuple with a function, *args, and **kw)
            fn, sargs, skw = obv
            args = args + sargs
            kw.update(skw)

            # Call function with appended arguments
            fn = cast(_signal_function, fn)
            fn(*args, **kw)

    def __str__(self) -> str:
        return self.name
