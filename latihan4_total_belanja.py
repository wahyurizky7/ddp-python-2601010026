nama_barang = input("Masukkan nama barang: ")
harga_barang = float(input("Masukkan harga barang: "))
jumlah_barang = int(input("Masukkan jumlah barang: "))

subtotal = harga_barang * jumlah_barang
ppn = subtotal * 0.11
total_pembayaran = subtotal + ppn

print(f"Nama Barang: {nama_barang}")
print(f"subtotal: {subtotal}")
print(f"PPN (11%): {ppn}")
print(f"Total Pembayaran: {total_pembayaran}")