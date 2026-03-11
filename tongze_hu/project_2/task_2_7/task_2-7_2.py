seq = [ "ATATACGCGTA", "CTTCGGNGGA" ]
full_seq = ''
count = 0

for i in seq:
    print(i)

    full_seq += i

    count += 1

    if count == 2:
        print(full_seq)
        print('Цикл выполнен')

