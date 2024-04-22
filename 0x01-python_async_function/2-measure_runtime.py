#!/usr/bin/env python3
""" measure_time implementation """
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, delay_max: int) -> float:
    """ execution time of wait_n """
    start_time = time.time()
    asyncio.run(wait_n(n, delay_max))
    exec_time = time.time() - start_time
    return exec_time
