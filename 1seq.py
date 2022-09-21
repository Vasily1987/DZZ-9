neo_spisok =[]
N = int(input('Введите количество элементов списка: '))
for i in range(N):
    neo_spisok.append(input('Введите элемент списка  : '))

neo_spisok.sort()
print(neo_spisok)
