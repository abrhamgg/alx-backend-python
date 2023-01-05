#!/usr/bin/env python3
"""sum_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """sum_list -> which takes a list input_list of floats as
    argument and returns their sum as a float.

    Args:
        input_list (list): list of floats

    Returns:
        float: sum of the list as a float
    """
    total: float = 0
    for i in input_list:
        total += i
    return total
