#!/usr/bin/python3

from typing import Callable, Optional, Union, Any
from sys import stderr

FuncRetType = Optional[Union[int, float]]
FuncType = Callable[[Any], FuncRetType]


def safe_function(fct: FuncType, *args: int) -> FuncRetType:
    """A function that executes a function safely

    TypeAlias:
        FuncRetType: Optional[Union[int, float]]
        FuncType: Callable[[Any], FuncRetType]

    Args:
        fct (FuncType): The function to be executed to get the
            return value to be returned

    Returns:
        FuncRetType: The return value from the given function object
    """
    try:
        return fct(*args)
    except Exception as error:
        print("Exception: {}".format(error), file=stderr)
        return None
