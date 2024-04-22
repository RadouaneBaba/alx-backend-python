""" wait_n function impelelmentation  """
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ return array of n times wait_random """
    delays = []
    tasks = [wait_random(max_delay) for i in range(n)]
    for task in asyncio.as_completed(tasks):
        elem = await task
        delays.append(elem)
    return delays
