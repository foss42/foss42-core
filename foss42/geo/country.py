from typing import Optional
from typeguard import typechecked
from foss42.data.geo.country import *
from foss42.helpers.geo.country import *

@typechecked
def is_valid_code(code: str,
                  only_alpha2: bool = False,
                  only_alpha3: bool = False,) -> tuple[bool, Optional[str]]:

    if len(code) not in (2, 3):
        return False, "Invalid country code is provided."

    if only_alpha2 and len(code) != 2:
        return False, "Alpha-2 country code should be of length 2."

    if only_alpha3 and len(code) != 3:
        return False, "Alpha-3 country code should be of length 3."

    code = code.upper()
    if (len(code) == 2) and (code not in ALPHA2_IDX_MAP):
        return False, "No country found for the given Alpha-2 country code."

    if (len(code) == 3) and (code not in ALPHA3_IDX_MAP):
        return False, "No country found for the given Alpha-3 country code."

    return True, None

@typechecked
def alpha3_to_alpha2(code: str) -> str:
    """
    Returns the Alpha-2 country code for the given Alpha-3 country code.

    >>> alpha3_to_alpha2('IND')
    'IN'
    >>> alpha3_to_alpha2('RED')
    Traceback (most recent call last):
        ...
    ValueError: No country found for the given Alpha-3 country code.
    >>> alpha3_to_alpha2('RE')
    Traceback (most recent call last):
        ...
    ValueError: Alpha-3 country code should be of length 3.   
    """

    status, msg = is_valid_code(code, only_alpha3 = True)
    if not status: 
        raise ValueError(msg)

    code = code.upper()
    return COUNTRY_CODES[ALPHA3_IDX_MAP[code]][KEY_ALPHA2]

@typechecked
def alpha2_to_alpha3(code: str) -> str:
    """
    Returns the Alpha-3 country code for the given Alpha-2 country code.

    >>> alpha2_to_alpha3('IN')
    'IND'
    >>> alpha2_to_alpha3('ZI')
    Traceback (most recent call last):
        ...
    ValueError: No country found for the given Alpha-2 country code.
    >>> alpha2_to_alpha3('RED')
    Traceback (most recent call last):
        ...
    ValueError: Alpha-2 country code should be of length 2.   
    """

    status, msg = is_valid_code(code, only_alpha2 = True)
    if not status: 
        raise ValueError(msg)

    code = code.upper()
    return COUNTRY_CODES[ALPHA2_IDX_MAP[code]][KEY_ALPHA3]

@typechecked
def country_code_map() -> dict:
    """
    Returns the map of country name (popular) and ISO Alpha-2 country code.

    >>> country_code_map()['Vietnam']
    'VN'
    >>> country_code_map()['South Korea']
    'KR'
    >>> len(country_code_map())
    250
    """

    return NAME_ALPHA2_MAP

@typechecked
def code_to_popular_name(code: str) -> str:
    """
    Returns the name by which a country is popularly know as for the given Alpha-3 or Alpha-2 country code.

    >>> code_to_popular_name('VN')
    'Vietnam'
    >>> code_to_popular_name('KOR')
    'South Korea'
    >>> code_to_popular_name('ZI')
    Traceback (most recent call last):
        ...
    ValueError: No country found for the given Alpha-2 country code.
    >>> code_to_popular_name('RED')
    Traceback (most recent call last):
        ...
    ValueError: No country found for the given Alpha-3 country code.
    >>> code_to_popular_name('REDI')
    Traceback (most recent call last):
        ...
    ValueError: Invalid country code is provided.
    """

    status, msg = is_valid_code(code)
    if not status: 
        raise ValueError(msg)

    code = code.upper()
    c = COUNTRY_CODES[ALPHA_IDX_MAP[code]]
    if KEY_POPULAR_NAME in c:
        return c[KEY_POPULAR_NAME]
    else:
        return c[KEY_NAME]

@typechecked
def code_to_official_name(code: str) -> str:
    """
    Returns the ISO official name of the country for the given Alpha-3 or Alpha-2 country code.

    >>> code_to_official_name('VN')
    'Viet Nam'
    >>> code_to_official_name('KOR')
    'Korea (the Republic of)'
    >>> code_to_official_name('ZI')
    Traceback (most recent call last):
        ...
    ValueError: No country found for the given Alpha-2 country code.
    >>> code_to_official_name('RED')
    Traceback (most recent call last):
        ...
    ValueError: No country found for the given Alpha-3 country code.
    >>> code_to_official_name('REDI')
    Traceback (most recent call last):
        ...
    ValueError: Invalid country code is provided.
    """

    status, msg = is_valid_code(code)
    if not status: 
        raise ValueError(msg)

    code = code.upper()
    return COUNTRY_CODES[ALPHA_IDX_MAP[code]][KEY_NAME]

@typechecked
def code_to_flag(code: str) -> str:
    """
    Returns the flag of the country given its ISO Alpha-2 or Alpha-3 country code.

    >>> code_to_flag('VN')
    '🇻🇳'
    >>> code_to_flag('KR')
    '🇰🇷'
    >>> code_to_flag('IND')
    '🇮🇳'
    >>> code_to_flag('ZI')
    Traceback (most recent call last):
        ...
    ValueError: No country found for the given Alpha-2 country code.
    >>> code_to_flag('RED')
    Traceback (most recent call last):
        ...
    ValueError: No country found for the given Alpha-3 country code.
    >>> code_to_flag('R')
    Traceback (most recent call last):
        ...
    ValueError: Invalid country code is provided.
    """

    status, msg = is_valid_code(code)
    if not status: 
        raise ValueError(msg)
    
    code = code.upper()
    if len(code) == 3: 
        code = alpha3_to_alpha2(code)
    return ALPHA2_FLAG_MAP[code]

