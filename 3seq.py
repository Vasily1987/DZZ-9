neo_spisok_1 = list(map(int, input("Введите ко-во эл-тов 1-го списка через запятую и нажм-те ввод ").split(",")))
neo_spisok_1 = list(set(neo_spisok_1))
neo_spisok_2 = list(map(int, input("Введите ко-во эл-тов 2-го списка через запятую и нажм-те ввод ").split(",")))
neo_spisok_2 = list(set(neo_spisok_2))

neo_spisok_3=[]

for i in neo_spisok_1:
     if i not in neo_spisok_2:
           neo_spisok_3.append(i)

print(neo_spisok_3)
