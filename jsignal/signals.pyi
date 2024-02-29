from ._types import _signal_function
from typing import Any

_SignalBinds = tuple[_signal_function, tuple[Any, ...], dict[str, Any]]

class signal:
    """Implements the observer pattern."""

    def __init__(self, name: str, obj: object=None): ...

    @property
    def count(self) -> int:
        ...

    @property
    def name(self) -> str:
        ...

    @property
    def obj(self) -> object:
        ...

    def connect(self, func: _signal_function, *binds: Any, **kw: Any) -> None:
        ...

    def disconnect(self, func: _signal_function, *binds: Any, **kw: Any) -> None:
        ...

    def emit(self, *args: Any, **kw: Any) -> None:
        ...

    def __str__(self) -> str:
        ...
