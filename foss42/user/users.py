import random

from typeguard import typechecked
from foss42.data.user.users import USERS


@typechecked
def get_random_user_data():
    """
    Retrieves a random user's data from the USERS list.

    Returns:
        A dictionary containing the data of a randomly selected user, 
        or None if the USERS list is empty.

    >>> isinstance(get_random_user_data(), dict)
    True
    >>> 'id' in get_random_user_data()
    True
    >>> 'name' in get_random_user_data()
    True
    >>> 'phone' in get_random_user_data()
    True
    >>> 'email' in get_random_user_data()
    True
    >>> 'country' in get_random_user_data()
    True
    >>> get_random_user_data() in USERS
    True
    """
    if not USERS:
        return None
    return random.choice(USERS)


@typechecked
def get_all_users_data():
    """
    Retrieves all users' data from the USERS list.

    Returns:
        A list of dictionaries, where each dictionary contains the data of a user.
        Returns an empty list if the USERS list is empty.

    >>> isinstance(get_all_users_data(), list)
    True
    >>> len(get_all_users_data())
    100
    >>> isinstance(get_all_users_data()[0], dict)
    True
    >>> 'id' in get_all_users_data()[0]
    True
    """
    if not USERS:
        return []
    return [user_data for user_data in USERS]


@typechecked
def get_user_data_by_id(user_id: int):
    """
    Retrieves a user's data by their ID using circular indexing.

    If the user_id is out of bounds, it wraps around to select a user
    from the available USERS list. For example, there are 100 users,
    a user_id of 101 will return the first user, and a user_id of 0
    will return the last user.

    Args:
        user_id: The integer ID of the user to retrieve.

    Returns:
        A dictionary containing the data of the selected user,
        or None if the USERS list is empty.

    >>> user = get_user_data_by_id(1)
    >>> user == USERS[0]
    True
    >>> get_user_data_by_id(101) == USERS[0]  # Circular indexing
    True
    >>> get_user_data_by_id(0) == USERS[-1]   # Wraps to last user
    True
    >>> get_user_data_by_id(-1) == USERS[98]   # Wraps to 99th user
    True
    >>> isinstance(get_user_data_by_id(50), dict)
    True
    >>> 'id' in get_user_data_by_id(50)
    True
    """
    if not USERS:
        return None
    user_id = user_id % len(USERS)
    return USERS[user_id - 1]
