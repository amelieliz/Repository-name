numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
for i in range(20):
    if numbers[i] == None:
        where_none = i


summa = 0
for x in numbers:
    if x != None:
        summa += x
numbers[where_none] = summa / 20

# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
