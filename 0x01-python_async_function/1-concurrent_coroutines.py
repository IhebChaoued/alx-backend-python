#!/usr/bin/env python3
"""Concurrent Coroutines"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Executes wait_random n times with the specified max_delay"""
    times = []

    for _ in range(n):
        times.append(wait_random(max_delay))

    randoDelay = await asyncio.gather(*times)
    return sorted(randoDelay)
