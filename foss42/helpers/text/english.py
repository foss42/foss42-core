PUNCTUATIONS = [
  '"',
  "'",
  "!",
  "“",
  "‘",
  "(",
  ")",
  "-",
  "—",
  "/",
  ",",
  ".",
  ":",
  ";",
  "?",
  "…",
]

SPECIAL_SYMBOLS = [
  "#",
  "$",
  "%",
  "&",
  "`",
  "{",
  "|",
  "}",
  "~",
  "@",
  "[",
  "]",
  "_",
  "\\",
  "*",
  "+",
]

ARTICLES = [
  'a',
  'an',
  'the',
]

PREPOSITIONS = [
  'as',
  'at',
  'by',
  'for',
  'from',
  'in',
  'into',
  'of',
  'off',
  'on',
  'onto',
  'per',
  'till',
  'to',
  'until',
  'up',
  'via',
  'with',
]

SMALL_PREP = [p for p in PREPOSITIONS if len(p) <= 3]

CONJUNCTIONS = [
  'and',
  'as',
  'but',
  'for',
  'if',
  'nor',
  'or',
  'so',
  'yet',
]

OTHER_LOWER = [
  'vs.',
  'vs',
  'v.',
  'v',
  'en',
]

SMALL_TITLE = list(set(ARTICLES + SMALL_PREP + CONJUNCTIONS + OTHER_LOWER))
