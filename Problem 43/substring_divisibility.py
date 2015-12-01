# test_num = 1406357289
multiples_of_17 =[str(i*17).zfill(3) for i in range(1,59) if i*17<999]

multiples_of_13 =[str(i*13).zfill(3) for i in range(1,77) if i*13<999]
multiples_of_11 =[str(i*11).zfill(3) for i in range(1,91) if i*11<999]
multiples_of_7 =[str(i*7).zfill(3) for i in range(1,143) if i*7<999]
# print(multiples_of_7)

for i in multiples_of_17:
    for j in multiples_of_13:
        for k in multiples_of_11:
            for l in multiples_of_7:
                # print(l, k, j, i)
                print(multiples_of_17)
                if i[0:2] == j[1:] and k[1:] == j[0:2] and int(k[0:1])%5==0 and l[1:]==k[0:1]:
                    print(l, k, j, i)