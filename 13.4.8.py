 try
    str_1=int(input("Строка 1"))
    str_2=int(input("Строка 2"))
    str_3=int(input("Строка 3"))
except ValueError as error
 print(error)
else print("Вы ввели числа:", str_1, str_2,str_3)
finally print("выход их программы")
