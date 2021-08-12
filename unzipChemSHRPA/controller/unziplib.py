import os

import hashlib


def add_extension_zip(filepath: str) -> str:
    """ 拡張子zipを追加する """
    return filepath + ".zip"


def get_hash_md5(filepath: str) -> str:
    """ ファイルのハッシュ値を取得 """
    # ファイル を バイナリーモード で開く
    with open(filepath, 'rb') as file:
        # ファイルを読み取る
        fileData = file.read()
        # ハッシュ値-md5の取得
        hash_md5 = hashlib.md5(fileData).hexdigest()
        return hash_md5


def rename_chemSHRPA2zip(pre_file_path: str):
    """ ファイル.shai を ハッシュ.zip にリネームする """
    PAIRENT_DIR = os.path.dirname(os.path.abspath(pre_file_path))
    # ハッシュ.zip
    rename = get_hash_md5(filepath)
    rename = add_extension_zip(rename)
    rename_file_path = os.path.join(PAIRENT_DIR, rename)
    try:
        os.rename(pre_file_path, rename_file_path)
    except FileNotFoundError as exc:
        print(pre_file_path, "がありません")
    except FileExistsError as exc:
        print(rename, "がすでにあります")


if __name__ == '__main__':
    filepath = r"C:\Users\IR-001\PycharmProjects\chemSHRPA_Search\unzipChemSHRPA\1043451-01.shai"
    rename_chemSHRPA2zip(filepath)
