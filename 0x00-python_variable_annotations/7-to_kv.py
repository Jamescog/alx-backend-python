#!/usr/bin/env python3
"""  Complex types - string and int/float to tuple"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ type-annotated function that takes a string k and an int
        OR float v as arguments and returns a tuple

        Args:
            k: str - the string
            v: Union[int, float] - the number
        Return:
            the string and float of the square of the number
    """

    square = v * v

    return k, square
