#Dasar Dasar Pemrograman Pertemuan 6 - Pengenalan Bahasa Pemrograman Python
#Latihan 3 - Konversi Suhu

#Kode Program Konversi Suhu
celcius = float(input("Masukkan suhu dalam Celsius: "))

# Konversi suhu ke Fahrenheit dan Kelvin
fahrenheit = (celcius * 9/5) + 32
kelvin = celcius + 273.15

# Menampilkan hasil konversi
print(f"Suhu dalam Fahrenheit: {fahrenheit} °F")
print(f"Suhu dalam Kelvin: {kelvin} K")