import csv
from random import randint
import xml.dom.minidom as minidom

# Задание 1
with open("books.csv") as r_file:
    freader = csv.reader(r_file, delimiter=";")
    k = 0
    for row in freader:
        if len(list(row)[1]) > 30:
            k += 1
    print(k)

# Задание 2
print('Введите автора')
search = input().lower()
flag = 0
result = set()
with open("books.csv") as r_file:
    freader = csv.reader(r_file, delimiter=";")
    for row in freader:
        if list(row)[4].lower() == search or list(row)[3].lower() == search:
            date = int(list(row)[6][6:10])  # берем из даты только год
            if date >= 2016 and date <= 2018:  # условие варианта 7
                flag = 1
                result.add(row[1])
    if flag == 0:
        print('Ничего не найдено')
    else:
        for book in result:
            print(book)

# Задание 3
with open("books.csv") as r_file:
    freader = csv.reader(r_file, delimiter=";")
    flength = 0
    for row in freader:
        flength += 1  # считаем кол-во строчек
with open("books.csv") as r_file:
    freader = csv.reader(r_file, delimiter=";")
    random_list = [randint(1, flength) for i in range(20)]  # случайные 20 значений
    random_list.sort()
with open("books.csv") as r_file:
    in_use = list(csv.reader(r_file, delimiter=";"))
    with open('result.txt', 'w') as file:
        for i in random_list:
            file.write(str(i) + ' ' + in_use[i][3] + '. ' + in_use[i][1] + ' - ' + in_use[i][6] + '\n')
    file.close()

# Задание 4
xml_file = open('currency.xml', 'r', encoding='utf-8')
xml_data = xml_file.read()
dom = minidom.parseString(xml_data)
dom.normalize()
elements = dom.getElementsByTagName('Valute')
C_Code = []
for node in elements:
    nominal = int(node.getElementsByTagName('Nominal')[0].firstChild.data)
    if nominal == 10 or nominal == 100:
        char_code = node.getElementsByTagName('CharCode')[0].firstChild.data
        C_Code.append(char_code)
print(C_Code)