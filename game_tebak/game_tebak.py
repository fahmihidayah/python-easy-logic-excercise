import random

soal = random.randint(1, 10)
jawaban = -1
while jawaban != soal:
    jawaban_str = input("Tebak angka : ")
    if int(jawaban_str) > soal:
        print('terlalu besar')
    elif int(jawaban_str) < soal:
        print('terlalu kecil')
    else:
        jawaban = int(jawaban_str)

print('selesai')