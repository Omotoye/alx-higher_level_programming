#!/usr/bin/python3
from sys import argv


def main() -> None:
    """Program to print formatted command line arguments"""
    argc: int = len(argv) - 1
    print("{} argument{}".format(argc, ("" if argc == 1 else "s")), end="")
    print("{}".format(":" if argc > 0 else "."))
    for index, arg in enumerate(argv[1:]):
        print("{}: {}".format(index + 1, arg))


if __name__ == "__main__":
    main()
