#!/usr/bin/env python3
""" function returns a tuple """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ return tuple of different types """
    return (k, float(v * v))
