import os
from zipfile import BadZipFile, ZipFile, is_zipfile


def check_archive(path: str):
    try:
        if not os.path.exists(path):
            raise FileNotFoundError

        if not is_zipfile(path):
            raise BadZipFile

    except FileNotFoundError as e:
        raise Exception('[EXCEPTION OCCURRED] FILE NOT FOUND').with_traceback(e.__traceback__)
    except BadZipFile as e:
        raise Exception('[EXCEPTION OCCURRED] ARCHIVE MUST HAVE ZIP EXTENSION').with_traceback(e.__traceback__)
    except Exception as e:
        print(f'Unexpected Exception occurred: {e}')


def check_pwd(path: str, pwd: str):
    try:
        pwd = pwd.strip()
        with ZipFile(file=path, mode='r') as archive:
            archive.extractall('extracted_archive', pwd=bytes(pwd, 'utf-8'))
        return True
    except Exception as e:
        # print(f'{pwd}')
        return None
