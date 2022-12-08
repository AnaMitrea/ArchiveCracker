import string
import sys
from archive_checker import check_pwd, check_archive


def crack_password(path: str):
    """
    Password cracker for length of maximum 10 alphanumerical characters
    :param path: File path
    :return: None
    """
    check_archive(path)

    all_chars = string.ascii_letters + string.digits

    characters = list(all_chars)
    length = len(characters)

    for idx in range(1, 11):
        generate_pwd(path=path, input_chars=characters, generated="", n=length, current_pwd_length=idx)


def generate_pwd(path: str, input_chars: list, generated: str, n: int, current_pwd_length: int):
    """
    Recursive password generator based on brute force algorithm which generates passwords starting from lowercase
    characters, to uppercase characters to digits.
    The algorithm builds character by character all the possibilities of a password. If password can open the given zip
    file, the recursive function stops the execution
    :param path: File path
    :param input_chars:  Lower & Upper characters & digits
    :param generated: Generated password which is recursively built
    :param n: How many characters to be used from input_chars string
    :param current_pwd_length: Current Password length, ranging from 1 to maximum 10
    :return:
    """
    if current_pwd_length == 0:
        # print(f'Trying..... {generated}')
        checking = check_pwd(path=path, pwd=generated)
        if checking is not None:
            print(f'\nPASSWORD FOUND - \'{generated}\'')
            print('[Stopping Brute-Force Algorithm]')
            sys.exit(1)
        return

    for i in range(n):
        new_generated = generated + input_chars[i]

        generate_pwd(path=path,
                     input_chars=input_chars,
                     generated=new_generated,
                     n=n,
                     current_pwd_length=current_pwd_length - 1
                     )
