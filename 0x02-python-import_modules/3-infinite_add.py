#!/usr/bin/python3
from sys import argv


def main() -> None:
    sum: int = 0
    for num in argv[1:]:
        sum += int(num)
    print(sum)


if __name__ == "__main__":
    main()
