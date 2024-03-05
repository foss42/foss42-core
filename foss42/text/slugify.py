import re
import unicodedata
import unidecode
from html.entities import name2codepoint
from typing import Optional
from typeguard import typechecked

CHAR_ENTITY_PATTERN = re.compile(r'&(%s);' % '|'.join(name2codepoint))
DECIMAL_PATTERN = re.compile(r'&#(\d+);')
HEX_PATTERN = re.compile(r'&#x([\da-fA-F]+);')
QUOTE_PATTERN = re.compile(r'[\']+')
DISALLOWED_CHARS_PATTERN = re.compile(r'[^-a-zA-Z0-9]+')
DISALLOWED_UNICODE_CHARS_PATTERN = re.compile(r'[\W_]+')
DUPLICATE_DASH_PATTERN = re.compile(r'-{2,}')
NUMBERS_PATTERN = re.compile(r'(?<=\d),(?=\d)')
DEFAULT_SEPARATOR = '-'


@typechecked
def slugify(text: str,
            separator: str = DEFAULT_SEPARATOR,
            regex_pattern: Optional[str] = None,
            replacements: Optional[list[tuple[str, str]]] = None) -> str:
    """
    Make a slug from the given text.

    >>> slugify(" aryan #$$ ")
    'aryan'

    >>> slugify("one kožušček")
    'one-kozuscek'

    >>> slugify("one TWO")
    'one-two'

    >>> slugify("Дrаft №2.txt")
    'draft-no-2-txt'

    >>> slugify("Я ♥ борщ")
    'ia-borshch'

    >>> slugify("ÜBER Über ")
    'uber-uber'

    >>> slugify("This is a test ---")
    'this-is-a-test'

    >>> slugify("影師嗎")
    'ying-shi-ma'

    >>> slugify("C'est déjà l'été.")
    'c-est-deja-l-ete'

    >>> slugify("Nín hǎo. Wǒ shì zhōng guó rén")
    'nin-hao-wo-shi-zhong-guo-ren'

    >>> slugify("Компьютер")
    'kompiuter'

    >>> slugify("jaja---lol-méméméoo--a")
    'jaja-lol-mememeoo-a'

    >>> slugify("10 | 20 %")
    '10-20'

    >>> slugify('i love 🦄')
    'i-love'
    """

    # user-specific replacements
    if replacements:
        for old, new in replacements:
            text = text.replace(old, new)

    # ensure text is unicode
    if not isinstance(text, str):
        text = str(text, 'utf-8', 'ignore')

    # replace quotes with dashes - pre-process
    text = QUOTE_PATTERN.sub(DEFAULT_SEPARATOR, text)

    # decode unicode
    text = unidecode.unidecode(text)

    # ensure text is still in unicode
    if not isinstance(text, str):
        text = str(text, 'utf-8', 'ignore')

    text = CHAR_ENTITY_PATTERN.sub(
        lambda m: chr(name2codepoint[m.group(1)]), text)

    # decimal character reference
    try:
        text = DECIMAL_PATTERN.sub(lambda m: chr(int(m.group(1))), text)
    except Exception:
        pass

    # hexadecimal character reference
    try:
        text = HEX_PATTERN.sub(lambda m: chr(int(m.group(1), 16)), text)
    except Exception:
        pass

    # translate
    text = unicodedata.normalize('NFKD', text)

    # make the text lowercase
    text = text.lower()

    # remove generated quotes -- post-process
    text = QUOTE_PATTERN.sub('', text)

    # cleanup numbers
    text = NUMBERS_PATTERN.sub('', text)

    # replace all other unwanted characters
    pattern = regex_pattern or DISALLOWED_CHARS_PATTERN

    text = re.sub(pattern, DEFAULT_SEPARATOR, text)

    # remove redundant
    text = DUPLICATE_DASH_PATTERN.sub(
        DEFAULT_SEPARATOR, text).strip(DEFAULT_SEPARATOR)

    # finalize user-specific replacements
    if replacements:
        for old, new in replacements:
            text = text.replace(old, new)

    if separator != DEFAULT_SEPARATOR:
        text = text.replace(DEFAULT_SEPARATOR, separator)

    return text
