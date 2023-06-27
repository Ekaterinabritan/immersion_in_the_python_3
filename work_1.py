#Задача 1
# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
my_list = [1, 2, 3, 1, 2, 4, 5]
sort_list = filter(lambda x: my_list.count(x) > 1, my_list)
sort_list = list(set(sort_list))
print(sort_list)