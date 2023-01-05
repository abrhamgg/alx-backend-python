#!/usr/bin/env python3
"""7-to_kv"""
from typing import List, Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """to_kv that takes a string k and an int OR
    float v as arguments and returns a tuple.

    Args:
        k (str): str
        v (Union[int, float]): int or float

    Returns:
        tuple: _description_
    """
    return(k, float(v**2))
