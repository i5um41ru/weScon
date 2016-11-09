# Namas asli berkas : berurusan_dengan_children.py
# Penulis           : Ismail Sudirman
# Alamat surel      : ismailsudirman83@gmail.com
# Web               : www.skeffo.com
# Berkas dibuat     : 09 November 2016

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

lokasi_url = urlopen('http://www.pythonscraping.com/pages/page3.html')
objek_bs   = bs(lokasi_url, 'html')

for anak in objek_bs.find("table", {"id": "giftList"}).children:
    print(anak)
