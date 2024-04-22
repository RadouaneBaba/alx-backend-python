#!/usr/bin/env python3
""" task_wait_n implementation """
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ return array of n times wait_random """
    delays = []
    tasks = [task_wait_random(max_delay) for i in range(n)]
    for task in asyncio.as_completed(tasks):
        elem = await task
        delays.append(elem)
    return delays
