import threading
import logging
import requests
import datetime
import os

def download_gambar(url=None):
    if (url is None):
        return False

    ff = requests.get(url)
    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/jpeg']='jpg'

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = os.path.basename(url)
        ekstensi = tipe[content_type]
        logging.warning(f"writing {namafile}.{ekstensi}")
        fp = open(f"{namafile}.{ekstensi}","wb")
        fp.write(ff.content)
        fp.close()
    else:
        return False

if __name__=='__main__':

    multi_threads = []
    url1 = 'https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__340.jpg'
    url2 = 'https://cdn.pixabay.com/photo/2018/11/14/20/50/hd-3816045_960_720.jpg'
    g1 = threading.Thread(target=download_gambar, args=(url1,))
    multi_threads.append(g1)
    g2 = threading.Thread(target=download_gambar, args=(url2,))
    multi_threads.append(g2)

    for i in multi_threads:
        i.start()
