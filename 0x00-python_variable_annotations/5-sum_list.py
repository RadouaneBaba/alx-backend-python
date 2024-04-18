#!/usr/bin/env python3
""" type annotated sum_list return sum of floatslist """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ returns sum of floats """
    return sum(input_list)
