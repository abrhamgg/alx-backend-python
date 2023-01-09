#!/usr/bin/env python3
"""async - coroutine"""
import random
import asyncio


async def wait_random(*argv) -> float:
    """wait_random - asynchronous coroutine that takes in an integer
    argument (max_delay, with a default value of 10) named wait_random
    that waits for a random delay between 0 and max_delay (included and
    float value) seconds and eventually returns it.

    Args:
        max_delay (int): input value

    Returns:
        float: _description_
    """
    if not argv:
        r = random.uniform(0, 10)
    else:
        r = random.uniform(0, argv[0])
    await asyncio.sleep(r)
    return r
