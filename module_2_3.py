my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0 # начальный индекс
while index < len(my_list):
    number = my_list[index]
    if number < 0: # отрицательное значение
        break # прерывание цикла
    if number > 0: # Выводим положительное число
        print(number)
    index += 1 # Переходим к следующему элементу списка
