#!/usr/bin/env python3
"""safe_first_elemenet"""
from typing import List, Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """duck typings

    Args:
        lst (Sequence[Any]): sequence of any values

    Returns:
        Any: any value
    """
    if lst:
        return lst[0]
    else:
        return None
