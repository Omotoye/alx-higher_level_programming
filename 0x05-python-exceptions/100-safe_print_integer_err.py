#!/usr/bin/python3

from typing import Any
from sys import stderr


def safe_print_integer_err(value: Any) -> bool:
    try:
        print("{:d}".format(value))
        return True
    except Exception as error:
        print("Exception: {}".format(error), file=stderr)
        return False
