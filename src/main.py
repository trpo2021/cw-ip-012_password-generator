import string
import random
from src.Modules import module_pass_generator
from src.Modules import module_password_combination_choice
from src.Modules import module_get_pass_len
from src.Modules import module_get_help_text


def main():
    module_get_help_text.get_help_text()
    length = module_get_pass_len.get_password_length()
    choice_list = module_password_combination_choice.password_combination_choice()
    password = module_pass_generator.password_generator(choice_list, length)

    print(password)

main()