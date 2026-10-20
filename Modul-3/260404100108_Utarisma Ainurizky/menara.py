#menara
n = int(input("Masukkan tinggi setengah menara (2-15): "))
while n < 2 or n > 15:
    n = int(input("Di luar rentang, Ulangi (2-15): "))
for baris in range(1, 2 * n):
    if baris <= n:
        b = baris
    else:
        b = 2 * n - baris
    print(" " * (2 * (n - b)), end=" ")
    for i in range(1, b + 1):
        print(i % 10, end=" ")
    for i in range(b - 1, 0, -1):
        print(i % 10, end=" ")
    print()