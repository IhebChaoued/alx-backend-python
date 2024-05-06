#!/usr/bin/env python3
"""Measure Runtime module"""

import time
from typing import Callable
from typing import List
from asyncio import run
from .1-concurrent_coroutines import wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time for wait_n"""
    start_time = time.time()
    
    delays: List[float] = run(wait_n(n, max_delay))
    
    end_time = time.time()
    total_time = end_time - start_time
    
    average_time = total_time / n
    
    return average_time


if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay)))
