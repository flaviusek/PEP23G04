# username = input('introduceti username')
#
#
# def validare_parola(password):
#     print(password)
#     result = True
#     if '%' not in password and '!' not in password and '@' not in password:
#         print('parola trebuie sa contina...')
#         result = False
#     for i in range(10):
#         i = str(i)
#
#         if i in password:
#             break
#
#     else:
#         print('parola trebuie sa contina o cifra')
#         result = False
#
#     if len(password) < 7:
#         print('parola trebuie sa contina 7 caractere')
#         result = False
#
#     return result
#
#
# while not validare_parola(input('introduceti parola:')):
#     pass


# 2



number = int(input('insert number or q to quit'))
result = number


def calculate(number):
    global result
    result = result ** number
    print(result)


condition = True
while condition:
    number = input('insert number or q to quit')
    if number == 'q':
        condition = False
        continue

    calculate(int(number))


# 3
