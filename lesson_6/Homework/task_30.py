# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: a
# n
#  = a1
#  + (n-1) * d


def arif_progress(first_num, different, count_elem):
    for elem in range(count_elem + 1):
        print(first_num + (elem-1) * different)
arif_progress(7, 2, 5)

    