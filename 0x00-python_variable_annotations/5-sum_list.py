#!/usr/bin/env python3
"""Complex types -list of floats"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """ type annotated function that takes a list of floats
        and returns theirs sums as a float

        Args:
            input_list: list - the input list
        Returns:
            the sum of the list as float
    """

    return float(sum(input_list))
