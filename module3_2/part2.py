# string1 = "Anxa are mere"
# number1 = 100
# x = False
#
# for char in string1:
#     if char == 'x':
#         print('Am gasit x.')
#         x = True
#         break
#
#
#
# if not x:
#     print("Sirul nu contine x.")
#
# # print(char)
# #
# # print(dir(string1))
# # print(string1)).__iter__())
# # print(dir(number11)).__iter__())
#
# # for number in number1:
# #     print(number)
#
# var1 = string1.__iter__()
# # print(next(var1))
# #
# # string1 = "Anxa are mere"
# #
# # for char in string1:
# #     if char == 'x':
# #         print('Am gasit x.')
# #         x = True
# #         break
# #
# #
# #
# # else:
#     print("Sirul nu contine x.")
#
#
# [11, '2', True, 2.3, '2', 2, 'abc']


# capuccino = 4
# espresso = 3.5
#
# print("Choose an option:")
# print("1. capuccino - 4")
# print("2. espresso - 3.5")
#
# option_choice = input('Ce optiune alegeti: (1 or 2): ')
#
# if option_choice not in ['1', '2']:
#     print('Invalid option choice. Please select option 1 or 2.')
# else:
#
#     option_choice = int(option_choice)
#
#     money_paid = float(input('Introduceti o bacnota: '))



# print('1. Capuccino ...4 lei')
# print('2. Espresso ..3.5 lei')
# choice = input('Ce optiune alefeti? [1,2]: ')
# money = input('Introduceti o bacnota [5,10]:')

# if choice == 1
# if choice not in ['1', '2']:
#     print('Invalid option choice. Please select option 1 or 2.')
# else:
#
#     option_choice = int(option_choice)
#
#     money_paid = float(input('Introduceti o bacnota: '))

# if option_choice not in ['1', '2']:
#     print('Invalid option choice. Please select option 1 or 2.')
#
# else:
#
#     option_choice = int(option_choice)
#
#     money_paid = float(input('Introduceti o bacnota: '))
#
#     if option_choice == 1:
#         selected_option_price = capuccino
#     else:
#         selected_option_price = espresso
#
#     rest = money_paid - selected_option_price
#
#     if rest < 0:
#         print('Suma incorecta')
#     elif rest == 0:
# #         print('Plata exacta.')
# #     else:
# #         print(f'Restul tau este: [rest:, .2f].')
#
#
# # _________________________
# options = [1, 2]
# choices = [4, 3.5]
# currency = [5, 10]
#
#
# print('1. Capuccino ...4 lei')
# print('2. Espresso ..3.5 lei')
# choice = int(input('Ce optiune alegeti? [1,2]: ').strip())
# money = int(input('Introduceti o bacnota [5,10]:').strip())
#
# if money in currency:
#   if choice in options:
#     print(f'Veti primi restul de {money - choices[choice - 1]} lei.')
#
#   else:
#     print('Optiune invalida')
#
# else:
#     print('Bancnota incorecta')
# # _______________________________

#
# parola = '7677'
# incercari = 0
#
# while input('Introduceti parola:') != parola:
#     # print('Parola incorecta')
#     incercari += 1
#     if incercari >= 3:
#         print('Acces restrictionat')
#         break
# else:
#     print('Acces permis')

#___________________
#
# lista = ['Masa', 5, 'Scaun', 4.5, [5, 6, 7], 8]
# for obiect in lista:
#     var_type = str(type(obiect)).split("\'")[1]
#     print(f'tipul obiectului {obiect} este {var_type}')

#_________

# cuvant = input('Introduceti un cuvant:')
#
# prima_litera = cuvant[0]
# numaratoare = cuvant.count(prima_litera)
#
# print(f'{prima_litera} apare de {numaratoare} ori in cuvant')


#___________



# lista = input('Introduceti lista de taskuri:')
# lista_taskuri = lista.split(',')
# print(lista_taskuri)
# result = []
# for element in lista_taskuri:
#     if element not in  result:
#         result.append(element)
#         print(result)




