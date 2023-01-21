# Utility Translators for various types of common or obscure lingo

from .db_helpers import LEET_CHAR, CHAR_TO_NUMBER, UPSIDE_DOWN, MIRROR

def phone2numeric(text: str) -> str:
    """
    Convert a phone number with letters into its numeric equivalent.

    >>> phone2numeric('1-800-GOT-JUNK')
    '1-800-468-5865'
    """

    return "".join(CHAR_TO_NUMBER.get(c, c) for c in text.lower())

def leet(text: str) -> str:
    """
    Returns the 1337 version of the text.

    >>> leet('Grass is Green')
    '9®@$$ !$ 9®33и'
    """

    return "".join(LEET_CHAR.get(c, c) for c in text.lower())

def upside_down(text: str) -> str:
    """
    Returns the upside down version of the text.
    
    >>> upside_down('Grass is green')
    'uǝǝɹƃ sᴉ ssɐɹ⅁'
    """

    return ''.join(reversed([UPSIDE_DOWN.get(c, c) for c in text]))

def mirror(text: str) -> str:
    """
    Returns the mirror version of the text.
    
    >>> mirror('Grass is green')
    'nɘɘาϱ ƨ𝗂 ƨƨ𐑇าᘐ'
    """

    return ''.join(reversed([MIRROR.get(c, c) for c in text]))

