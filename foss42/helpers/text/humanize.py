CURRENCY_UNIT_SINGULAR = "<unit>"
CURRENCY_SUBUNIT_SINGULAR = "<subunit>"
CURRENCY_UNIT_PLURAL = "<units>"
CURRENCY_SUBUNIT_PLURAL = "<subunits>"

NUM_WORDS = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}

NUM_ORDS = {
    0: "zeroth",
    1: "first",
    2: "second",
    3: "third",
    4: "fourth",
    5: "fifth",
    6: "sixth",
    7: "seventh",
    8: "eighth",
    9: "ninth",
    10: "tenth",
    11: "eleventh",
    12: "twelfth",
}

NUM_ORDS_SHORT = {
    0: "th",
    1: "st",
    2: "nd",
    3: "rd",
    4: "th",
    5: "th",
    6: "th",
    7: "th",
    8: "th",
    9: "th",
}

# power of 10 : short scale
SHORT_SCALE_WORDS = {
    2: "hundred",
    3: "thousand",
    6: "million",
    9: "billion",
    12: "trillion",
    15: "quadrillion",
    18: "quintillion",
    21: "sextillion",
    24: "septillion",
    27: "octillion",
    30: "nonillion",
}

INDIAN_SCALE_WORDS = {
    2: "hundred",
    3: "thousand",
    5: "lakh",
    7: "crore",
    9: "arab",
    11: "kharab",
    13: "nil",
    15: "padma",
    17: "shankh"
}

SHORT_SCALE_SIZES = list(zip(list(SHORT_SCALE_WORDS), list(SHORT_SCALE_WORDS)[1:] + [float("inf")]))
INDIAN_SCALE_SIZES = list(zip(list(INDIAN_SCALE_WORDS), list(SHORT_SCALE_WORDS)[1:] + [float("inf")]))

# power of 10 : N. America abbreviation
ABBR_NUM = {
    "NA" :{
        0: "",
        3: "K",
        6: "M",
        9: "B",
        12: "T",  
    },
    "UK": {
        0: "",
        3: "k",
        6: "m",
        9: "bn",
        12: "tn",
    },
    "SS": {
        0: "",
        3: "thousand",
        6: "million",
        9: "billion",
        12: "trillion",        
    }
}

ABBR_SIZES = list(zip(list(ABBR_NUM["NA"]), list(ABBR_NUM["NA"])[1:] + [float("inf")]))

# power of 10 : (prefix, symbol)
METRIC_PREFIX = {
    0: ("", ""),
    1: ("deca", "da"),
    2: ("hecto", "h"),
    3: ("kilo", "k"),
    6: ("mega", "M"),
    9: ("giga", "G"),
    12: ("tera", "T"),
    15: ("peta", "P"),
    18: ("exa", "E"), 
    21: ("zetta", "Z"),
    24: ("yotta", "Y"),
    27: ("ronna", "R"),
    30: ("quetta", "Q")
}

SIZE_SYMBOLS = ('B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')

TIME_UNIT = [
    (0, 1, "ms", "millisecond"),
    (1, 60, "s", "second"),
    (60, 60*60, "m", "minute"),
    (60*60, 24*60*60, "h", "hour"),
    (24*60*60, 7*24*60*60, "d", "day"),
    (7*24*60*60, 365*24*60*60, "w", "week"),
    (365*24*60*60, float("inf"), "y", "year"),
]

TIME_UNIT_IDX = {"FULL": 3, "SHORT": 2}