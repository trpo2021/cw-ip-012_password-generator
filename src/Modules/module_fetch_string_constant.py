import string

LETTERS_LOWERS = string.ascii_lowercase
LETTERS_UPPERS = string.ascii_uppercase
NUMBERS = string.digits
PUNCTUATION = string.punctuation

def fetch_string_constant(choice_list):
    '''
    Returns a string constant based on users choice_list.
    string constant can either be digits, letters, punctuation or
    combination of them.
    : choice_list --> list <class 'list'> of boolean
        0 item ---> digits
            True to add digits to constant False otherwise
        1 item ---> letters
            True to add letters to constant False otherwise
        2 item ---> punctuation
            True to add punctuation to constant False otherwise
    '''
    string_constant = ''

    string_constant += NUMBERS if choice_list[0] else ''
    string_constant += LETTERS_LOWERS if choice_list[1] else ''
    string_constant += LETTERS_UPPERS if choice_list[2] else ''
    string_constant += PUNCTUATION if choice_list[3] else ''

    return string_constant