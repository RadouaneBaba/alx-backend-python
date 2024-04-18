#!/usr/bin/python3
""" annotate a function """
from typing import Sequence, Iterable, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ element_length annotation """
    return [(i, len(i)) for i in lst]
