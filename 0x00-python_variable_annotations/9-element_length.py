#!/usr/bin/env python3
"""
Module Docs
"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """function doc

    Args:
        lst (Iterable[Sequence]): _description_

    Returns:
        List[Tuple[Sequence, int]]: _description_
    """
    return [(i, len(i)) for i in lst]
