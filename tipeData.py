"""
tipe data:
string <
integr <
float <
list
tuple
set
dictionary
"""

variable_integer = 3
variable_float = 1.5
# type() -> mengecek tipe data pada variavble

print(type(variable_integer))
print("tipe data ini adalah", type(variable_float))

# Casting adlah mengubah tipe data ke tipe data yang lain
# str() fungsi untuk mengubah suatu tipe data menjadi tipe data string
# int()
# float()
variable_string = str(variable_integer)
print("tipe data setelah diubah", type(variable_string))

#==========================================
# OPERATOR LOGIKA, -> AND, OR, NOT
# BIASA DIPAKE WAKTU KONDISI

a = 3
b = 3
if a == 3 and b == 3: #-> and itu kedua syarat harus terpenuhi
    print("nilai data sama")

c = 4
d = "string"

if a == 5 or d == "string": #-> or salah satu harus syarat terpenuhi
    print("nilai salah satu syarat terpenuhi")

#========================
# OPERATOR PENUGASAN 
arif = 6
suep = 8

arif += suep # arif = arif + suep / arif = 6 + 8 = 14
suep *= arif # suep = suep * arif / suep = 8 * 14 = 112
print(arif)
print(suep)

"""
+=, -=, *=, /=, %=, >=, <=, !=, >, <
"""

#=======================================
format = f"nilai suep adalah {suep}" #-> f memungkinkan untuk menulis variabel atau melakukan operasi dalam string, namun tidak dianggap string 
tanpaFormat = "nilai suep adalah ", suep
print(format)
print(tanpaFormat)

upper = "{:30}".format("ini adalah format") # "{:30}" -> digunakan sebagai template string, isi template diletakkan dala fungsi format()
print(upper)
print(len(upper))
print(type(upper))

#=====================
rataKanan = "|{:>30}|".format("ini adalah format") #-> mengatur isi template menjadi rata kiri
rataKiri = "|{:<30}|".format("ini adalah format") #-> mengatur isi template menjadi rata atas
rataTengah = "|{:^30}|".format("ini adalah format") #-> mengatur isi template menjadi rata tengah
maksimal = "|{:.30}|".format("ini adalah format teks python dalam vscode") #-> mengatur isi template hanya memiliki maksimal panjang karakter 30, jika karakter melebihi template, maka karakter yang diluar panjang 30 tidak akan ditulis
print(rataKanan)
print(rataKiri)
print(rataTengah)
print(maksimal)
