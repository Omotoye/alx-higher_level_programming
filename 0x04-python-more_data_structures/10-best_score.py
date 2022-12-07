#!/usr/bin/python3

from typing import Optional


def best_score(a_dict):
    """A function that returns a key with the biggest integer value.

    Args:
        a_dict (Optional[dict[str, int]]): The dictonary to operate on
            or None

    Returns:
        Optional[str]: the key to the maximum value in the dictionary
            or None
    """
    return max(a_dict.items(), key=lambda x: x[1])[0] if a_dict else None
