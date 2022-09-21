neo_spisok = list(map(int, input("Введите ко-во эл-тов списка через запятую и нажм-те ввод ").split(",")))
neo_spisok = list(set(neo_spisok))
print(neo_spisok)