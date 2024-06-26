#!/usr/bin/env python3
""" measure_time implementation to measure runtime """
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ execution time of wait_n in float number """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    exec_time = time.time() - start_time
    return exec_time / n
