a = 0
b = 0
c = 0
d = 0
e = 0
total_akhir = 0
tinggi = -1
rendah = 101

for i in range(3):
    print("Mahasiswa ke-", i + 1)
    nama = (input("Masukkan nama: "))
    tugas = int(input("Masukkan nilai tugas: "))
    UTS = int(input("Masukkan nilai UTS: "))
    UAS = int(input("Masukkan nilai UAS: "))

    akhir = tugas * 0.3 + UTS * 0.3 + UAS * 0.4
    akhir = int(akhir)

    if akhir >= 85:
        Kategori = "A"
        a += 1
    elif akhir >= 75:
        Kategori = "B"
        b += 1
    elif akhir >= 65:
        Kategori = "C"
        c += 1
    elif akhir >= 50:
        Kategori = "D"
        d +=1
    else:
        Kategori = "E"
        e +=1

    print(nama, tugas, UTS, UAS, akhir, Kategori)
    total_akhir += akhir

    if akhir > tinggi:
        tinggi = akhir
        nama_tinggi = nama
    if akhir < rendah:
        rendah = akhir
        nama_rendah = nama

print("A:", a, "B:", b, "C:", c, "D:", d, "E:", e)
print("Tertinggi:", tinggi, nama_tinggi)
print("Terendah:", rendah, nama_rendah)
print("Rata-rata", total_akhir / 10)