#!/usr/bin/env python3
"""Implement a coroutine that measures the total runtime"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Coroutine that measures the total runtime"""
    start = time.time()
    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
            )
    
    end = time.time()
    return end - start
