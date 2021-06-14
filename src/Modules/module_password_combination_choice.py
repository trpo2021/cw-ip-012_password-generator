def password_combination_choice():
    '''
    Prompt a user to choose password character combination which
    could either be digits, letters, punctuation or combibation of
    either of them.
    :returns list <class 'list'> of boolean [True, True, False]
        0 item ---> digits
        1 item ---> letters
        2 item ---> punctuation
    '''

    # retrieve a user's password character combination choice
    want_digits = input("Want digits ? (True or False) : ")
    want_letters_lowers = input("Want lowers letters ? (True or False): ")
    want_letters_uppers = input("Want uppers letters ? (True or False): ")
    want_puncts = input("Want punctuation ? (True or False): ")

    # convert those choices from string to it's right boolean type
    try:
        want_digits = eval(want_digits.title())
        want_puncts = eval(want_puncts.title())
        want_letters_lowers = eval(want_letters_lowers.title())
        want_letters_uppers = eval(want_letters_uppers.title())
        return [want_digits, want_letters_lowers, want_letters_uppers, want_puncts]

    except NameError as e:
        print("Invalid value. Use either True or False")
        print("Invalidity returns a default, try again to regenerate")

    return [True, True, True, True]