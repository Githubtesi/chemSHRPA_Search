import functools
import glob
import hashlib
import os
from typing import List

import Constants
from searchFileApp.model.models import ChemSHRPA_DATA_PATH
from searchFileApp.view.user_select_file import get_DirPath_with_dialog


def is_shai(file: str) -> bool:
    """　
    shci拡張子ならばTrue
    >>> is_shai("aaa.shai")
    True
    >>> is_shai("aaa.py")
    False
    """
    return True if file.endswith('.shai') else False


def is_shci(file: str) -> bool:
    """ shciファイルならばTrue
    >>> is_shci("aaa.shci")
    True
    >>> is_shci("aaa.py")
    False
    """
    return True if file.endswith('.shci') else False


def is_chemSHRPA_data(file: str) -> bool:
    """ chemSHRPAファイルならばTrue
    >>> is_chemSHRPA_data("aaa.shai")
    True
    >>> is_chemSHRPA_data("aaa.shci")
    True
    """
    return is_shci(file) or is_shai(file)


def filter_chemSHRPA_list(file_path_list: List[str]) -> List[str]:
    """ chemSHRPAファイルのみ抽出してlistで返す """
    result = []
    for file_path in file_path_list:
        if is_chemSHRPA_data(file_path):
            result.append(file_path)
    return result


@functools.lru_cache()
def get_files(folderpath: str) -> List[str]:
    """ 指定したフォルダ以下にあるファイルリストを取得 """
    if os.path.isdir(folderpath):
        return glob.glob(folderpath + r"\**", recursive=True)
    else:
        raise FileNotFoundError(folderpath)


def get_hash_md5(filepath: str) -> str:
    """ ファイルのハッシュ値を取得 """
    # ファイル を バイナリーモード で開く
    with open(filepath, 'rb') as file:
        # ファイルを読み取る
        fileData = file.read()
        # ハッシュ値-md5の取得
        hash_md5 = hashlib.md5(fileData).hexdigest()
        return hash_md5


def test():
    """ Doctest """
    import doctest
    doctest.testmod()


def test_main():
    """ サンプルテスト"""
    target_path = get_DirPath_with_dialog(Constants.CHEMSHRPA_SOURCE)
    l = get_files(target_path)
    l2 = filter_chemSHRPA_list(l)
    result: List[ChemSHRPA_DATA_PATH] = []
    for item in l2:
        result.append(ChemSHRPA_DATA_PATH(item, get_hash_md5(item)))

    import pprint

    pp = pprint.PrettyPrinter(indent=4, width=40)
    pp.pprint(result)


if __name__ == "__main__":
    test_main()
