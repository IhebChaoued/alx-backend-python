#!/usr/bin/env python3
"""Implement a coroutine that measures the total runtime"""

import asyncio
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Coroutine that measures the total runtime"""
    start_time = asyncio.get_event_loop().time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = asyncio.get_event_loop().time()
    return end_time - start_time
