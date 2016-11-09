# Dokumentasi kecil tentang BeautifulSoup4
Contoh dasar penggunaan *bs4* adalah sebagai berikut:

```python
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

lokasi_url = urlopen('http://wikipedia.org')
objek_bs = bs(lokasi_url, 'html')
for teks in objek_bs.findAll('span', {'class': 'other-project-title'}):
    print(x.get_text())
```

## find() dan findAll() pada BeautifulSoup
`find()` dan `findAll()` merupakan dua fungsi yang mungkin akan paling sering
Anda gunakan nantinya.

```python
findAll(tag, attributes, recursive, text, limit, kwargs)
find(tag, attributes, recursive, text, kwargs)
```
95% yang paling sering mungkin Anda gunakan adalah dua argumen pertama dari
fungsi diatas: `tag` dan `attributes`.

```python
.findAll({"h1", "h2", "h3", "h4", "h5", "h6"})
```
Kode diatas akan menghasilkan daftar (*list*) untuk semua *tag header* pada
dokumen.

```python
.findAll("span", {"class": "hijau", "class": "merah"})
```
Kode diatas menemukan semua elemen `span` yang memiliki *class* hijau maupun
merah dan menyimpannya dalam bentuk daftar (*list*).

Argumen *recursive* bernilai *boolean* (hanya dapat bernilai benar/salah
(*True/False*)). Jika *recursive* bernilai *True* maka fungsi *findAll()*
akan melihat ke dalam setiap anak elemen dst untuk setiap `tag` yang sesuai dengan
parameter yang Anda berikan. 

Untuk argumen *text* itu mencari elemen konten teks dari *tags* yang
diinginkan, bukan dari properti *tags* tersebut. Berikut contoh penggunaannya:

```python
daftarTemuan = objek_bs.findAll(text='pandawa lima')
print(len(daftarTemua))
```

Argumen *limit* sendiri tentunya untuk membatasi jumlah hasil pencarian. Hasil
yang ditemukan tentunya merupakan temuan pertama dari fungsi *findAll()*,
bukan berdasarkan sesuai keinginan Anda.

Argumen *kwarg/keyword arguments* memungkinkan Anda untuk memilih *tag* yang
memiliki atribute spesifik. Berikut contohnya:

```python
semuaTeks = objek_bs.findAll(id="teks")
print(semuaTeks[0].get_text())

# kedua baris berikut serupa
objek_bs.findAll(id="teks")
objek_bs.findAll("", {"id": "teks"})
```

Harap diperhatikan bahwa penggunaan contoh berikut pada *kwarg* akan 
menghasilkan pesan kesalahan kesalahan karena `class` merupakan fungsi bawaan
pada Python:

```python
objek_bs.findAll(class="hijau") # Kesalahan!
```

Gunakan opsi kikuk berikut:

```python
objek_bs.findAll(class_="hijau")         # atau dapat pula dengan contoh
objek_bs.findAll("", {"class": "hijau'}) # yang satu ini
```

Untuk memilih elemen secara lebih spesifik:

```python
objek_bs.find("table", {"id": "bola"}).tr
```
