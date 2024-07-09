#name = input('Введите ваше имя: ')
#if name == "Dany":
#    print('Здравствуйте, администратор')
#if name == 'Сергей':
#   print("С тобой не здороваюсь")
#else:
#    print("Привет",name)
first = input("Введите число: "); second = input("Введите число: "); third = input("Введите число: ")

if first == second == third:
    print(3)
elif first==second or first==third or second==third:
    print(2)
else:
    print(0)


