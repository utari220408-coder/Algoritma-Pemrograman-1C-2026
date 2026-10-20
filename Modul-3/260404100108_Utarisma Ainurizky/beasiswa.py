penuh = 0

for i in range(10):
    print("Mahasiswa ke-", i + 1)
    nama = ("Nama: ")
    ipk = float(input("Masukkan ipk: "))
    gaji = int(input("Masukkan penghasilan orang tua per bulan: "))

    if ipk < 3.00:
        print(nama, "Tidak memenuhi syarat IPK")
        continue
    if gaji <= 3000000:
        print(nama, "Beasiswa penuh")
        penuh += 1
    elif gaji <= 5000000:
        print(nama, "Beasiswa sebagian")
    else:
        print(nama, "Tidak mendapat beasiswa")

    if penuh == 3:
        print("Kuota beasiswa penuh (3) sudah terpenuhi, seleksi dihentikan")
        break
print("Jumlah penerima beasiswa penuh: ", penuh)