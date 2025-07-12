lista = [5, 7, 'a', 'b', 'c', 'd', 33, 22, 14]
print(lista[2: 8: 1])  #  a', 'b', 'c', 'd', 33, 22
print(lista[:3:-1])    #5, 7, 'a
print(lista[::-1])     #  5, 7, 'a', 'b', 'c', 'd', 33, 22, 14
print(lista[-5::-1])   # 5, 7, 'a', 'b', 'c
print(lista[-1::2])    #  14 33 c a 5
print(lista[-7::2])    #  a 5
print(lista[-1:-8:-2]) #  14 33 c a