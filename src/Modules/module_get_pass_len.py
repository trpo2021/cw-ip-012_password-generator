def get_password_length():
    '''
    Retrieves the length of a password
    :returns number <class 'int'>
    '''
    while True:
        length = input("How long do you want your password: ")
        try:
            temp_lenght = int(length)
        except ValueError:
            print("Length must be non-negative real number")
        except TypeError:
            print("Length must be non-negative real number")
        else:
            break
    return int(length)
