#!/usr/bin/env python3
"""Calculate execution time"""


import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def calculate_execution_time(n: int, max_delay: int) -> float:
    """ Calculate the run time of wait_random
        Args:
            n (int): The number of times wait_random will be called
            max_delay (int): The maximum delay
        Returns:
            float: Average run time per call to wait_random
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start) / n
