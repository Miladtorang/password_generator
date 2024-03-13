import random
import string
import os

settings = {
    'upper': True,
    'lower': True,
    'symbol': True,
    'number': True,
    'space': False,
    'length': 8
}


def clear_cmd():
    os.system('cls')


def welcome_message():
    welcome = '''Welcome to the Random Password Generator!
    Let's get started on strengthening your digital defenses'''

    underline = '*' * len(welcome)

    print(f"\n{underline}\n{welcome}\n{underline}\n")


def get_password_length(option, default, pw_min_length=4, pw_max_length=30):
    while True:
        user_input = input('enter your password length. '
                           f'(default is {default}) (enter: default): ')

        if user_input == '':
            return default

        if user_input.isdigit():
            password_length = int(user_input)
            if 4 <= password_length <= 30:
                return int(user_input)
            print('invalid input')
            print(f'password length should be between'
                  f' {pw_min_length} and {pw_max_length}')
        else:
            print('invalid input.please enter a number.')
        print('please try again')


def get_option_from_user(option, default):
    while True:
        user_input = input(f'include {option}?'
                           f'(default is {default}) '
                           '(y: yes, n: no, enter: default):')

        if user_input == '':
            return default

        if user_input in ['y', 'n']:
            return user_input == 'y'

        print('invalid input please enter correct option')


def get_setting_from_user(settings):
    for option, default in settings.items():
        if option != 'length':
            user_choice = get_option_from_user(option, default)
            settings[option] = user_choice

        else:
            user_password_length = get_password_length(option, default)
            settings[option] = user_password_length


def ask_user_for_change_settings(settings):
    while True:
        user_input = input('do you want to change default settings? (y: yes, n: no, enter: yes): ')

        if user_input in ['y', 'n', '']:
            if user_input in ['y', '']:
                print('-' * 5, 'change settings', '-' * 5, sep='')
                get_setting_from_user(settings)
            break

        else:
            print('invalid input.')
            print('please try again')


def get_random_uppercase():
    return random.choice(string.ascii_uppercase)


def get_random_lowercase():
    return random.choice(string.ascii_lowercase)


def get_random_number():
    return random.randint(0, 9)


def get_random_symbol():
    return random.choice(string.punctuation)


def generate_random_char(choices):
    choice = random.choice(choices)

    if choice == 'upper':
        return get_random_uppercase()
    if choice == 'lower':
        return get_random_lowercase()
    if choice == 'symbol':
        return get_random_symbol()
    if choice == 'number':
        return str(get_random_number())
    if choice == 'space':
        return ' '


def password_generator(settings):
    final_password = ''
    user_password_length = settings['length']

    choices = list(filter(lambda x: settings[x], ['upper', 'lower', 'symbol', 'number', 'space']))

    for i in range(user_password_length):
        final_password += generate_random_char(choices)

    return final_password


def check_generate_another_password():
    while True:
        user_choice_another_password = input('do you want another pasword? (y: yes, n: no)')

        if user_choice_another_password in ['y', 'n', '']:
            if user_choice_another_password == 'n':
                return False
            return True

        else:
            print('invalid input.')
            print('please try again')


def password_generator_loop(settings):
    while True:
        print('-' * 20)
        print(f'generated password: {password_generator(settings)}')

        if check_generate_another_password() == False:
            break


def run():
    clear_cmd()
    welcome_message()
    ask_user_for_change_settings(settings)
    password_generator_loop(settings)
    print('success')


run()
