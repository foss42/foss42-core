import math
from datetime import datetime, timezone
from typing import Optional
from typeguard import typechecked
from foss42.helpers.text.humanize import *

@typechecked
def remove_trailing_zeros(num: str) -> str:
    """
    >>> remove_trailing_zeros("1.00")
    '1'
    >>> remove_trailing_zeros("0.000000")
    '0'
    >>> remove_trailing_zeros("0001.000000")
    '0001'
    """

    match num.split('.'):
        case [w]:
            pass
        case [w, d]:
            d = d.rstrip('0')
            d = f'.{d}' if len(d) > 0 else ""
            num = f"{w}{d}"
    return num

@typechecked
def humanize_bytes(num: int | str, 
                   digits: int = 0,
                   prefix: bool = False,
                   add_space: bool = True,
                   trailing_zeros: bool = False) -> str:
    """
    Turns `num` bytes into a human readable format.  
    `digits` specify the max. number of digits after the decimal (default `0`).
    If `trailing_zeros` is False (default), all trailing zeros to the right of the decimal point are removed.
    For example, if the final result is 1.10 MB, the trailing 0 is removed and 1.1 MB is returned.
    If `prefix` is `True` then SI prefixes (kilobytes, megabytes, gigabytes, etc.) are used instead of the symbols.  
    `add_space` (default `True`) can be used to specify whether a space should be added between the number and the unit (1 MB or 1MB). 

    >>> humanize_bytes(128991)
    '126 KB'
    >>> humanize_bytes(100001221)
    '95 MB'
    >>> humanize_bytes(0, 2)
    '0 B'
    >>> humanize_bytes(1, 3) # No decimal 0s as they are not significant.
    '1 B'
    >>> humanize_bytes(1024, add_space = False)                   
    '1KB'
    >>> humanize_bytes(24117248, 0, add_space = False)
    '23MB'
    >>> humanize_bytes(664365320, 2)
    '633.59 MB'
    >>> humanize_bytes(4324324232343, 2, add_space = False)
    '3.93TB'
    >>> humanize_bytes(664365320, 4)
    '633.5881 MB'
    >>> humanize_bytes(4324324232343, 3)
    '3.933 TB'
    >>> humanize_bytes(128991, prefix = True)
    '126 kilobytes'
    >>> humanize_bytes(100001221, prefix = True)
    '95 megabytes'
    >>> humanize_bytes(1126, 2, prefix = True)
    '1.1 kilobytes'
    >>> humanize_bytes(1126, 2, prefix = True, trailing_zeros = True)
    '1.10 kilobytes'
    >>> humanize_bytes('abc')
    Traceback (most recent call last):
        ...
    ValueError: num should be a valid number.
    >>> humanize_bytes(-10)
    Traceback (most recent call last):
        ...
    ValueError: num cannot be less than 0.
    """

    try:
        num = int(num) if type(num) is str else num
    except Exception as e:
        raise ValueError("num should be a valid number.")
    symbol = SIZE_SYMBOLS[0]
    units = "bytes"
    if num < 0:
        raise ValueError("num cannot be less than 0.")
    elif num == 0:
        res = 0
    else:
        p = math.floor(math.log2(num)/10)
        p = len(SIZE_SYMBOLS) if p > len(SIZE_SYMBOLS) else p
        symbol = SIZE_SYMBOLS[p]
        units = METRIC_PREFIX[3*p][0] + units
        res = num/1024**p
    if prefix: symbol = units
    if add_space: symbol = f" {symbol}"
    result = f'{res:.{digits}f}'
    if not trailing_zeros:
        result = remove_trailing_zeros(result)
    return  f"{result}{symbol}"

