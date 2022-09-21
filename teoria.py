# 1 часть ДЗ теория популярные методы list, dict, set,str:

#Методы list:

#1. Метод Append:
#добавляет элемент в конец списка
z = [7, 4, 3, 2]
z.append(3)
print(z)

#2.Метод sort сортирует и меняет исходный список:

z = [3, 7, 4, 2]
z.sort()
print(z)

#3. Метод extend расширяет список, добавляя элементы.
#Преимущество над append в том, что  можно добавлять списки
z = [7, 3, 3]
z.extend([4,5])
print(z)

#4.Метод index возвращает положение первого индекса, со значением х.
# В указанном ниже коде, он возвращает назад 0.
z = [4, 1, 5, 4, 10, 4]
print(z.index(4))

#5.Метод count работает так, как звучит.
#Он считает количество раз, когда значение появляется в списке.
random_list = [4, 1, 5, 4, 10, 4]
print(random_list.count(4))

#Методы словарей (dict):

#1. Метод keys():
dict_sample = {
  "Company": "Toyota",
  "model": "Premio",
  "year": 2012
}
x = dict_sample.keys()

print(x)

#2. Метод items():
#Этот метод возвращает итерируемый объект. Метод используется, когда нужно перебрать значения словаря.
dict_sample = {
  "Company": "Toyota",
  "model": "Premio",
  "year": 2012
}

for k, v in dict_sample.items():
    print(k, v)

#3.Метод copy()
#Этот метод возвращает копию существующего словаря
dict_sample = {
  "Company": "Toyota",
  "model": "Premio",
  "year": 2012
}
x = dict_sample.copy()

print(x)

#4. Метод len():
#С помощью этого метода можно посчитать количество элементов в словаре

dict_sample = {
  "Company": "Toyota",
  "model": "Premio",
  "year": 2012
}
print(len(dict_sample))

#5. Метод  get(), которой можно пользоваться для доступа к элементам словаря.
dict_sample = {
  "Company": "Toyota",
  "model": "Premio",
  "year": 2012
}
x = dict_sample.get("model")
print(x)

# Методы множеств (set):
# 1 Метод add()
set1 = {1, 3, 4}
set1.add(2)
print(set1)
{1, 2, 3, 4}

#2 Больше одного элемента можно добавить с помощью метода update()

set2 = {1, 2, 3}
set2.update([4, 5, 6])
print(set2)  #  {1, 2, 3, 4, 5, 6}

#3 Метод remove() полезен в тех случаях,
# когда нужно удалить из множества конкретный элемент и вернуть ошибку в том случае, если его нет в объекте.
set1 = {1, 2, 3, 4, 'a', 'p'}
set1.remove(2)
print(set1)
{1, 3, 4, 'a', 'p'}

#set1.remove(5)
# Error element not found


#4. Метод discard() полезен, потому
# что он удаляет конкретный элемент и не возвращает ошибку, если тот не был найден во множестве.

set1 = {1, 3, 4, 'a', 'p'}
set1.discard('a')
print(set1)
# {1, 3, 4 'p'}

set1.discard(6)
print(set1)
# {1, 3, 4, 'p'}

#5. Метод pop() удаляет по одному элементу за раз в случайном порядке.
# Set — это неупорядоченная коллекция, поэтому pop() не требует аргументов (индексов в этом случае).

set1 = {1, 3, 4, 'p'}
set1.pop()
print(set1)

#Методы строк

#1. Метод string.lower() преобразует все буквенные символы в строчные.
alf ='everyTHing yoU Can IMaGine is rEAl'
alf_1 = alf.lower()
print(alf_1 )

#2. Метод string.replace (заменяем данные в строке)
s = 'python'
s = s.replace('h', 't')
print(s)

#3. Метод string.title() преобразует первые буквы всех слов в заглавные.
s = 'the sun also rises'.title()
print(s)

#4. Метод string.upper() преобразует все буквенные символы в заглавные.

b = 'follow us @PYTHON'.upper()
print(b)

#5. Метод string.join(<iterable>) объединяет список в строку.

lst = ', '.join(['foo', 'bar', 'baz', 'qux'])
print(lst)