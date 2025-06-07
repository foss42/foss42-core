from datetime import datetime, timedelta, timezone

from typeguard import typechecked
from foss42.user.config import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, SECRET_KEY
from jose import jwt


@typechecked
def create_access_token(data: dict):
    """
    Generates a JWT access token.

    Args:
        data: A dictionary containing the user data to be encoded in the token.
        expires_delta: An optional timedelta object representing the token's expiration time.
                       If not provided, the token expires in 15 minutes.

    Returns:
        A string representing the encoded JWT access token.

    >>> token = create_access_token({'sub': 'Craig Espinoza'})
    >>> isinstance(token, str)
    True
    >>> from jose import jwt
    >>> from foss42.user.config import SECRET_KEY, ALGORITHM
    >>> decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    >>> decoded['sub']
    'Craig Espinoza'
    """
    expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

print(create_access_token({'sub': 12341}))