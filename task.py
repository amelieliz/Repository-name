def find_common_participants(group1, group2, separator=","):


    list1 = group1.split(separator)
    list2 = group2.split(separator)


    common = []
    for person in list1:
        if person in list2 and person not in common:
            common.append(person)


    common.sort()

    return common


# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

result = find_common_participants(participants_first_group, participants_second_group, "|")
print("Общие участники:", result)


group1 = "Иванов,Петров,Сидоров"
group2 = "Петров,Сидоров,Смирнов"
result2 = find_common_participants(group1, group2,",")
print("Общие участники:", result2)