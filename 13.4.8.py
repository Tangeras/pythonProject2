# try:
#     str_1=int(input("Строка 1"))
#     str_2=int(input("Строка 2"))
#     str_3=int(input("Строка 3"))
# except ValueError as error:
#     print("Вы ввели совсем не число" )
# else:
#     print("Вы ввели числа:", str_1, str_2,str_3)
# finally:
#     print("выход из программы")

# A=input('A')
# B=input('B')
# if A % 2 == 1 and B % 2 == 1:
#     print('Числа А и B нечетные')

# if x > 0 and y > 0:                 # x > 0, y > 0
#          print("Первая четверть")
# if x > 0 and y < 0:                 # x > 0, y < 0
#          print("Четвертая четверть")
# if y > 0 and x < 0:                 # x < 0, y > 0
#          print("Вторая четверть")
# if y < 0 and x < 0:                 # x < 0, y < 0
#          print("Третья четверть")
#
# month=int(input("Введите номер месяца"))
# if month in [12,1,2]:
#     print("Зимушка-зима")
# elif month in [3,4,5]:
#     print("Весна пришла!")
# elif month in [6, 7, 8]:
#     print("Ура, лето!")
# elif month in [9, 10, 11]:
#     print("Вот и осень")

# A = int(input('Введите первое число\n'))
# # B = int(input('Введите второе число\n'))
# # C = int(input('Введите третье число\n'))
# #
# # if ((A < 45) and (B >= 45) and (C >=45)) or \
# #     ((A >= 45) and (B < 45) and (C >=45)) or \
# #     ((A >= 45) and (B >= 45) and (C < 45)):
# #     print('Есть число меньше 45 и только одно')
# # else:
# #     print('Числа меньше 45 нет или их несколько')
#
# A=int(input("Введите двузначное число"))
# if A%5==0 or 10<=A//5<=11:
#    print("В составе числа есть 5")
# else: print("В составе числа нет 5")

# n = 15
# first_digit = A // 10
# second_digit = A % 10
#
# print((first_digit == 5) or (second_digit == 5))

# A=list(input("Введите числа без пробелов"))
# print(A)
# if len(set(A))==len(A):
#     print("Все числа уникальные")
# else:
#     print("числа повторяются")

# A=input("Введите восьмизначное число")
# print(str(A) == str(A)[::-1])
# if A[0]==A[7] and A[1]==A[6] and A[2]==A[5] and A[3]==A[4]:
#    print("Это число - палиндром!")
# else:
#     print("Просто число")

# P = 1  # заводим переменную-счетчик, в которой мы будем считать произведение
# N = 5
#
# # заводим цикл for, в котором мы будем проходить по всем числам от одного до N
# for i in range(1, N + 1):  # равносильно выражению for i in [1, 2, 3, ... , N -1, N]:
#     print("Значение произведения на предыдущем шаге: ", P)
#     print("Текущее число: ", i)
#     P = P * i  # cуммируем текущее число i и перезаписываем значение суммы
#     print("Значение суммы после умножения: ", P)
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ: произведение равнo = ",P)

# n=5
# for i in range(1, n + 1):
#     print("*" *i)
# n=1
# while True:
# if n ** 2 >= 1000:
#        print("Последнее число", n - 1)
#        break
#    n += 1
# while True:  # в данной программе это условие всегда True, цикл будет бесконечным
#    print("Hello World")
#    n += 1
#    if n > 10:  # условие, при достижении которого цикл while будет принудительно завершен
#        break
# P = 1  # заводим переменную-счетчик, в которой мы будем считать произведение
# N = 5


# запишите цикл for для подсчета произведения
# for i in range(1, N+1):
#     P *= i # P=P*i
#
# print(P)

