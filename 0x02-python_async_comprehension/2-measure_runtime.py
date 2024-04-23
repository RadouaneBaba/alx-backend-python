#!/usr/bin/env python3
""" measure_runtime implementation """
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ execute async_comprehension four times in parallel """
    start_time = time.time()
    tasks = [async_comprehension() for i in range(4)]
    await asyncio.gather(*tasks)
    elapsed_time = time.time() - start_time
    return elapsed_time
