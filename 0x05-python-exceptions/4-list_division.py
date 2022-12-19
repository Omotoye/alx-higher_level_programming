#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length: int):
    """A function that divides element by element 2 lists

    Args:
        my_list_1 (List[Any]): the first list
        my_list_2 (List[Any]): the second list
        list_length (int): the length of the new list to be returned

    Returns:
        List[Union[float, int]]: new list which length is the given
            `list_length`, with all divisions between elements of the two list.
            if the division of any of the elements of the two given list is not
            successful, the appended item to the new list is 0
    """
    new_list = []

    for index in range(list_length):
        try:
            new_list.append(my_list_1[index] / my_list_2[index])
        except (TypeError, ValueError):
            print("wrong type")
            new_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
    return new_list
