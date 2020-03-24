import shelve
import uuid
import os
import io


class Person:
    def __init__(self):
        self.data = shelve.open('mydata.dat')

    def List_isi(self):
        list = os.listdir("File Server")
        arr = []
        for namafile in list:
            arr.append(namafile)
        return arr

    def Upload_isi(self,nama=None,data=None):
        file_simpan=open("File Server/"+nama, "wb")
        file_simpan.write(data)
        file_simpan.close()
        return True

    def Download_isi(self,nama=None):
        if os.path.isfile("File Server/"+nama):
            file_punya = open("File Server/"+nama, "rb")
            data=file_punya.read()
            file_punya.close()
        else:
            data=b'File gaada'
        return data

if __name__=='__main__':
    p = Person()
