#!/usr/bin/env python3
"""sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum_mixed_list -> which takes a list mxd_lst of integers and floats and
    returns their sum as a float.

    Args:
        mxd_lst (List[int, float]): mixed list of str and float

    Returns:
        float: sum of numbers in the list as  float
    """
    total: float = 0
    for i in mxd_lst:
        total += i
    return total
