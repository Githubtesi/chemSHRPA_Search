import hashlib
import os

"""
shaiファイルの中身抽出関連のパッケージの前に行うファイルパッケージ
"""


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
    """ ファイル.shai を ハッシュ.zip にリネームする
    pre_file_path : 解凍するフォルダ先
    """
    PAIRENT_DIR = os.path.dirname(os.path.abspath(pre_file_path))
    # ハッシュ.zip
    rename = get_hash_md5(pre_file_path)
    rename = add_extension_zip(rename)
    rename_file_path = os.path.join(PAIRENT_DIR, rename)
    try:
        os.rename(pre_file_path, rename_file_path)
    except FileNotFoundError as exc:
        print(pre_file_path, "がありません")
    except FileExistsError as exc:
        print(rename, "がすでにあります")


if __name__ == '__main__':
    filepath = r"C:\Users\yoshiaki\PycharmProjects\chemSHRPA_Search\zipfiles\test44SHAI_Temp_W01065E_20190206162426.shai"
    rename_chemSHRPA2zip(filepath)
