
 # 7
#
# a = 5
# b = 5
# c = "ana"
#
# print("Memory location of 'a':", id(a))
# print("Memory location of 'b':", id(b))
# print("Memory location of 'c':", id(c))
#
# print("Type of variable 'a':", type(a))
# print("Type of variable 'b':", type(b))
# print("Type of variable 'c':", type(c))


# 6
#
# original_string = 'hello python'
# str1 = words = original_string.split()
# str2 = words[0] = words[0] * 4
# str3 = result_string = '_'.join(words) + '.'
# print(str1, str2, str3)
#
# original_string = 'Ana are mere'
# str1 = words = original_string.split()
# str2 = words[0] = words[0] * 4
# str3 = result_string = '_'.join(words) + '.'
# print(str1, str2, str3)
#
# original_string = 'Pizza party'
# str1 = words = original_string.split()
# str2 = words[0] = words[0] * 4
# str3 = result_string = '_'.join(words) + '.'
# print(str1, str2, str3)
#



# # 5
str1 = input('Introduceti un cuvant: ')

rev = str1[::-1]

if str1 == rev:
        print("PALINDROME!")
else:
        print("NOT PALINDROME!")