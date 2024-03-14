#!/usr/bin/python3
"""
Module 6-sum_mixed_list

A type-annotated function sum_mixed_list which takes
a list mxd_lst of integers and floats
and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int,float]]) -> float:
    """Sums all float values in
    the list

    Args:
        input_list (list)

    Returns:
        float
    """
    sum: float = 0.0
    for _ in mxd_list:
        sum += _
    return sum