@typechecked
def humanize_social(num: int | str, 
                    digits: int = 1, 
                    system: str = "NA",
                    add_space: bool = False,
                    trailing_zeros: bool = False) -> str:
    """
    Returns a human readable version of social media numbers like number of followers, shares, likes, etc.
    `digits` specify the max. number of digits after the decimal (default `1`).
    If `trailing_zeros` is False (default), all trailing zeros to the right of the decimal point are removed.
    For example, if the final result is 1.10, the trailing 0 is removed and 1.1 is returned.  
    `add_space` (default `False`) can be used to specify whether a space should be added between the number and the unit (1 K or 1K).
    `system` can be "NA" (default), "UK" or "SS" to switch between US abbreviation ("K", "M", "B", "T"), UK abbreviation ("k", "m", "bn", "tn") or SS - Short Scale ("thousand", "million", "billion", "trillion)  system.
    If `num` is greater than trillion, it is specified in trillions no matter how large the amount.

    >>> humanize_social(3456)
    '3.5K'
    >>> humanize_social(3456, 0)
    '3K'
    >>> humanize_social(3456, 2)
    '3.46K'
    >>> humanize_social(3456, add_space = True)
    '3.5 K'
    >>> humanize_social(3456, system = "UK", add_space = True)
    '3.5 k'
    >>> humanize_social(345, 2)
    '345'
    >>> humanize_social(0)
    '0'
    >>> humanize_social(10000000)
    '10M'
    >>> humanize_social(2000000000, system = "UK")
    '2bn'
    >>> humanize_social(2200000000, system = "SS", add_space = True)
    '2.2 billion'
    >>> humanize_social(30000000000000)
    '30T'
    >>> humanize_social(11500)
    '11.5K'
    >>> humanize_social(11500, digits = 2)
    '11.5K'
    >>> humanize_social(11500, digits = 2, trailing_zeros = True)
    '11.50K'
    >>> humanize_social(1070)
    '1.1K'
    >>> humanize_social('abc')
    Traceback (most recent call last):
        ...
    ValueError: num should be a valid number.
    >>> humanize_social(-10)
    Traceback (most recent call last):
        ...
    ValueError: num cannot be less than 0.
    >>> humanize_social(10, system = "PO")
    Traceback (most recent call last):
        ...
    ValueError: Permitted Values of system are  ['NA', 'UK', 'SS'].
    """

    try:
        num = int(num) if type(num) is str else num
    except Exception as e:
        raise ValueError("num should be a valid number.")    
    if system not in ABBR_NUM:
        raise ValueError(f"Permitted Values of system are {list(ABBR_NUM.keys())}.")
    symbol = ABBR_NUM[system][0]
    if num < 0:
        raise ValueError("num cannot be less than 0.")
    elif num == 0:
        res = 0
    else:
        p = math.floor(math.log10(num))
        for l, g in ABBR_SIZES:
            if l <= p < g:
                p = l
        symbol = ABBR_NUM[system][p]
        res = num/10**p
    if add_space: symbol = f" {symbol}"
    result = f'{res:.{digits}f}'
    if not trailing_zeros:
        result = remove_trailing_zeros(result)
    return  f"{result}{symbol}"

@typechecked
def humanize_rank(num: int | str) -> str:
    """
    Covert a number provided as an interger or string into its ordinal form that indicates the exact position or rank in a leaderboard. 

    >>> humanize_rank(0)
    '0th'
    >>> humanize_rank('1')
    '1st'
    >>> humanize_rank(2)
    '2nd'
    >>> humanize_rank(3)
    '3rd'
    >>> [humanize_rank(5), humanize_rank(61), humanize_rank(80)]
    ['5th', '61st', '80th']
    >>> [humanize_rank(112), humanize_rank(120), humanize_rank(1101)]
    ['112th', '120th', '1101st']
    >>> [humanize_rank(11), humanize_rank(12), humanize_rank(13)]
    ['11th', '12th', '13th']
    >>> humanize_rank('abc')
    Traceback (most recent call last):
        ...
    ValueError: num should be a valid number.
    >>> humanize_rank(-10)
    Traceback (most recent call last):
        ...
    ValueError: num cannot be less than 0.
    """

    try: 
        num = int(num) if type(num) is str else num
    except Exception as e:
        raise ValueError("num should be a valid number.")
    
    if num < 0:
        raise ValueError("num cannot be less than 0.")

    if num%100 in (11, 12, 13):
        return f"{num}th"
    else:
        return f"{num}{NUM_ORDS_SHORT[num%10]}"

