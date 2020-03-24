from person import Person
import json
import logging

'''
PROTOCOL FORMAT

string terbagi menjadi 2 bagian, dipisahkan oleh spasi
COMMAND spasi PARAMETER spasi PARAMETER ...

FITUR

- create : untuk membuat record
  request : create
  parameter : nama spasi notelpon
  response : berhasil -> ok
             gagal -> error

- delete : untuk menghapus record
  request: delete
  parameter : id
  response: berhasil -> OK
            gagal -> ERROR

- list : untuk melihat daftar record
  request: list
  parameter: tidak ada
  response: daftar record person yang ada

- get : untuk mencari record berdasar nama
  request: get 
  parameter: nama yang dicari
  response: record yang dicari dalam bentuk json format

- jika command tidak dikenali akan merespon dengan ERRCMD

'''
p = Person()

class PersonMachine:
    def proses(self,string_to_process, data):
        s = string_to_process
        cstring = s.split(" ")
        try:
            command = cstring[0].strip()
            if (command=='upload'):
                logging.warning("create")
                nama = cstring[1].strip()
                p.Upload_isi(nama,data)
                return "OK"

            elif (command=='download'):
                logging.warning("get")
                nama = cstring[1].strip()
                hasil = p.Download_isi(nama)
                return hasil

            elif (command=='list'):
                logging.warning("list")
                hasil = p.List_isi()
                hasil={"file":hasil}
                return json.dumps(hasil)

            else:
                return "ERRCMD"
        except:
            return "ERROR"


if __name__=='__main__':
    pm = PersonMachine()
    hasil = pm.proses("aaa.txt", "null")
    print(hasil)