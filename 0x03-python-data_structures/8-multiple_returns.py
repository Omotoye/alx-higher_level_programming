#!/usr/bin/python3


def multiple_returns(sentence: str):
    """A function that returns a tuple with the length of the given
    string and the first character of the given string

    Args:
        sentence (str): the sentence given, from which the length and
            the first character would be taken

    Returns:
        tuple[int, Optional[str]]: the tuple of length of the given
            string and either first character of the string or None
            if string is empty.
    """
    return (len(sentence), None if len(sentence) == 0 else sentence[0])
