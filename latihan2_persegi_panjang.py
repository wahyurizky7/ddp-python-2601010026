#Dasar Dasar Pemrograman Pertemuan 6 - Pengenalan Bahasa Pemrograman Python
#Latihan 2 - Persegi Panjang

#Kode Program Persegi Panjang
panjang = float(input("Masukkan panjang (m): "))
lebar = float(input("Masukkan lebar (m): "))

# Menghitung luas dan keliling persegi panjang
luas = panjang * lebar
keliling = 2 * (panjang + lebar)

# Menampilkan hasil perhitungan
print(f"Luas     : {luas} m2")
print(f"Keliling : {keliling} m")


"""
TRACE TABLE PROGRAM (Simulasi Input: panjang = 8, lebar = 5)
# TRACE TABLE:
# Step | panjang | lebar | luas  | keliling
# 1    | 8.0     | -     | -     | -     
# 2    | 8.0     | 5.0   | -     | -     
# 3    | 8.0     | 5.0   | 40.0  | -     
# 4    | 8.0     | 5.0   | 40.0  | 26.0
"""