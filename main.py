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


