#!/usr/bin/env python3
"""sum_mixed_list: sum up a mixed list of integers and floats"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of a mixed list of integers and floats."""
    return sum(mxd_lst)


if __name__ == "__main__":
    sum_mixed_list = __import__('6-sum_mixed_list').sum_mixed_list

    mixed = [5, 4, 3.14, 666, 0.99]
    ans = sum_mixed_list(mixed)
    print(ans == sum(mixed))
    print("sum_mixed_list(mixed) returns {} which is a {}".format(ans, type(ans)))
