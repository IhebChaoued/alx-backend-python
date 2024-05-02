#!/usr/bin/env python3
"""safe_first_element: Safely retrieve the first element from a sequence"""

import typing


def safe_first_element(lst: Sequence) -> Union[Any, None]:
    """Returns the first element of 'lst' or None if 'lst' is empty."""
    if lst:
        return lst[0]
    else:
        return None
