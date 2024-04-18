#!/usr/bin/env python3
""" make_multiplier function """
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ returns a function that multiplies a float by multiplier """
    def low_multiplier(factor: float) -> float:
        """ multiply the previous num with a float """
        return multiplier * factor
    
    return low_multiplier
