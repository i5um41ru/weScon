# Namas asli berkas : berurusan_dengan_parents.py
# Penulis           : Ismail Sudirman
# Alamat surel      : ismailsudirman83@gmail.com
# Web               : www.skeffo.com
# Berkas dibuat     : 09 November 2016

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

lokasi_url = urlopen('http://pythonscraping.com/pages/page3.html')
objek_bs   = bs(lokasi_url)

print(objek_bs.find("img", {"src": "../img/gifts/img1.jpg"
                           }).parent.previous_sibling.get_text())
