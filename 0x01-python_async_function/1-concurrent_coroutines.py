#!/usr/bin/env python3
"""1. Let's execute multiple coroutines at the same time with async"""


import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ calling wait_random n times

        Args:
            n: int - the number of times n called
            max_delay: int - the delay time
        Returns:
            the list of all delays
    """

    returned_time = []

    for i in range(0, n):
        returned_time.append(await wait_random(max_delay))
    return sorted(returned_time)
