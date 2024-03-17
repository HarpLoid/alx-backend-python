#!/usr/bin/env python3
"""
Module 8-make_multiplier

A type-annotated function make_multiplier
that takes a float multiplier as argument
and returns a function that multiplies
a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """takes a float multiplier as argument
    and returns a function that multiplies
    a float by multiplier

    Args:
        multiplier (float): multiplier

    Returns:
        Callable[[float], float]: callable
    """
    def mult(m: float) -> float:
        """multiplier callable

        Args:
            m (float): multiplier

        Returns:
            float: _description_
        """
        return m * multiplier

    return mult
