jumlah = 0
total = 0
terjauh = 0
total_jarak = 0

jarak = int(input("Masukkan jarak (km), 0 untuk selesai: " ))
while jarak != 0:
    if jarak < 0:
        print("Jarak tidak valid, ulangi!: ")
    else:
        jumlah +=1

        if jarak <= 5:
            tarif = 3000
        elif jarak <= 15:
            tarif = 3000 + (jarak - 5) * 1000
        else:
            tarif = 13000 + (jarak - 15) * 500

        if jumlah % 5 == 0:
            tarif = tarif // 2

        total += tarif
        total_jarak += jarak
        if jarak > terjauh:
            terjauh = jarak

    jarak = int(input("Masukkan jarak (km), 0 untuk selesai: " ))
print("jumlah penumpang: ", jumlah)
print("Total pendapatan: Rp", total)
print("Jarak terjauh: ",terjauh, "km" )
if jumlah > 0:
    print("Rata-rata jarak: ", total_jarak // jumlah, "km")