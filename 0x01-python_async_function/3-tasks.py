#!/usr/bin/env python3
""" task_wait_random implementation """
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ return task class """
    return asyncio.Task(wait_random(max_delay))
