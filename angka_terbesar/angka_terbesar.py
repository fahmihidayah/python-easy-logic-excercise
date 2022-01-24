
max_number = 0
input_str = ''
while input_str != 'x':
    input_str = input('masukkan angka : ')
    if input_str != 'x' and max_number < int(input_str):
        max_number = int(input_str)


print('angka terbesar ' + str(max_number))