#!/usr/bin/env python3
"""to_kv: that converts a string and an int or float to a tuple"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple"""
    return (k, v ** 2)


if __name__ == "__main__":
    to_kv = __import__('7-to_kv').to_kv

    print(to_kv.__annotations__)
    print(to_kv("eggs", 3))
    print(to_kv("school", 0.02))
