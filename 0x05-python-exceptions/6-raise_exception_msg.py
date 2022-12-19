#!/usr/bin/python3


def raise_exception_msg(message: str = "") -> None:
    """A function that raises a name exception with a message

    Args:
        message (str, optional): The message to raise the
            exception with. Defaults to "".

    Raises:
        NameError: the exception to be raised
    """
    raise NameError(message)
