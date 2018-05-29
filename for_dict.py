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

for key, value in counter.items():
  print ("Имя {} повторяется {} раз".format(key, value))


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


for class_num, class_stud in enumerate(school_students, 1):
  names = [name['first_name'] for name in class_stud]
  count_name = {name: names.count(name) for name in names}
  values = list(count_name.values())


  for key, value in count_name.items():
    if value == max(values):
      print("Самое частое имя в классе {}: {}".format(class_num, key))




# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
# ???
# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


for students in school:
  names = [name['first_name'] for name in students['students']]
  gend = {'девочки': 0, 'мальчики': 0}

  for name in names:
    if is_male[name]:
      gend['мальчики'] += 1
    else:
      gend['девочки'] += 1

  print('В классе {} {} девочки и {} мальчики'.format(students['class'], gend['девочки'], gend['мальчики']))


  # Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}, {'first_name': 'Миша'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}, {'first_name': 'Оля'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
# ???

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a


for students in school:
  names = [name['first_name'] for name in students['students']]
  gend = {'девочек': 0, 'мальчиков': 0}

  for name in names:
    if is_male[name]:
      gend['мальчиков'] += 1
    else:
      gend['девочек'] += 1

  gend_v = list(gend.values())


  for key, value in gend.items():
    if value == max(gend_v):
      print("Больше всего {} в классе {}".format(key, students['class']))
    if value == min(gend_v):
      print("Меньше всего {} в классе {}".format(key, students['class']))