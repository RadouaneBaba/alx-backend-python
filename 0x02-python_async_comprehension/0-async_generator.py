#!/usr/bin/env python3
""" async_generator implementation """
import asyncio
import random

async def async_generator():
    """ yield a random number """
    for i in range(10):
        await asyncio.sleep(1)
        yield(random.uniform(0, 10))
