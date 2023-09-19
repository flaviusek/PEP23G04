# first_number = int(input('give number:'))
#
# if first_number == 10:
#     print('number is 10')
#
# elif first_number == 11:
#     print('number is 11')
#
# else:
#     print('number is other')
#
#
# a = 15
# while a > 0:
#     print(a)
#     a -= 1
# print('Gata')
#
# #
# #
# a = 10
# print(a)
# a = a + 1
# print(a)
# a += 1
# print(a)
#
# while a >= 10:
#       print(a)
#       a -= 2
#
# print('done')


# n = 0
#
# while n < 10:
#     if n == 7:
#         n += 1
#         continue
#     elif n == 8:
#         break
#     print(n)
#     n += 1
#
# print('done')



#
# birth_year = int(input("Introduceti primele 7 cifre din CNP: "))
#
# age = 2023 - birth_year[1,2]
#
# if age >= 18:
#     print("Aveti peste 18 ani.")
# else:
#     print("Nu aveti peste 18 ani.")
#


# curr_year = 2023
# id = input('first 7 nb from ci:')
# # if int(input -= [2000000])
# if len(id) != 7:
#     print('not enough digits.')
# else:
# year = int(id[1:3])
#
# print(year)
# if id[0] < '5':
#     year += 1900
# else:
#     year += 2000
#
# result = curr_year - year
#
# if result >= 18:
#     print("Aveti peste 18 ani.")
# else:
#    print("Nu aveti peste 18 ani.")



# num = int(input("Enter a number: "))
# current_num = 0
#
# while current_num <= num:
#          if current_num % 2 == 0:
#             print(current_num)
#
# current_num += 1

#             print("Invalid input. Please enter a valid number.")

#
# N = int(input('introduceti un numar'))
# n = 0
# while N > 0:
#     print(n)
#
# n += 1
# print(n)

# a = 'abcd'
# if a:
#     print('done')
#
# print(bool('abcd'))
# print(bool('d'))
# # print(bool(''))
#
# print(bool(100))
# print(bool(-100))
# print(bool(0))






capuccino = 4
espresso = 3.5

print("Choose an option:")
print("1. capuccino - 4")
print("2. espresso - 3.5")

option_choice = input('Ce optiune alegeti: (1 or 2): ')


if option_choice not in ['1', '2']:
    print('Invalid option choice. Please select option 1 or 2.')
else:

    option_choice = int(option_choice)

    money_paid = float(input('Introduceti o bacnota: '))

    if option_choice == 1:
        selected_option_price = capuccino
    else:
        selected_option_price = espresso

    rest = money_paid - selected_option_price

    if rest < 0:
        print('Suma incorecta')
    elif rest == 0:
        print('Plata exacta.')
    else:
        print(f'Restul tau este: [rest:, .2f].')



# print(True and True)
# print('x' and True)
# print(True and 'x')
#
