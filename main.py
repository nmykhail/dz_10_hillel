#3. Знайти остачу від ділення 121 на 12, і скільки націло поділиться 134 на 7
dz1_3_1 = 121
print("Result 3_1:", dz1_3_1%12)
dz1_3_2 = 134
print("Result 3_2:", dz1_3_2//7)
#4. Обчислити 4 в степені 7
dz1_4 = 4
print("Result 4:", dz1_4**7)
#5. Зробити зріз другої половини довільного списку
dz1_5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Result 5:", dz1_5[len(dz1_5)//2:])
#6. зробити зріз з 4го по 8й елемент списку
dz1_6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print("Result 6:", dz1_6[3:8])
#7. дістати зі списку остатній елемент і помножити його на 10
dz1_7_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
dz1_7_1[-1:] = [10*x for x in dz1_7_1[-1:]]
print("Result 7:", dz1_7_1)
#8. видалити 3й елемент cписка і вивести його на екран
dz1_8_1 = [1, 2, 'tree', 4, 5, 6, 7, 8, 9, 10]
dz1_8_2 = dz1_8_1.pop(2)
print("Result 8:", dz1_8_2)
#9. добавити в середину списку новий елемент зі значенням 100
dz1_9_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dz1_9_1.insert(int(len(dz1_9_1)/2),100)
print("Result 9:", dz1_9_1)

#1. a = "10", b = "15", a i b це строки, обчислити b/a.
a = "10"
b = "15"
a1 = int(a)
b1 = int(b)
d = b1/a1
print("Result_1:", d)

#2. Створити словник в якому вказати основні дані про себе, словник має містить ключі значенням якого
#є інший словник, а також масив.
student = {
    "name": "Misha",
    "surname": "Nosach",
    "adress": {
        "country": "Ukraine",
        "city": "Kiev",
        "street": {
            "str_name": "Harkovskoe_shose",
            "str_number": ["244"],
            "apartment": ["1"]
        },
    },
    "work": [
        {"work_str": "Polova", "position": "worker"}
    ]
}
print("Result_2: ", student.get("work", {}))

#3. Створити масив з 10 елементів і перетворити його в typle, вивисти зріз перших трьох елементів.
a = ("Hello", 2, 3, 4, 5, 6, 7, 8, 9, 10)
tuple(a)
print("Result_3: ", a[0:3])

#4. a, b - сторони прямокутника, знайти площу прямокутника. Якщо a = b, використати площу квадрата.
a = 23
b = 10

if a == b:
    s = a**2
    print("Result_4_square: ",s)

else:
    s = a * b
    print("Result_4_rectangle: ", s)

#5. Є три числа знайти найменше.
a = 23
b = 11
c = 7
if a < b and a < c:
    print("Result_5-A_min")

elif b < c:
    print("Result_5-B_min")

else:
    print("Result_5-C_min")

#6. Є три числа A, B, C - якщо вони впорядковані по зростанню, то до кожного з них добавити 3
#і вивести їх нові значення, якщо ні то вивести їх протилежне число (помножити на -1).
a = 7
b = 11
c = 18
if a < b and b < c:
    a1 = a + 3
    b1 = b + 3
    c1 = c + 3
    print("Result_6-(+3): ", a1, b1, c1)

else:
    a1 = a * (-1)
    b1 = b * (-1)
    c1 = c * (-1)
    print("Result_6-(*(-1)): ",a1, b1, c1)

#7. Дано три числа. Знайти суму двох найбільших з них.
a = 1
b = 11
c = 13
if a > b and b > c or b > a and a > c:
    s = a + b
    print("Result_7-A&B :", s)

elif b > c and c > a or c > a and b > a:
    s = b + c
    print("Result_7-B&C :", s)

else:
    s = a + c
    print("Result_7-A&C :", s)

#8. Створити невпорядкований список з 10 елементів: знайти найбільший, найменший елемент, а також кількість елементів.
a = [2, 23, 12, 7, 33, 18, 22, 0, 11, 5]

min_element = min(a)
max_element = max(a)
sum = len(a)

print("Result_8-min: ", min_element)
print("Result_8-max: ",max_element)
print("Result_8-sum: ",sum)