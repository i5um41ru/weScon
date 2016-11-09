# Namas asli berkas : perkenalan_dengan_bs4.py
# Penulis           : Ismail Sudirman
# Alamat surel      : ismailsudirman83@gmail.com
# Web               : www.skeffo.com
# Berkas dibuat     : 09 November 2016

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

lokasi_url = urlopen('http://pythonscraping.com/pages/page3.html')
objek_bs   = bs(lokasi_url)

for saudara in objek_bs.find("table", {"id": "giftList"}).tr.next_siblings:
    print(saudara)
