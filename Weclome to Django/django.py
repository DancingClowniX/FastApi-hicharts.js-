import collections
# list1 = [1, 2, 3, 4, 5]
# list_2 = list(map(lambda x:x*2,list1))
# print(list_2)

# def check_candidates(names_input: str, scores_input: str)-> str:
#     names = names_input.split(',')#lst
#     scores = scores_input.split('|')#lst
#     listNone = ''
#     stringResult = ''
#     for i in range(0,len(scores)):
#         lstScore = scores[i].split(',')
#         list1 = [int(el) for el in lstScore]
#         summ = sum(list1)/4
#         if summ < 50:
#             names.pop(0)
#     for item in names:
#         stringResult += f'{item},'
#     stringResult = stringResult.rstrip(',')
#     if stringResult == listNone:
#         return "Никто"
#     else:
#         return stringResult
# result = check_candidates('Oleg,Ksenia,Sergei,Sergei', "27,26,31,37|54,59,67,4|60,60,60,60|60,60,70,70")


# Формат вывода
# Имена тех сотрудников, которые набрали проходной балл на вакансию.
# Каждое имя должно начинаться с новой строки, в выводе не должно быть запятых и других символов. Если никто не набрал проходной балл, выводится «Никто»‎.‎

# a = [1,2,3,4,5,6,7,8,9 , 10]
# k = 7
# count1 = 0
# count2 = 0
# def pair():
#     for i in range (0,len(a)):
#         for j in range(0, len(a)):
#             if a[i]+a[j] == k :
#                 count1 = a[i]
#                 count2 = a[j]
#     print(count2,count1)
# pair()

# def multiply():
# 	for i in range (0, 1001):
# 		if i % 3 == 0 and i % 5 != 0:
# 			sum_digit = 0
# 			for j in str(i):
# 				sum_digit += int(j)
# 			if sum_digit < 10:
# 				print(i)
# 			else:
# 				continue
# multiply()

# with open("digit.txt", 'r+', encoding='utf-8') as f:
#     digits = f.readlines()
#     item_list = []
#     for digit in digits:
#         digit = digit.replace('\n', '')
#         item_list.append(digit)
#     print(sorted(item_list))

# a = [3, 5, 4, 3, 2, 6, 7, 5, 8]
# b = collections.Counter(a)
# for
#     print(k,v)
# import os
#
# import requests
#
# list1 =[1,2,3,4,5,6,7,8,9,10]
# list2 = []
#
#
# def recus(n):
#     if list1 == list2:
#         print(True)
#         print(list2)
#     else:
#         list2.append(n)
#         n+=1
#         return recus(n)
#
# recus(1)

nums=[1,2,3,4,5,6,7,8,9,10]
listcomp = [n*2 for n in nums]
print(listcomp)