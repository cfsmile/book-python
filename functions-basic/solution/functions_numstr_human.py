from typing import Union

NUMBER_DICT = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '.': 'and',
}


def number_to_str(number: Union[int, float]) -> str:
    """
    >>> number_to_str(1969)
    'one thousand nine hundred sixty nine'

    >>> number_to_str(31337)
    'thirty one thousand three hundred thirty seven'

    >>> number_to_str(13.37)
    'thirteen and thirty seven hundredths'

    >>> number_to_str(31.337)
    'thirty one three hundreds thirty seven thousands'
    """
    pass
