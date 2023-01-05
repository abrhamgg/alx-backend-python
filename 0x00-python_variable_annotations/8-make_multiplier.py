#!/usr/bin/env python3
"""make-multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make_multiplier that takes a float multiplier as argument and
    returns a function that multiplies a float by multiplier

    Args:
        multiplier (float): number

    Returns:
        Callable[[float], float]: function which takes float as input and
        returns a float
    """
    return lambda x: x * multiplier
