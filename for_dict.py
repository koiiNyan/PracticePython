# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
# ???

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

counter = {}

for row in students:
    counter.setdefault(row['first_name'], 0)
    counter[row['first_name']] += 1

print(counter)


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
# ???

# Пример вывода:
# Самое частое имя среди учеников: Маша
counter = {}
for row in students:
  counter.setdefault(row['first_name'], 0)
  counter[row['first_name']] += 1


max_key = max(counter, key =lambda k: counter[k])
print("Самое частое имя среди учеников: {}".format(max_key))


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
# ???

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша
counter = {}
for row in school_students[0:][0:]:
  for row in school_students[0:]:
    counter.setdefault(row[0]['first_name'], 0)
    counter[row[0]['first_name']] += 1
print(counter.keys())