@typechecked
def parse_dt(dt: str | datetime,
             fmt: Optional[str] = None) -> datetime:
    '''
    Parse a date in form of string or datetime object and returns it with timezone.
    >>> parse_dt('2009-12-17T08:31:29')
    datetime.datetime(2009, 12, 17, 8, 31, 29, tzinfo=datetime.timezone.utc)
    >>> parse_dt('2009-12-17T08:31:29Z')
    datetime.datetime(2009, 12, 17, 8, 31, 29, tzinfo=datetime.timezone.utc)
    >>> parse_dt('2009-12-17T08:31:29+01:00')
    datetime.datetime(2009, 12, 17, 8, 31, 29, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600)))
    >>> parse_dt(datetime(2023, 3, 7, 14))
    datetime.datetime(2023, 3, 7, 14, 0, tzinfo=datetime.timezone.utc)
    >>> parse_dt("14 Jan, 2023", "%d %b, %Y")
    datetime.datetime(2023, 1, 14, 0, 0, tzinfo=datetime.timezone.utc)
    '''
    dt_val = None
    try:
        if type(dt) is str:
            if fmt is None:
                dt_val = datetime.fromisoformat(dt)
            else:
                dt_val = datetime.strptime(dt, fmt)
        elif isinstance(dt, datetime):
            dt_val = dt
        else:
            raise TypeError("Incorrect type of input date.")
        if dt_val.tzinfo is None:
            dt_val = dt_val.replace(tzinfo=timezone.utc)
    except Exception as e:
        raise ValueError("Error parsing input date.")
    return dt_val

