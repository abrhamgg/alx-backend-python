#!/usr/bin/env python3
"""duck type"""
from typing import Iterable, Union, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """element length

    Args:
        lst (Iterable[Union[int, float, str, list]]): iterable item

    Returns:
        List[int]: return list of elements in the list
    """
    return [(i, len(i)) for i in lst]
