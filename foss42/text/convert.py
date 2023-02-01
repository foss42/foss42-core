import re
from enum import Enum
from typeguard import typechecked
import titlecase as tc
from .db_words import SMALL_TITLE

SMALL_WORD = "|".join(re.escape(s) for s in SMALL_TITLE)
tc.set_small_word_list(SMALL_WORD)

RE_CAMEL_CASE = re.compile(r"(((?<=[a-z])[A-Z])|([A-Z](?![A-Z]|$)))")

class CaseType(Enum):
    LOWER = 0
    UPPER = 1
    CAMEL = 2
    PASCAL = 3

@typechecked
def casefold(text: str) -> str:
    """
    Returns a lowercase version of the string that is 
    suitable for caseless comparisons.
    It is more aggressive as it converts Unicode characters into 
    corresponding lowercase versions.

    >>> casefold('Grass is green')
    'grass is green'

    >>> casefold('Graß is green')
    'grass is green'
    """

    return text.casefold()

@typechecked
def lower_case(text: str) -> str:
    """
    All cased characters are converted into lowercase.

    >>> lower_case('Grass is green')
    'grass is green'
    """

    return text.lower()

@typechecked
def upper_case(text: str) -> str:
    """
    All cased characters are converted into uppercase.

    >>> upper_case('Grass is green')
    'GRASS IS GREEN'
    """

    return text.upper()

@typechecked
def capital_case(text: str) -> str:
    """
    For each word in the string, the first character is uppercased 
    and the remaining characters are lowercased.

    >>> capital_case('grass is green')
    'Grass Is Green'

    >>> capital_case('from the highest heights to the lowest depths, in photographs')
    'From The Highest Heights To The Lowest Depths, In Photographs'

    >>> capital_case("'Ford v Ferrari' finishes first at the box office")
    "'Ford V Ferrari' Finishes First At The Box Office"
    """

    return text.title()

@typechecked
def title_case(text: str) -> str:
    """
    Formats text with a proper title case for article/publication headlines.
    The rules are based on style guides from APA, The Chicago Manual of Style, and other modern conventions.
    Also known as headline case.

    >>> title_case('grass is green')
    'Grass Is Green'

    >>> title_case('from the highest heights to the lowest depths, in photographs')
    'From the Highest Heights to the Lowest Depths, in Photographs'

    >>> title_case("'Ford vs. Ferrari' finishes first at the box office")
    "'Ford vs. Ferrari' Finishes First at the Box Office"

    >>> title_case("Apple deal with AT&T falls through")
    'Apple Deal With AT&T Falls Through'

    >>> title_case("RAM is not same as ROM")
    'RAM Is Not Same as ROM'
    """

    return tc.titlecase(text)

@typechecked
def sentence_case(text: str) -> str:
    """
    First character is capitalized and rest all characters are lowercased.
    Note: It doesn't capitalize names or places.

    >>> sentence_case('grass is green')
    'Grass is green'
    """

    return text.capitalize()

@typechecked
def swap_case(text: str) -> str:
    """
    Uppercase characters are converted into lowercase and 
    lowercase characters are converted into uppercase.
    Also known as toggle case.

    >>> swap_case('Grass is Green')
    'gRASS IS gREEN'
    """

    return text.swapcase()

@typechecked
def text_split(text: str, 
               type: CaseType = CaseType.LOWER) -> list[str]:
    """
    >>> text_split('Grass is Green')
    ['grass', 'is', 'green']

    >>> text_split('Grass is Green', type = CaseType.UPPER)
    ['GRASS', 'IS', 'GREEN']

    >>> text_split('Grass is Green', type = CaseType.CAMEL)
    ['grass', 'Is', 'Green']

    >>> text_split('Grass is Green', type = CaseType.PASCAL)
    ['Grass', 'Is', 'Green']
    """

    text = text.strip()
    match type:
        case CaseType.LOWER:
            words = text.lower().split()
        case CaseType.UPPER:
            words = text.upper().split()
        case CaseType.CAMEL:
            words = text.lower().split()
            words = [words[0], ] + [word.title() for word in words[1:]]
        case CaseType.PASCAL:
            words = text.title().split()
    return words

