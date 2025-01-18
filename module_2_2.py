first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
if first == second == third:
    print(3)  # Все числа равны
elif first == second or first == third or second == third:
    print(2)  # Есть хотя бы 2 равных числа
else:
    print(0)  # Все числа различны