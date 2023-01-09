#!/usr/bin/env python3
"""takes an integer max_delay
and returns a asyncio.Task
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ Take the integer on max delay and return the task """
    task = asyncio.create_task(wait_random(max_delay))
    return task