@typechecked
def flat_case(text: str) -> str:
    """
    Converts into flat case.

    >>> flat_case('Grass is Green')
    'grassisgreen'
    """

    return "".join(text_split(text))

@typechecked
def upper_flat_case(text: str) -> str:
    """
    Converts into upper flat case.

    >>> upper_flat_case('Grass is Green')
    'GRASSISGREEN'
    """

    return "".join(text_split(text, type=CaseType.UPPER))

@typechecked
def pascal_case(text: str) -> str:
    """
    Converts into pascal case.
    Also known as upper camel case, studly case.

    >>> pascal_case('Grass is Green')
    'GrassIsGreen'
    """

    return "".join(text_split(text, type=CaseType.PASCAL))

@typechecked
def camel_case(text: str) -> str:
    """
    Converts into camel case.
    Also known as dromedary case.

    >>> camel_case('Grass is Green')
    'grassIsGreen'
    """

    return "".join(text_split(text, type=CaseType.CAMEL))

@typechecked
def snake_case(text: str) -> str:
    """
    Converts into snake case.
    Also known as pothole case.

    >>> snake_case('Grass is Green')
    'grass_is_green'
    """

    return "_".join(text_split(text))

@typechecked
def constant_case(text: str) -> str:
    """
    Converts into constant case.
    Also known as macro case, screaming snake case.

    >>> constant_case('Grass is Green')
    'GRASS_IS_GREEN'
    """

    return "_".join(text_split(text, type=CaseType.UPPER))

@typechecked
def camel_snake_case(text: str) -> str:
    """
    Converts into camel snake case.

    >>> camel_snake_case('Grass is Green')
    'grass_Is_Green'
    """

    return "_".join(text_split(text, type=CaseType.CAMEL))

@typechecked
def pascal_snake_case(text: str) -> str:
    """
    Converts into pascal snake case.

    >>> pascal_snake_case('Grass is Green')
    'Grass_Is_Green'
    """

    return "_".join(text_split(text, type=CaseType.PASCAL))

@typechecked
def dot_case(text: str) -> str:
    """
    Converts into dot case.

    >>> dot_case('Grass is Green')
    'grass.is.green'
    """

    return ".".join(text_split(text))

@typechecked
def kebab_case(text: str) -> str:
    """
    Converts into kebab case.
    Also known as skewer case, spinal case, param case, dash case, LISP case.
    
    >>> kebab_case('Grass is Green')
    'grass-is-green'
    """

    return "-".join(text_split(text))

@typechecked
def cobol_case(text: str) -> str:
    """
    Converts into COBOL case where every word is capitalised.
    Also known as upper train case, screaming kebab case.
    
    >>> cobol_case('Grass is Green')
    'GRASS-IS-GREEN'
    """

    return "-".join(text_split(text, type=CaseType.UPPER))

@typechecked
def train_case(text: str) -> str:
    """
    Converts into train case where first letter of each word capitalized.
    Also known as HTTP Header Case.
    
    >>> train_case('Grass is Green')
    'Grass-Is-Green'
    """

    return "-".join(text_split(text, type=CaseType.PASCAL))

@typechecked
def camel_to_lower(text: str) -> str:
    """
    Split Camel Case and convert to lowercase. 
    Strip surrounding whitespace.
    
    >>> camel_to_lower('grassIsGreen')
    'grass is green'
    """

    return RE_CAMEL_CASE.sub(r" \1", text).strip().lower()

@typechecked
def snake_to_lower(text: str) -> str:
    """
    Split Snake Case and convert to lowercase. 
    Strip surrounding whitespace.
    
    >>> snake_to_lower('grass_is_green')
    'grass is green'
    """

    return " ".join(text.strip().lower().split("_"))

@typechecked
def kebab_to_lower(text: str) -> str:
    """
    Split Kebab Case and convert to lowercase. 
    Strip surrounding whitespace.

    >>> kebab_to_lower('grass-is-green')
    'grass is green'
    """

    return " ".join(text.strip().lower().split("-"))
