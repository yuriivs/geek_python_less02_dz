# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

mylist = [1, 5, "hello", {435, 59, "i25"},
          (99, 100, 101), None, [0, 9, 2, 4],
          {"key1": 15, "key2": "ten"}, ]
# i = 0
# while i < len(mylist):
#     print(type(mylist[i]))
#     i += 1

print(list(map(type, mylist)))
