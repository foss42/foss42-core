from foss42.data.geo.country import *

ALPHA2_IDX_MAP =  {row[KEY_ALPHA2]: idx for idx, row in enumerate(COUNTRY_CODES)}
ALPHA3_IDX_MAP =  {row[KEY_ALPHA3]: idx for idx, row in enumerate(COUNTRY_CODES)}
ALPHA_IDX_MAP = ALPHA2_IDX_MAP | ALPHA3_IDX_MAP
NAME_ALPHA2_MAP = {(row[KEY_POPULAR_NAME] if KEY_POPULAR_NAME in row else row[KEY_NAME]): row[KEY_ALPHA2] 
                   for idx, row in enumerate(COUNTRY_CODES)}
NAME_IDX_MAP  = {row[KEY_NAME].lower(): idx for idx, row in enumerate(COUNTRY_CODES)} | \
                {row[KEY_POPULAR_NAME].lower(): idx for idx, row in enumerate(COUNTRY_CODES) if KEY_POPULAR_NAME in row} | \
                {term.lower(): idx for idx, row in enumerate(COUNTRY_CODES) if KEY_SEARCH in row for term in row[KEY_SEARCH]}

ALPHA2_FLAG_MAP = {k: ''.join([chr(127397 + ord(a)) for a in k]) for k in ALPHA2_IDX_MAP}

ALPHA2_PHONE_MAP = {row[KEY_ALPHA2]: idx for idx, row in enumerate(PHONE_CODES)}

# UN Data

REGION_ALPHA2_MAP = {}
SUB_REGION_ALPHA2_MAP = {}
INT_REGION_ALPHA2_MAP = {}
for t in REGION_COUNTRY_MAP:
    world, region, subregion, intregion = t
    if region is not None:
        if region not in REGION_ALPHA2_MAP:
            REGION_ALPHA2_MAP[region] = []
        REGION_ALPHA2_MAP[region].extend(REGION_COUNTRY_MAP[t])
    if subregion is not None:
        if subregion not in SUB_REGION_ALPHA2_MAP:
            SUB_REGION_ALPHA2_MAP[subregion] = []
        SUB_REGION_ALPHA2_MAP[subregion].extend(REGION_COUNTRY_MAP[t])       
    if intregion is not None:
        if intregion not in INT_REGION_ALPHA2_MAP:
            INT_REGION_ALPHA2_MAP[intregion] = []
        INT_REGION_ALPHA2_MAP[intregion].extend(REGION_COUNTRY_MAP[t])  

REGION_UNM49_MAP = {v: k for k, v in UNM49_REGION_MAP.items()}
ALPHA2_UNM49_MAP = {v: k for k, v in UNM49_ALPHA2_MAP.items()}

NO_WB_DATA = {KEY_AREA: None, KEY_POPULATION: None}

# Country Sub-region
CODE_SUB_CA_MAP = {row[KEY_CODE]: row for row in SUB_CA}
NAME_SUB_CA_MAP = {row[KEY_NAME]: row for row in SUB_CA}
CODE_SUB_KR_MAP = {row[KEY_CODE]: row for row in SUB_KR}
NAME_SUB_KR_MAP = {row[KEY_NAME]: row for row in SUB_KR}
CODE_SUB_IN_MAP = {row[KEY_CODE]: row for row in SUB_IN}
NAME_SUB_IN_MAP = {row[KEY_NAME]: row for row in SUB_IN}
CODE_SUB_JP_MAP = {row[KEY_CODE]: row for row in SUB_JP}
NAME_SUB_JP_MAP = {row[KEY_NAME]: row for row in SUB_JP}
CODE_SUB_CN_MAP = {row[KEY_CODE]: row for row in SUB_CN}
NAME_SUB_CN_MAP = {row[KEY_NAME]: row for row in SUB_CN}
CODE_SUB_AU_MAP = {row[KEY_CODE]: row for row in SUB_AU}
NAME_SUB_AU_MAP = {row[KEY_NAME]: row for row in SUB_AU}
CODE_SUB_US_MAP = {row[KEY_CODE]: row for row in SUB_US}
NAME_SUB_US_MAP = {row[KEY_NAME]: row for row in SUB_US}