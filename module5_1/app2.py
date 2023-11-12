# # import random
# #
# # nume = input('introduceti numele:')
# # variante = ['piatra', 'hartie', 'foarfece']
# # for _ in range(3):
# #     alegere = input('introdu o alegere (piatra, hartie, foarfece): ')
# #     alegere_pc = random.choice(variante)
# #     if alegere[0].lower() == alegere_pc[0]:
# #         print('Remiza')
# #         continue
# #     if alegere[0].lower() == 'p':
# #         if
# #         print('ai pierdut')
# #     if alegere[0].lower() == 'p':
#
# lst = []
# while True:
#     numar = input("Introduceti un numar (cand v-ati saturat, apasati q): ")
#     if numar == 'q':
#         break
#     try:
#         numar = int(numar)
#     except ValueError:
#         print('nu ai ales o cifra')
#         continue
#     lst.append(numar)
#
#
#
#
#
#
#
#
#
#
#
# # Suma numarului de pe pozitia 1 si 2.
# print("O sa adaugam numarul 2 si 3.")
# print("lst[1] + lst[2] = ", lst[1] + lst[2])
# # Divizia primelor 2 numere din lista
# print("Divizia primelor 2 numere din lista este: ")
# print("lst[0] / lst[1] = ", lst[0] / lst[1])
# # Suma tuturor numerelor din lista
# sum = 0
# for i in lst:
#     sum += i
# print("Suma tuturor numerelor din lista este: ", sum)




#
#
# lst = []
# while True:
#     numar = input("Introduceti un numar (cand v-ati saturat, apasati q): ")
#     if numar == 'q':
#         break
#     try:
#         numar = int(numar)
#     except ValueError:
#         print('nu ai ales o cifra')
#         continue
#     lst.append(numar)
# # Suma numarului de pe pozitia 1 si 2.
# print("O sa adaugam numarul 2 si 3.")
# try:
#     print("lst[1] + lst[2] = ", lst[1] + lst[2])
# except IndexError:
#     print('Nu ai dat al treilea numar.')
#
# # Divizia primelor 2 numere din lista
# print("Divizia primelor 2 numere din lista este: ")
# try:
#     print("lst[0] / lst[1] = ", lst[0] / lst[1])
# except ZeroDivisionError:
#     print('Al doilea numar este zero.')
# except IndexError:
#     print('Primul sau al doilea numar lipseste.')
#
# # Suma tuturor numerelor din lista
# sum = 0
# for i in lst:
#     sum += i
# print("Suma tuturor numerelor din lista este: ", sum)
