#!/usr/bin/env python3
"""
Module 5-sum_list

A type-annotated function sum_list which takes
a list input_list of floats as argument
and returns their sum as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sums all float values in
    the list

    Args:
        input_list (list)

    Returns:
        float
    """
    sum: float = 0.0
    for _ in input_list:
        sum += _
    return sum
