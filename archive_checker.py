import os
from zipfile import BadZipFile, ZipFile, is_zipfile


def check_archive(path: str):
    """
    Checks path from given input if the file exists and if the file is a zip
    :param path:    file path
    :return: None
    """
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
    """
    Checks if given string password can be used to open (extract) given zip to 'extracted_archive' directory. If zip
    cannot be extracted, then function throws ZIP Exception
    :param path: Path to Zip File
    :param pwd: String Password
    :return: True is password was correct, None otherwise
    """
    try:
        pwd = pwd.strip()
        with ZipFile(file=path, mode='r') as archive:
            archive.extractall('files/extracted_archive', pwd=bytes(pwd, 'utf-8'))
        return True
    except Exception as e:
        # print(f'{pwd}')
        return None
