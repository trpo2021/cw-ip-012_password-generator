def password_combination_choice(user_option_input1, user_option_input2, user_option_input3, user_option_input4):
    """
    Prompt a user to choose password character combination which
    could either be digits, letters, punctuation or combibation of
    either of them.
    :returns list <class 'list'> of boolean [True, True, False]
        0 item ---> digits
        1 item ---> letters
        2 item ---> punctuation
    """

    # convert those choices from string to it's right boolean type
    try:
        want_digits = eval(user_option_input1.title())
        want_puncts = eval(user_option_input4.title())
        want_letters_lowers = eval(user_option_input2.title())
        want_letters_uppers = eval(user_option_input3.title())
        #return [want_digits, want_letters_lowers, want_letters_uppers, want_puncts]

    except TypeError:
        print("Invalid value. Use either True or False")
        print("Invalidity returns a default, try again to regenerate")
        want_digits = True
        want_puncts = True
        want_letters_lowers = True
        want_letters_uppers = True

    return [want_digits, want_letters_lowers, want_letters_uppers, want_puncts]
