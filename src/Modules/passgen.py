import string
import random

LETTERS_LOWERS = string.ascii_lowercase
LETTERS_UPPERS = string.ascii_uppercase
NUMBERS = string.digits
PUNCTUATION = string.punctuation


def get_password_length():
    '''
    Retrieves the length of a password
    :returns number <class 'int'>
    '''
    length = input("How long do you want your password: ")
    return int(length)


# def get_number_password():
#     number = input("Enter a number of password: ")
#     return int(number)


def get_help_text():
        print("""
            Description of options:

            -0, --without numbers Will not include numbers in generated passwords.

            -A, --no-capitalize Don't capitalize generated passwords.

            -1, Will output the generated passwords, one on each line.

            -c, --capitalize Include at least one capital letter in the password.

            -h, --help Prints a help message.

            -y, --symbols Include at least one special character in the password.
            """)


def password_generator(cbl, length=8):
    '''
    Generates a random password having the specified length
    :length -> length of password to be generated. Defaults to 8
        if nothing is specified
    :cbl-> a list of boolean values representing a user choice for
        string constant to be used to generate password.
        0 item ---> digits
             True to add digits to constant False otherwise
        1 item ---> letters
             True to add letters to constant False otherwise
        2 item ---> punctuation
             True to add punctuation to constant False otherwise
    :returns string <class 'str'>
    '''
    # create alphanumerical by fetching string constant
    printable = fetch_string_constant(cbl)

    # convert printable from string to list and shuffle
    printable = list(printable)
    random.shuffle(printable)

    # generate random password
    random_password = random.choices(printable, k=length)

    # convert generated password to string
    random_password = ''.join(random_password)
    return random_password


def password_combination_choice():
    '''
    Prompt a user to choose password character combination which
    could either be digits, letters, punctuation or combibation of
    either of them.
    :returns list <class 'list'> of boolean [True, True, False]
        0 item ---> digits
        1 item ---> lower case letters
        2 item ---> upper case letters
        3 item ---> punctuation
        4 item ---> help text
    '''

    # retrieve a user's password character combination choice
    want_digits = input("Want digits ? (True or False) : ")
    want_letters_lowers = input("Want lowers letters ? (True or False): ")
    want_letters_uppers = input("Want uppers letters ? (True or False): ")
    want_puncts = input("Want punctuation ? (True or False): ")
    want_help = input("Want help text ? (True or False): ")

    # convert those choices from string to it's right boolean type
    try:
        want_digits = eval(want_digits.title())
        want_puncts = eval(want_puncts.title())
        want_letters_lowers = eval(want_letters_lowers.title())
        want_letters_uppers = eval(want_letters_uppers.title())
        want_help = eval(want_help.title())
        return [want_digits, want_letters_lowers, want_letters_uppers, want_puncts, want_help]

    except NameError as e:
        print("Invalid value. Use either True or False")
        print("Invalidity returns a default, try again to regenerate")

    return [True, True, True, True, True]


def fetch_string_constant(choice_list):
    '''
    Returns a string constant based on users choice_list.
    string constant can either be digits, letters, punctuation or
    combination of them.
    : choice_list --> list <class 'list'> of boolean
        0 item ---> digits
            True to add digits to constant False otherwise
        1 item ---> lower case letters
            True to add lower case letters to constant False otherwise
        2 item ---> upper case letters
            True to add upper case letters to constant False otherwise
        3 item ---> punctuation
            True to add punctuation to constant False otherwise
    '''
    string_constant = ''

    string_constant += NUMBERS if choice_list[0] else ''
    string_constant += LETTERS_LOWERS if choice_list[1] else ''
    string_constant += LETTERS_UPPERS if choice_list[2] else ''
    string_constant += PUNCTUATION if choice_list[3] else ''

    return string_constant


def main():
    get_help_text()
    length = get_password_length()
    choice_list = password_combination_choice()
    password = password_generator(choice_list, length)
    print(password)

main()
