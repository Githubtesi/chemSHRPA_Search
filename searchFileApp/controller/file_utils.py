import glob
import os
from typing import List


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


def get_chemSHRPA_list(file_path_list: List[str]) -> List[str]:
    """ chemSHRPAファイルのみ抽出してlistで返す """
    result = []
    for file_path in file_path_list:
        if is_chemSHRPA_data(file_path):
            result.append(file_path)
    return result


def get_files(folderpath: str) -> List[str]:
    """ 指定したフォルダ以下にあるファイルリストを取得 """
    if os.path.isdir(folderpath):
        return glob.glob(folderpath + r"\**", recursive=True)
    else:
        raise FileNotFoundError(folderpath)


if __name__ == "__main__":
    # import doctest

    # doctest.testmod()

    # テスト
    l = get_files(r"\\IRS5\irs5_public\DQS\品証共通フォルダ\環境調査chemSHRPA RoHS2\製品")
    l2 = get_chemSHRPA_list(l)
    for item in l2:
        print(item)
