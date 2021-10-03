import os
import shutil
from typing import List

import Constants
from searchFile_package.controller.file_utils import get_files, get_chemSHRPA_list, is_shai, is_shci
from unzipChemSHRPA_package.controller.unziplib import get_hash_md5, rename_chemSHRPA2zip

"""
各種パッケージの統合
"""


def copy_files(files: List[str], cp_folder=None):
    """
    1.解凍フォルダの指定
    2.再帰検索でshai,shciファイルのパスを検索
    3.dictでフォルダ場所を保持する
    4.ハッシュ値.zipにリネームする
    5.リネームされなかったファイル(同じデータ)を削除
    """

    # 1.解凍先のフォルダ指定
    if cp_folder is None:
        cp_folder = Constants.PAIRENT_DIR + "\zipfiles"

    # 3 "ハッシュファイル名":"フォルダ場所"
    pathes = {}
    for file_path in files:
        # 2.shai,shciファイルの検索->パスを取得
        shutil.copy(file_path, Constants.PAIRENT_DIR + "\zipfiles")

        # ハッシュコードの取得(重複回避のため)
        hash_name = get_hash_md5(file_path)

        # 新規データの場合
        if hash_name not in pathes.keys():
            pathes.update({hash_name: file_path})

        #  重複データがある場合->pathを追加
        else:
            # strをlistに変換
            if type(pathes.get(hash_name)) is str:
                new_path: List[str] = [pathes.get(hash_name), (file_path)]
            # listの追加
            elif type(pathes.get(hash_name)) is List:
                new_path: List[str] = pathes.get(hash_name).append(file_path)
            pathes.update({hash_name: new_path})

    # 4.ファイルをハッシュ値にリネームする
    l = get_files(cp_folder)
    l2 = get_chemSHRPA_list(l)
    print(l2)
    for f in l2:
        print(f)
        rename_chemSHRPA2zip(f)

    # 5.リネームされなかったファイル(同じデータ)を削除
    remove_shai_files(cp_folder)


def remove_shai_files(folderpath: str):
    """
    shai,shci ファイルの削除
    """
    files = get_files(folderpath)
    for file in files:
        if is_shai(file) or is_shci(file):
            os.remove(file)


# テスト
l = get_files(r"C:\Users\yoshiaki\PycharmProjects\search_chemSHRPA\chemSHRPA_Data")
l2 = get_chemSHRPA_list(l)
copy_files(l2, None)
