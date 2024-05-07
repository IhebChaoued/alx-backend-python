#!/usr/bin/env python3
"""Implement a coroutine"""

from typing import List
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Coroutine that collects 10 random numbers"""
    return [i async for i in async_generator()][:10]
