import os
import tkinter
import tkinter.filedialog
import Constants


def get_FilePath_with_dialog(folder: str) -> str:
    """
    ファイルダイアログをGUIでファイルを指定する
    :param folder: フォルダ名
    :param targetName: ファイル名 ex)"保存するファイル"
    :return:  フォルダ/ファイル名のパスを返す
    """
    # ファイル選択ダイアログの表示
    root = tkinter.Tk()
    # 小さいウィンドウの非表示
    root.withdraw()
    # ファイルタイプの指定
    fTyp = [("", "*")]
    # 初回ダイアログで開くフォルダの場所
    iDir = os.path.abspath(folder)
    file = tkinter.filedialog.askopenfilename(filetypes=fTyp, initialdir=iDir)
    return file


def get_DirPath_with_dialog(folder: str) -> str:
    """
    ファイルダイアログをGUIでフォルダを指定する
    :param folder: フォルダ名
    :param targetName: ファイル名 ex)"保存するファイル"
    :return:  フォルダ/ファイル名のパスを返す
    """
    # ファイル選択ダイアログの表示
    root = tkinter.Tk()
    # 小さいウィンドウの非表示
    root.withdraw()
    # 初回ダイアログで開くフォルダの場所
    iDir = os.path.abspath(folder)
    dir = tkinter.filedialog.askdirectory(initialdir=iDir)
    return dir


if __name__ == '__main__':
    get_DirPath_with_dialog(Constants.PAIRENT_DIR)
    get_FilePath_with_dialog(Constants.PAIRENT_DIR)
