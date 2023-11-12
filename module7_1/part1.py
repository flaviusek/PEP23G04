# # color = 'blue'
# # print(color)
#
# class Car:
#     color = 'red'
#
#     def drive(self):
#         print(f'Driving {self.color} car ...')
#
#
#
# my_car = Car()
# print(my_car)
# print('my_car:', my_car.color)
# my_car.color = 'blue'
# print('my_car:', my_car.color)
# my_car.drive()
# # print(dir(my_car))
#
#
# your_car = Car()
# print(your_car)
# print('your_car:', your_car.color)
# your_car.color = 'green'
# print('your_car:', your_car.color)
# your_car.drive()
# # print(dir(your_car))
#
# # def x():
# #     pass
# #
# # print(x.__name__)
# # print(Car.drive(Car))
# #
# # print(Car.color)
# # print(dir(Car))


class Chair:
    color = 'yellow'
    legs = 4
    back = True

    def __init__(self, extra_legs=False, color='red'):
        if extra_legs:
            self.legs += 2
        self.color = color

    def sitting(self):
        print(f' Sitting on {self.color} Chair...:')
        self.has_back = False


    def has_back(self):
        self.has_back = True


my_chair = Chair(extra_legs=True, color='brown')
print(my_chair.legs)
print(my_chair.color)

other_chair = Chair()
print(other_chair.has_back)
print(other_chair.legs)
print(other_chair.color)
