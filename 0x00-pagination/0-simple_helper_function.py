#!/usr/bin/env python3
"""
Defines a function named `index_range`
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple containing a start index and an end index
    corresponding to the range of indexes to return in a list for
    the provided pagination parameters.
    
    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple of (start index, end index).
    """

    start_index = (page - 1) * page_size
    end_index = page * end_index

    return start_index, end_index
