from .types import ModuleAware
from .public import public
from .private import private


__version__ = '2.0'


def install():
    """Install @public and @private into builtins."""
    import builtins
    builtins.public = public
    builtins.private = private


public(
    ModuleAware=ModuleAware,
    public=public,
    private=private,
    )
