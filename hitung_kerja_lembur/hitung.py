gaji = input('berapa gaji : ')
hari = input('hari : ')
lembur = int(hari) - 20
total = float(gaji) * 20
for i in range(lembur):
    total = total + (float(gaji) + (float(gaji) * (i+1) / 100))

print('total is ' + str(total))