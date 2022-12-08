import string
import sys
from archive_checker import check_pwd, check_archive


def crack_password(path: str):
    check_archive(path)

    all_chars = string.ascii_letters + string.digits

    characters = list(all_chars)
    length = len(characters)

    for idx in range(1, 11):
        generate_pwd(path=path, input_chars=characters, generated="", n=length, current_pwd_length=idx)


def generate_pwd(path: str, input_chars: list, generated: str, n: int, current_pwd_length: int):
    if current_pwd_length == 0:
        checking = check_pwd(path=path, pwd=generated)
        if checking is not None:
            print(f'PASSWORD FOUND - {generated}')

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
