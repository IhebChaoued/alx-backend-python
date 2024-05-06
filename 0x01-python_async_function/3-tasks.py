#!/usr/bin/env python3
"""Tasks module"""

import asyncio
from typing import Callable
from asyncio import Task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """Creates and returns an asyncio"""
    task = asyncio.create_task(wait_random(max_delay))
    return task


if __name__ == "__main__":
    import asyncio

    async def test(max_delay: int) -> None:
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)

    asyncio.run(test(5))
