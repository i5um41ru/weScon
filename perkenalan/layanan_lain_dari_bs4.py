# Namas asli berkas : perkenalan_dengan_bs4.py
# Penulis           : Ismail Sudirman
# Alamat surel      : ismailsudirman83@gmail.com
# Web               : www.skeffo.com
# Berkas dibuat     : 09 November 2016

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

lokasi_url  = urlopen('http://i5um41ru.wordpress.com')
objek_bs    = bs(lokasi_url)

daftarHasil = objek_bs.findAll('span') # objs.findAll('span', {'class':'red'})
for hasil in daftarHasil:
  print(hasil.get_text())