# random_matrix = [
#     [9, 2, 1],
#     [2, 5, 3],
#     [4, 8, 5]
# ]
#
# min_value_rows = []  # здесь будут храниться минимальные значения для каждой строки
# min_index_rows = []  # здесь будут храниться индексы минимальных значений для каждой строки
# max_value_rows = []  # здесь будут храниться максимальные значения для каждой строки
# max_index_rows = []  # здесь будут храниться индексы максимальных значений для каждой строки
#
# for row in random_matrix:  # здесь мы целиком берем каждую сроку
#     min_index = 0  # в качестве минимального значения возьмем первый элемент строки
#     max_index = 0
#     min_value = row[min_index]  # начальное минимальное значение для каждой строки будет новое
#     max_value = row[max_index]  # для максимального значения тоже самое
#     for index_col in range(len(row)):
#         if row[index_col] < min_value:
#             min_value = row[index_col]
#             min_index = index_col
#         if row[index_col] > max_value:
#             max_value = row[index_col]
#             max_index = index_col
#     min_value_rows.append(min_value)
#     min_index_rows.append(min_index)
#     max_value_rows.append(max_value)
#     max_index_rows.append(max_index)
#
# print(min_value_rows)
# print(min_index_rows)
# print(max_value_rows)
# print(max_index_rows)
#
# list_ = [-5, 2, 4, 8, 12, -7, 5]
# # Объявим переменную, в которой будем хранить индекс отрицательного элемента
# index_negative = 0
#
# for i, value in enumerate(list_):
#     if value < 0:
#         print("Отрицательное число: ", list_[i])
#         index_negative=i
#     else:
#         print("Положительное число: ", list_[i])
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ: индекс последнего отрицательного элемента = ", index_negative)
#
# text = """
# У лукоморья дуб зелёный;
# Златая цепь на дубе том:
# И днём и ночью кот учёный
# Всё ходит по цепи кругом;
# Идёт направо -- песнь заводит,
# Налево -- сказку говорит.
# Там чудеса: там леший бродит,
# Русалка на ветвях сидит;
# Там на неведомых дорожках
# Следы невиданных зверей;
# Избушка там на курьих ножках
# Стоит без окон, без дверей;
# Там лес и дол видений полны;
# Там о заре прихлынут волны
# На брег песчаный и пустой,
# И тридцать витязей прекрасных
# Чредой из вод выходят ясных,
# И с ними дядька их морской;
# Там королевич мимоходом
# Пленяет грозного царя;
# Там в облаках перед народом
# Через леса, через моря
# Колдун несёт богатыря;
# В темнице там царевна тужит,
# А бурый волк ей верно служит;
# Там ступа с Бабою Ягой
# Идёт, бредёт сама собой,
# Там царь Кащей над златом чахнет;
# Там русский дух... там Русью пахнет!
# И там я был, и мёд я пил;
# У моря видел дуб зелёный;
# Под ним сидел, и кот учёный
# Свои мне сказки говорил.
# """
#
# text = text.lower()
# text = text.replace(" ", "")
# text = text.replace("\n", "")
# print(text)
# while True:
#     if n % 3 == 0:
#          n = n // 3
#          if n == 1:
#               break
#     else:
#          break
#
# n=int(input("Введите число"))
# def check_h(n):
#     while n > 1:
#      if n%2==0:
#        return n/2
#      else:
#        return (n*3+1)/2
# if n == 1:
#       return True
# else:
#       return False
# Вебинар Условные выражения
# letter=input('Введите букву латинского алфавита')
# if letter=='e'or  letter=='i' or letter=='a' or letter=='o'or letter=='u':
#     print ('гласная буква')
# elif letter=='y':
#     print('гласная и согласная буква')
# else:
#     print('согласная буква')
# num = int(input())
# for i in range(num):
#     num = int(input())
#     maxs = 0
#     if num % 5 == 0 and num > maxs:
#         maxs=i
# print(maxs)

# def sum_(n):
#     if n == 1:
#         return 1
#     return n + sum_(n-1)
#
# rec_sum=sum_(50)
# print(rec_sum)  # 55
# def text_reverse(string):
#     if len(string) == 0:
#         return '  '
#     else:
#         return string[-1] + text_reverse(string[:-1])
#
# text=text_reverse('string')
# print(text)
# def sum_digit(n):
#    if n < 10:
#        return n
#    else:
#        return n % 10 + sum_digit(n // 10)

# print(sum_digit(9))  # 6
# def count(start=1, step=1):
#     counter = start
#     while True:
#         yield counter
#         counter += step
#         print(count())

# def repeat_list(list_):
#    list_values = list_.copy()
#    print(list_values)
#    while True:
#        value = list_values.pop(0)
#        list_values.append(value)
#        yield value
#
# for i in repeat_list([1, 2, 3]):
#    print(i)
# str_ = "my tst"
# str_iter = iter(str_)
#
# print(type(str_))  # строка
# print(type(str_iter))  # итератор строки
#
# print(next(str_iter))  # m
#
# # Получим ещё несколько элементов последовательности
# print(next(str_iter))  # y
# print(next(str_iter))  #
# print(next(str_iter))  # t
# print(next(str_iter))  # s
# print(next(str_iter))  # t

# def decorator_time(fn):
#    def wrapper():
#        t0 = time.time()
#        result = fn()
#        dt = time.time() - t0
#        return dt
#    return wrapper


# def pow_2():
#    return 10000000 ** 2
#

# def in_build_pow():
#    return pow(10000000, 2)


