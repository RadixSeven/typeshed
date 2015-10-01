"""Stubs for the 'unicodedata' module."""

from typing import Any, TypeVar, Union, Optional

ucd_3_2_0 = ... # type: UCD
unidata_version = ... # type: str
# PyCapsule
ucnhash_CAPI = ... # type: Any

_default = TypeVar("_default")

def bidirectional(unichr: unicode) -> str: ...
def category(unichr: unicode) -> str: ...
def combining(unichr: unicode) -> int: ...
def decimal(chr: unicode, default=_default) -> Union[int, _default]: ...
def decomposition(unichr: unicode) -> str: ...
def digit(chr: unicode, default=_default) -> Union[int, _default]: ...
def east_asian_width(unichr: unicode): str
def lookup(name: str): unicode
def mirrored(unichr: unicode): int
def name(chr: unicode, default=_default) -> Union[str, _default]: ...
def normalize(form: str, unistr: unicode) -> unicode: ...
def numeric(chr, default=_default) -> Union[float, _default]: ...

class UCD(object):
    unidata_version = ... # type: str
    # The methods below are constructed from the same array in C
    # (unicodedata_functions) and hence identical to the methods above.
    def bidirectional(unichr: unicode) -> str: ...
    def category(unichr: unicode) -> str: ...
    def combining(unichr: unicode) -> int: ...
    def decimal(chr: unicode, default=_default) -> Union[int, _default]: ...
    def decomposition(unichr: unicode) -> str: ...
    def digit(chr: unicode, default=_default) -> Union[int, _default]: ...
    def east_asian_width(unichr: unicode): str
    def lookup(name: str): unicode
    def mirrored(unichr: unicode): int
    def name(chr: unicode, default=_default) -> Union[str, _default]: ...
    def normalize(form: str, unistr: unicode) -> unicode: ...
    def numeric(chr, default=_default) -> Union[float, _default]: ...