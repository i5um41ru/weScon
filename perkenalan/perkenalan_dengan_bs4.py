# Namas asli berkas : perkenalan_dengan_bs4.py
# Penulis           : Ismail Sudirman
# Alamat surel      : ismailsudirman83@gmail.com
# Web               : www.skeffo.com
# Berkas dibuat     : 09 November 2016

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
lokasi_url = urlopen('https://github.com')
objek_bs   = bs(lokasi_url.read())
print(objek_bs.h1.text) # keluaran 'How people build software'
