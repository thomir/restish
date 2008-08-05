"""
General-purpose utilities.
"""

from webhelpers.html import literal


class RequestBoundCallable(object):
    """
    Bind a request to something callable.

    The callable will be called with request as the 1st positional argument.
    Any additional args (positional or keyword) will be passed as-is.
    """

    def __init__(self, callable, request):
        self.callable = callable
        self.request = request

    def __call__(self, *a, **k):
        return literal(self.callable(self.request, *a, **k))
