from __future__ import annotations

# Make it so that ic() calls never raise an exception
try:
    import icecream
    icecream.install()
except ImportError:
    def ic(*args, **kw):
        pass

    import builtins
    setattr(builtins, "ic", ic)

__version__ = "1.0.0"
