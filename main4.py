# Menulis ke file dengan mode append
# file = open("hello.txt", "w")
# file.write("HELLO")
# file.close()
file = open("hello.txt", "a")
# file.readlines()
file.writelines([
"Sekarang kita belajar menulis dengan menggunakan Python\n", 
"Menulis konten file dengan mode a (append)\n"
])
file.close()

file = open("hello2.txt","w")
file.writelines(["Halo", "Belajar Python", "Menyenangkan!"])
file.close()
file = open("hello2.txt","w")
file.writelines("Menulis ke dalam file")
file.writelines("menggunakan Python")
file = open("hello.txt","r")
for line in file:
    print(line)