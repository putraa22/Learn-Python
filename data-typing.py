age = 24
year = "2000"

# print(type(age))
# print(type(year))

# Dalam Python, tipe data dikelompokkan menjadi dua, yaitu TIPE DATA PRIMITIF  dan TIPE DATA COLLECTION
'''
1. Tipe Data Primitif
Tipe data primitif merupakan jenis paling dasar dalam pemrograman. Tipe data ini menyimpan single value. Berikut adalah berbagai tipe data primitif.
 - Numbers
 Integer, Float, Complex.

Tipe data primitif pertama, yakni numbers adalah tipe data angka berupa bilangan bulat, riil, dan kompleks.

Tipe data integer merupakan bilangan bulat positif atau negatif dan tidak memiliki angka desimal. Selanjutnya, tipe data float merupakan bilangan riil yang mewakili bilangan bulat dan angka desimal. Terakhir, tipe data complex yang merupakan representasi dari bilangan kompleks dalam matematika. Tipe data complex terdiri dari bilangan riil dan imajiner dengan bentuk “x +yj”, yaitu “x” adalah bilangan riil dan “y” adalah bilangan imajiner. 

Ciri dari bilangan numbers adalah Anda dapat mengoperasikan bilangan tersebut dengan operasi matematika sederhana, seperti pertambahan (+), pengurangan (-), perkalian (*), dan operasi matematika lainnya.

- Boolean (true, false)

Tipe data primitif kedua adalah boolean, yakni tipe data yang hanya bernilai TRUE atau FALSE. Tipe data ini merepresentasikan nilai kebenaran (truth values). Sebenarnya, setiap variabel yang memiliki nilai bisa dievaluasi dan menghasilkan nilai true.

- String
String merupakan karakter yang berurutan. Ketika Anda membuat variabel bernilai string tentu diawali dengan single quote (‘’) atau double quote (“”).

'''


name = 'Putra'
pekerjaan = 'Frontend Developer'
umur = 24

print(f"Hai.. nama saya {name}") # Formatted String
print('Saya seorang %s' % (pekerjaan)) # %-formatting
print("Dan umur saya {}".format(umur))
