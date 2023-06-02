from contextlib import contextmanager
import secrets
import inspect
from functools import wraps

from api.injectable import Realm

# modified from https://stackoverflow.com/a/60638430/4729528
# wrap the function to add the realm parameter
# this in turn will make Sanic inject the realm and authenticate the user
def authenticated(func):
    # new parameter name is realm or realm_[_...] if realm if already present
    name = "realm"
    while name in func.__annotations__:
        name += '_'

    @wraps(func)
    async def wrapped_function(self, *args, **kwargs):
        if name in kwargs:
            del kwargs[name]
    
        retval = func(self, *args, **kwargs)
        if inspect.isawaitable(retval):
            retval = await retval
        return retval

    wrapped_function.__annotations__[name] = Realm
    return wrapped_function
