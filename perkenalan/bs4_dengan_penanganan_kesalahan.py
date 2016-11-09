# Namas asli berkas : perkenalan_dengan_bs4.py
# Penulis           : Ismail Sudirman
# Alamat surel      : ismailsudirman83@gmail.com
# Web               : www.skeffo.com
# Berkas dibuat     : 09 November 2016

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup as bs

def gaetJudul(url):
    try:
        lok_url = urlopen(url)
    except HTTPError as e:
        return None
    try:
        obj_bs  = bs(lok_url.read())
        judul   = obj_bs.body.h1.text
    except Attribute.err as e:
        return None
    return judul

judul = gaetJudul('https://github.com')
if judul == None:
    print('Judul tidak ditemukan!')
else:
    print(judul)
