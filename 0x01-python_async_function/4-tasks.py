#!/usr/bin/env python3
"""
Module Docs
"""
import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """func docs"""
    list_delays = []
    for _ in range(n):
        list_delays.append(task_wait_random(max_delay))
    return sorted(await asyncio.gather(*list_delays))
