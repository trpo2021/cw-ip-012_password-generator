def get_password_length(user_input):
    """
    Retrieves the length of a password
    :returns number <class 'int'>
    """
    try:
        length = int(user_input)
    except ValueError:
        print("Length must be non-negative real number")
        print("Length set by 10")
        length = 10
    except TypeError:
        print("Length must be non-negative real number")
        print("Length set by 10")
        length = 10

    return int(length)
