from Modules import module_get_help_text
from Modules import module_get_pass_len
from Modules import module_pass_generator
from Modules import module_password_combination_choice


def main():
    module_get_help_text.get_help_text()
    user_input = input("How long do you want your password: ")
    user_option_input1 = input("Want digits ? (True or False) : ")
    user_option_input2 = input("Want lowers letters ? (True or False): ")
    user_option_input3 = input("Want uppers letters ? (True or False): ")
    user_option_input4 = input("Want punctuation ? (True or False): ")
    length = module_get_pass_len.get_password_length(user_input)
    choice_list = module_password_combination_choice.password_combination_choice(user_option_input1, user_option_input2, user_option_input3, user_option_input4)
    password = module_pass_generator.password_generator(choice_list, length)

    print(f'Your password: {password}')


main()
