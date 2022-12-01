#!/usr/bin/python3
from sys import argv, exit
from typing import Callable, Final
from calculator_1 import add, sub, mul, div

Operation = dict[str, Callable[[int, int], int]]
operations: Final[Operation] = {"+": add, "-": sub, "*": mul, "/": div}


def main() -> None:
    argc: int = len(argv) - 1

    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operator: str = argv[2]
    if operator not in operations.keys():
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a: int = int(argv[1])
    b: int = int(argv[3])
    result: int = operations[operator](a, b)

    print("{} {} {} = {}".format(a, operator, b, result))


if __name__ == "__main__":
    main()