@typechecked
def humanize_time(dt: str | datetime,
                  dt_ref: Optional[str | datetime] = None, 
                  fmt: Optional[str] = None,
                  units: str = "FULL", 
                  cutoff_now: int = 1,
                  add_adverb: bool = False,
                  use_article: bool = False,
                  round_down: bool = True) -> str:
    """
    Returns a time difference in human readable verison as typically displayed in social media.
    eg: .. minutes ago, .. days ago, .. hours from now, etc.
    `dt` can be a `datetime.datetime` object or a valid ISO 8601 format string.
    `dt_ref` can be used to supply a base time. The current system timestamp is used if it is `None`.
    `fmt` can be used to provide the format of the timestamp if it is not in a valid ISO 8601 format.
    Check https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes to learn more about formatting date strings.
    `units` can be "FULL" (default) or "SHORT"
    `cutoff_now` is the number of seconds of time difference for which "now" is returned instead of the actual time difference. Default is set as `1` which means that any time difference less than a second is returned as "now" instead of the time difference in milliseconds.
    `add_adverb` if `True` (default is `False`), adds "ago" or "from now" based on the time difference.
    `use_article` if `True` (default is `False`), uses article "a" and "an" instead of "1". For example, "a minute ago" instead of "1 minute ago".
    `round_down` if True (default), rounds the time difference to the largest unit quantity that is less than or equal to it. For example, "1 week, 2 days" becomes "1 week". If turned `False`, "1 week, 2 days" still returns "1 week", but "1 week, 5 days" returns "2 weeks".
    
    >>> humanize_time('2008-12-18T16:30:00', '2008-12-18T16:30:00')
    'now'
    >>> humanize_time('2008-12-18T16:29:31', '2008-12-18T16:30:00')
    '29 seconds'
    >>> humanize_time('2008-12-18T16:29:31', '2008-12-18T16:30:00', add_adverb = True)
    '29 seconds ago'
    >>> humanize_time('2008-12-18T16:29:00', '2008-12-18T16:30:00', add_adverb = True)
    '1 minute ago'
    >>> humanize_time('2008-12-18T16:29:00', '2008-12-18T16:30:00', add_adverb = True, use_article = True)
    'a minute ago'
    >>> humanize_time('2008-12-18T16:25:35', '2008-12-18T16:30:00', units = "SHORT")
    '4 m'
    >>> humanize_time('2008-12-18T15:30:29', '2008-12-18T16:30:00')
    '59 minutes'
    >>> humanize_time('2008-12-18T15:30:01', '2008-12-18T16:30:00')
    '59 minutes'
    >>> humanize_time('2008-12-18T15:30:01', '2008-12-18T16:30:00', round_down = False)
    '1 hour'
    >>> humanize_time('2008-12-18T15:30:01', '2008-12-18T16:30:00', units = "SHORT", round_down = False)
    '1 h'
    >>> humanize_time('2008-12-18T15:30:00', '2008-12-18T16:30:00', add_adverb = True, use_article = True)
    'an hour ago'
    >>> humanize_time('2008-12-18T13:31:29', '2008-12-18T16:30:00', add_adverb = True)
    '2 hours ago'
    >>> humanize_time('2008-12-17T13:31:29', '2008-12-18T16:30:00')
    '1 day'
    >>> humanize_time('2008-12-17T13:30:01', '2008-12-18T16:30:00', add_adverb = True)
    '1 day ago'
    >>> humanize_time('2008-12-17T01:30:00', '2008-12-18T16:30:00')
    '1 day'
    >>> humanize_time('2008-12-17T01:30:00', '2008-12-18T16:30:00', round_down = False)
    '2 days'
    >>> humanize_time('2008-12-18T16:30:30', '2008-12-18T16:30:00', add_adverb = True)
    '30 seconds from now'
    >>> humanize_time('2008-12-18T16:30:29', '2008-12-18T16:30:00', units = "SHORT")
    '29 s'
    >>> humanize_time('2008-12-18T16:31:00', '2008-12-18T16:30:00', add_adverb = True, use_article = True) 
    'a minute from now'
    >>> humanize_time('2008-12-18T16:34:35', '2008-12-18T16:30:00', add_adverb = True) 
    '4 minutes from now'
    >>> humanize_time('2008-12-18T17:30:29', '2008-12-18T16:30:00', add_adverb = True, use_article = True) 
    'an hour from now'
    >>> humanize_time('2008-12-18T18:31:29', '2008-12-18T16:30:00', units = "SHORT", add_adverb = True) 
    '2 h from now'
    >>> humanize_time('2008-12-19T16:31:29', '2008-12-18T16:30:00', add_adverb = True, use_article = True) 
    '1 day from now'
    >>> humanize_time('2008-12-27T18:31:29', '2008-12-16T16:30:00', add_adverb = True, use_article = True) 
    '1 week from now'
    >>> humanize_time('2008-12-27T18:31:29', '2008-12-16T16:30:00', round_down = False, add_adverb = True) 
    '2 weeks from now'
    >>> humanize_time('2009-12-17T08:31:29', '2008-12-17T16:30:00') 
    '1 year'
    >>> humanize_time('2010-12-17T08:31:29', '2008-12-17T16:30:00', units = "SHORT") 
    '1 y'
    >>> humanize_time('2010-12-17T08:31:29', '2008-12-17T16:30:00', units = "SHORT", round_down = False) 
    '2 y'
    >>> humanize_time('2009-12-17T08:31:29Z', '2009-12-17T16:30:00') 
    '7 hours'
    >>> humanize_time('2009-12-17T08:31:29', '2009-12-17T16:30:00Z', round_down = False) 
    '8 hours'
    """

    dt_val = None
    
    try:
        dt_val = parse_dt(dt, fmt)
        if dt_ref is not None:
            dt_ref = parse_dt(dt_ref, fmt)
        else:
            dt_ref = datetime.now(timezone.utc)
    except Exception as e:
        raise e 
    
    if units not in TIME_UNIT_IDX:
        raise ValueError(f"Permitted Values of units are {list(TIME_UNIT_IDX.keys())}.")

    diff = (dt_val - dt_ref).total_seconds()
    if math.fabs(diff) < cutoff_now:
        return "now"

    end = ""
    if add_adverb:
        if diff < 0: 
            end = " ago"
        else:
            end = " from now"

    diff = math.fabs(diff)
    idx = None
    symbol = ""
    for i, row in enumerate(TIME_UNIT):
        if row[0] <= diff < row[1]:
            idx = i
            break
    
    p = TIME_UNIT[idx][0]
    res = int(diff/p) if round_down else round(diff/p)
    calc_res = res * p

    # take care of boundary cases
    if (calc_res == TIME_UNIT[idx][1]) or (TIME_UNIT[idx][2] == "w" and res == 52):
        idx += 1
        res = 1

    uIdx = TIME_UNIT_IDX[units]
    symbol = TIME_UNIT[idx][uIdx]

    if res > 1 and units == "FULL": symbol += "s"

    if use_article:
        if res == 1:
            if p == 1 or p == 60:
                res = "a"
            if p == 60*60:
                res = "an"

    return f'{res} {symbol}{end}'
