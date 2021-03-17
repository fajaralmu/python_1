import csv
import http
from urllib.request import urlopen

print("HELLO")


# tentukan lokasi file, nama file, dan inisialisasi csv
# f = urlopen("https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv")
# print(type(f))
local_f = open("D:\Development\Python\learn1\penduduk_gender_head.csv","r")

# data = f.read().decode()
# print((data))

# print(type(data))

reader = csv.reader(local_f)
# csv.reader(f)

# # membaca baris per baris
for row in reader:
     print (row)

# # menutup file csv
local_f.close()