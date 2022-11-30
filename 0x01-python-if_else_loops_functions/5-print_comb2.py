#!/usr/bin/python3

for i in range(100):
    print(
      "{}{}{}".format(0 if i < 10 else "", i, "," if i != 99 else ""), end=" "
    )