@typechecked
def code_to_data(code: str) -> dict:
    """
    Returns some key world bank data of the country given its ISO Alpha-2 or Alpha-3 country code.

    >>> code_to_data('VN')
    {'area': 331340.0, 'population': 97468029}
    >>> code_to_data('KR')
    {'area': 100410.0, 'population': 51744876}
    >>> code_to_data('IND')
    {'area': 3287260.0, 'population': 1407563842, 'population_female_percent': 48.39}
    >>> code_to_data('ZI')
    Traceback (most recent call last):
        ...
    ValueError: No country found for the given Alpha-2 country code.
    >>> code_to_data('RED')
    Traceback (most recent call last):
        ...
    ValueError: No country found for the given Alpha-3 country code.
    >>> code_to_data('R')
    Traceback (most recent call last):
        ...
    ValueError: Invalid country code is provided.
    """

    status, msg = is_valid_code(code)
    if not status: 
        raise ValueError(msg)
    
    code = code.upper()
    if len(code) == 2: 
        code = alpha2_to_alpha3(code)
    if code in ALPHA3_WB_DATA:
        return ALPHA3_WB_DATA[code]
    else:
        return NO_WB_DATA

@typechecked
def code_to_population_density(code: str) -> float:
    """
    Returns the population density of the country given its ISO Alpha-2 or Alpha-3 country code.

    >>> code_to_population_density('VN')
    294.24
    >>> code_to_population_density('KR')
    515.61
    >>> code_to_population_density('IND')
    428.9
    >>> code_to_population_density('ZI')
    Traceback (most recent call last):
        ...
    ValueError: No country found for the given Alpha-2 country code.
    >>> code_to_population_density('RED')
    Traceback (most recent call last):
        ...
    ValueError: No country found for the given Alpha-3 country code.
    >>> code_to_population_density('R')
    Traceback (most recent call last):
        ...
    ValueError: Invalid country code is provided.
    """
    
    status, msg = is_valid_code(code)
    if not status: 
        raise ValueError(msg)
    
    code = code.upper()
    if len(code) == 2: 
        code = alpha2_to_alpha3(code)
    
    data = code_to_data(code)
    if 'area' in data and 'population' in data:
        return data['population'] / data['area']
    else:
        raise ValueError("Population density data is not available for the given country code.")

@typechecked
def code_to_gender_ratio(code: str) -> float:
    """
    Returns the gender ratio (number of males per 100 females) of the country given its ISO Alpha-2 or Alpha-3 country code.

    >>> code_to_gender_ratio('VN')
    99.4
    >>> code_to_gender_ratio('KR')
    100.4
    >>> code_to_gender_ratio('IND')
    103.5
    >>> code_to_gender_ratio('ZI')
    Traceback (most recent call last):
        ...
    ValueError: No country found for the given Alpha-2 country code.
    >>> code_to_gender_ratio('RED')
    Traceback (most recent call last):
        ...
    ValueError: No country found for the given Alpha-3 country code.
    >>> code_to_gender_ratio('R')
    Traceback (most recent call last):
        ...
    ValueError: Invalid country code is provided.
    """

    status, msg = is_valid_code(code)
    if not status: 
        raise ValueError(msg)
    
    code = code.upper()
    if len(code) == 2: 
        code = alpha2_to_alpha3(code)
    
    data = code_to_data(code)
    if 'population_female_percent' in data:
        population_female_percent = data['population_female_percent']
        population_male_percent = 100 - population_female_percent
        return (population_male_percent / population_female_percent) * 100
    else:
        raise ValueError("Gender ratio data is not available for the given country code.")

@typechecked
def code_to_subdivision(code: str) -> list[dict]:
    """
    Returns the country subdivision details (states, territories, etc.) for the given two letter (Alpha-2) or three letter (Alpha-3) ISO 3166-1 country code. 
    Currently, the following countries are supported - AU (Australia), US (USA), CN (China), Japan (JP), IN (India), KR (South Korea) and CA (Canada).

    >>> code_to_subdivision('IN')[0:2]
    [{'code': 'AN', 'name': 'Andaman and Nicobar Islands', 'category': 'union territory'}, {'code': 'CH', 'name': 'Chandigarh', 'category': 'union territory'}]
    >>> len(code_to_subdivision('IN'))
    36
    >>> code_to_subdivision('US')[0]
    {'code': 'DC', 'name': 'District of Columbia', 'category': 'district'}
    >>> code_to_subdivision('IR')
    Traceback (most recent call last):
        ...
    NotImplementedError: Provided country code is currently not supported. Please raise a request to add support.
    >>> code_to_subdivision('XYZ')
    Traceback (most recent call last):
        ...
    ValueError: code should be a valid 2 or 3 letter country code.
    >>> code_to_subdivision('AXYZ')
    Traceback (most recent call last):
        ...
    ValueError: code should be a valid 2 or 3 letter country code.    
    """

    code = code.upper()
    if (len(code) not in (2, 3)) or (code not in ALPHA_IDX_MAP):
        raise ValueError("code should be a valid 2 or 3 letter country code.")

    if len(code) == 3: code = alpha3_to_alpha2(code)

    if code in SUB_SUPPORTED:
        return SUB_SUPPORTED[code]
    else:
        raise NotImplementedError("Provided country code is currently not supported. Please raise a request to add support.")
