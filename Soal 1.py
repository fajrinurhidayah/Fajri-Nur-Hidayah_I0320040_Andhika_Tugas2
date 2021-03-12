#menghitung luas persegi panjang
print("Menghitung luas persegi panjang")
Panjang = float(input("Masukkan nilai panjang: "))
Lebar = float(input("Masukkan nilai lebar: "))
luas_persegi_panjang = Panjang * Lebar
print("Luas persegi panjang adalah: ", luas_persegi_panjang)

#menghitung luas lingkaran
print("Menghitung luas lingkaran")
r = float(input("Masukkan jari-jari lingkaran: "))
luas_lingkaran = 3.14 * (r ** 2)
print("Luas lingkaran adalah: ", luas_lingkaran)

#menghitung luas kubus
print("Menghitung luas permukaan kubus")
panjang_sisi = float(input("Masukkan panjang sisi kubus: "))
luas_permukaan_kubus = 6 * (panjang_sisi ** 2)
print("Luas permukaan kubus adalah: ", luas_permukaan_kubus)

#mengkonversi suhu celcius ke fahrenheit
print("Mengkonversi suhu celcius ke fahrenheit")
C = float(input("Masukkan suhu dalam celcius: "))
C_F = (9 * C / 5) + 32
print("Suhu dalam fahrenheit: ", C_F)

#mengkonversi suhu reamur ke kelvin
print("Mengkonversi suhu reamur ke kelvin")
R = float(input("Masukkan suhu dalam reamur: "))
R_K = (5 * R / 4) + 273
print("Suhu dalan kelvin: ", R_K)


