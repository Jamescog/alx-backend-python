#!/usr/bin/env python3
"""Complex types -mixed list"""


from typing import Union


def sum_mixed_list(mxd_lst: list[Union[int, float]]) -> float:
    """ type annotated function that takes a list of integers
        and floats and returns their sums as float

        Args:
            mxd_lst: Unioun[int, float] - the list of num
        Returns:
            the sum of the nums as float
    """

    return float(sum(mxd_lst))
