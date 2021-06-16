def get_password_length(user_input):
    """
    Retrieves the length of a password
    :returns number <class 'int'>
    """
    if user_input.isdigit:
        length = int(user_input)
    else:
        raise TypeError("Length must be a number")
    if length < 0:
        raise ValueError("Length must be a non-negative number")

    return int(length)
