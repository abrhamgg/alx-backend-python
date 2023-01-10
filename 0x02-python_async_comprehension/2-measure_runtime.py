#!/usr/bin/env python3
"""
will execute async_comprehension four times in parallel using asyncio.gather.
measure the total runtime and return it.
"""
import asyncio
from time import perf_counter
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Measure the run time of four gathered asyncio """
    start = perf_counter()
    tasks = [asyncio.create_task(async_comprehension()) for _ in range(4)]
    await asyncio.gather(*tasks)
    end = perf_counter()
    return end - start
