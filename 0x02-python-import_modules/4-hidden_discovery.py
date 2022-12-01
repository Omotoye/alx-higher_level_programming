#!/usr/bin/python3
import hidden_4 as h4


def main() -> None:
    mods: list[str] = dir(h4)
    mod_list: list[str] = [mod for mod in mods if "__" not in mod]
    for mod in mod_list:
        print(mod)


if __name__ == "__main__":
    main()
