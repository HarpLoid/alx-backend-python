#!/usr/bin/env python3
"""
Module Docs
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ func docs """
    delay_list = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*delay_list)
    return sorted(delays)
