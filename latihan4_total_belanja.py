#Dasar Dasar Pemrograman Pertemuan 6 - Pengenalan Bahasa Pemrograman Python
#Latihan 4 - Total Belanja

#Kode Program Total Belanja
nama_barang = input("Masukkan nama barang: ")
harga_barang = float(input("Masukkan harga barang: "))
jumlah_barang = int(input("Masukkan jumlah barang: "))

# Menghitung subtotal, PPN, dan total pembayaran
subtotal = harga_barang * jumlah_barang
ppn = subtotal * 0.11
total_pembayaran = subtotal + ppn

# Menampilkan hasil perhitungan
print(f"Nama Barang: {nama_barang}")
print(f"subtotal: {subtotal}")
print(f"PPN (11%): {ppn}")
print(f"Total Pembayaran: {total_pembayaran}")