from dataclasses import dataclass


@dataclass
class ChemSHRPA_DATA_PATH:
    """ ハッシュとファイルパスをまとめるクラス"""
    path: str
    hash: str
