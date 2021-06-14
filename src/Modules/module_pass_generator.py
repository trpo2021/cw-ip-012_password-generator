from src.Modules import module_fetch_string_constant
import random

def password_generator(cbl, length=8):
    '''
    Generates a random password having the specified length
    :length -> length of password to be generated. Defaults to 8
        if nothing is specified
    :cbl-> a list of boolean values representing a user choice for
        string constant to be used to generate password.
        0 item ---> digits
             True to add digits to constant False otherwise
        1 item ---> uppercase letters
             True to add uppercase letters to constant False otherwise
        2 item ---> lowercase letters
             True to add lowercase letters to constant False otherwise
        3 item ---> punctuation
             True to add punctuation to constant False otherwise
    :returns string <class 'str'>
    '''
    # create alphanumerical by fetching string constant
    printable = module_fetch_string_constant.fetch_string_constant(cbl)

    # convert printable from string to list and shuffle
    printable = list(printable)
    random.shuffle(printable)

    # generate random password
    random_password = random.choices(printable, k=length)

    # convert generated password to string
    random_password = ''.join(random_password)
    return random_password