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