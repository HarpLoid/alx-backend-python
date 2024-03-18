#!/usr/bin/env python3
"""
Module Docs
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between
    0 and max_delay (included and float value) seconds

    Args:
        max_delay (int, optional): maximun delay. Defaults to 10.

    Returns:
        float: actual random delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