# pow_2 = decorator_time(pow_2)
# in_build_pow = decorator_time(in_build_pow)
#
# mean_pow_2 = 0
# mean_in_build_pow = 0
# for _ in range(N):
#    mean_pow_2 += pow_2()
#    mean_in_build_pow += in_build_pow()
#
# print(f"Функция {pow_2} выполнялась {N} раз. Среднее время: {mean_pow_2 / N:.10f}")
# print(f"Функция {in_build_pow} выполнялась {N} раз. Среднее время: {mean_in_build_pow / 100:.10f}")

# def counter(fn):# оборачиваемая функция
#     print("Этот код будет выведен один раз в момент декорирования функции")
#     count=0
#     def wrapper(*args, **kwargs):
#         nonlocal count
#         print('Этот код будет выполняться перед каждым вызовом функции')
#         fn(*args, **kwargs)
#         count+=1
#         print('Этот код будет выполняться после каждого вызова функции')
#         print(f"Функция {fn} была вызвана {count} раз")
#     return wrapper
# @counter
# def say_word(word):
#    print(word)
#
# say_word("Oo!!!")
# # Oo!!!
# # Функция <function say_word at 0x7f93836d47b8> была вызвана 1 раз
#
# say_word("Oo!!!")
# Oo!!!
# Функция <function say_word at 0x7f93836d47b8> была вызвана 2 раз
# say_word("Ух ты!!!")
# def a_decorator_passing_arguments(function_to_decorate):
#     def a_wrapper_accepting_arguments(arg1, arg2):
#          print("Смотри, что я получил:", arg1, arg2)
#          function_to_decorate(arg1, arg2)
#     return a_wrapper_accepting_arguments
#
#  # Теперь, когда мы вызываем функцию, которую возвращает декоратор, мы вызываем её "обёртку",
#  # передаём ей аргументы и уже в свою очередь она передаёт их декорируемой функции
# @a_decorator_passing_arguments
# def print_full_name(first_name, last_name):
#      print("Меня зовут", first_name, last_name)
# print_full_name("Vasya", "Pupkin")
# dict={}
# def my_decorator(func):
#     dict = {}
#     def wrapper(arg):
#         nonlocal dict
#         if arg not in dict:
#             dict[arg]=func[arg]
#             print(f"Добавление результата в кэш: {dict[arg]}")
#         else:
#             print(f"Возвращение результата из кэша: {dict[arg]}")
#         print(f"Кэш {dict}")
#         return dict[arg]
#     return wrapper
# @my_decorator
#     def f(n):
#     return n * 123456789
# print(n)
# d=None
# def discrim(a, b, c):
#      d=b**2 - 4*a*c
#      print(f"дискриминант равен{d}")
# discrim(2,3,5)

# def quadratic_solve(a,b,c):
#     d=b**2 - 4*a*c
#     if d<0:
#         print( 'нет вещественных корней')
#     elif d==0:
#         result =int( -b/(2*a))
#         print(f'корень уравнения равен{result}')
# quadratic_solve(2,4,2)

# def min_list(L):
#     if len(L) == 1:
#         return L[0]
#     return L[0] if L[0] < min_list(L[1:]) else min_list(L[1:])

# def equal(N, S):
#     if S < 0:
#         return False
#     if N < 10:
#         return N == S
#     else:
#         return equal(N // 10, S - N % 10)
# print(equal(95,9))
# iter_obj = iter("Hello!")
#
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# USERS = ['admin', 'guest', 'director', 'root', 'superstar']
# yesno = input("""Введите Y, если хотите авторизоваться или N,
#              если хотите продолжить работу как анонимный пользователь: """)
#
# auth = yesno == "Y"
#
# def is_auth(func):
#     def wrapper():
#         if auth:
#             username = input("Введите ваш username:")
#             func()
#         else:
#             print("Пользователь неавторизован. Функция выполнена не будет")
#     return wrapper
# def has_access(func):
#     def wrapper():
#         if  username in USERS:
#             print(f"Авторизован как{username}")
#             func()
#         else:
#             print("Пользователь с таким именем не найден")
#     return wrapper
# @is_auth
# @has_access
# def from_db():
#     print("some data from database")
# from_db()
# def even(x):
#     return x % 2==0  # функция возвращает только True или False
#
# result = filter(even, [-2, -1, 0, 1, -3, 2, -3])
#
# # Возвращается итератор, т.е. перечисляйте или приводите к списку
# print(list(result))   # [1, 2]

# data = [
#    (82, 191),
#    (68, 174),
#    (90, 189),
#    (73, 179),
#    (76, 184)
# ]
# result=sorted(data, key = lambda x: x[0] / x[1] ** 2)
# print(result)
# dict={1:"one", 2:"two", 3: "three"}
# a = {item[0]: item[1] * 2 for item in dict.items()}
# print(a)
myfile=open('C:/Users/Татьяна/PycharmProjects/pythonProject2/filename.txt','w')
print(myfile.read)

