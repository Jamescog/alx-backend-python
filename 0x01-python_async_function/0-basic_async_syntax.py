#!/usr/bin/env python3
"""0. The basics of async"""


import random
import asyncio


async def wait_random(max_delay=10):
    """ asynchronous coroutine that takes an integer argument
        and waits for for a randm delay  between 0 and max-delay

        Args:
            max_delay -  the time it waits
        Returns:
            The the delay time
    """

    t = random.uniform(0, max_delay)
    await asyncio.sleep(t)
    return t
