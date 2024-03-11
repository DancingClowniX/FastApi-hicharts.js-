
# №1 Написать программу, которая подсчитывает повторяющиеся символы в заданной строке
#-----------------------------------------Первое решение-----------------------------
# dict = {}
# string = "jjjjantytynssn"
#
# for i in range (len(string)):
#     count = 0
#     for j in string:
#         if string[i] == j:
#             count += 1
#     dict[f"{string[i]}"] = count
# print(dict)
#-----------------------------------------Второе решение-----------------------------
# import collections
#
# string = "jjjjantyptynssn"
#
# counter = collections.Counter(string)
# print(counter)
#

