#!/usr/bin/env python3
"""
Module 7-to_kv

A type-annotated function to_kv
that takes a string k and
an int OR float v as arguments
and returns a tuple.
The first element of the tuple is the string k.
The second element is the square of the int/float v
and should be annotated as a float.
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """that takes a string k and an int OR float v
    and returns a tuple

    Args:
        k (str): string
        v (typing.Union[int, float]): int or float

    Returns:
        typing.Tuple[str, float]: tuple of string and float
    """
    return (k, v ** 2)
