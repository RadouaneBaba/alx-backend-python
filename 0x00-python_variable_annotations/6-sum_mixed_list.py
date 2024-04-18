#!/usr/bin/env python3
""" type annotated sum_mixed_list return sum of numslist """
from typing import List, Union


def sum_mixed_list(input_list: List[Union[int, float]]) -> float:
    """ returns sum of floats """
    return sum(input_list)
