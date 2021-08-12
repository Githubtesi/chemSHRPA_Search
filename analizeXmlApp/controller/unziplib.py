import zipfile





def unzip_file(filepath:str):
    """ zipファイルの解凍 """
    with zipfile.ZipFile(r"C:\Users\IR-001\PycharmProjects\chemSHRPA_Search\analizeXmlApp\controller\Constants.zip","r") as z:

        #01 extract all files
        z.extractall("")

        # 解凍後にできるデータ一覧。
        names =  z.namelist()

        #02 extract one file
        # with z.open("test_dir/test.txt") as f:
        #     print(f.read())
