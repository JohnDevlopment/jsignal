from __future__ import annotations
from typing import Protocol, Any, cast, overload

class _signal_function(Protocol):
    def __call__(self, *args: Any, **kw: Any) -> None:
        ...
