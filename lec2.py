# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 10:52:57 2022

@author: John
"""

# =============================================================================
# list_index= []
# myString = "this is a good course"
# 
# for i in range(len(myString)):
#     if myString[i] == 's':
#         list_index.append(i)
# 
# print(len(list_index))
# print(list_index)
# =============================================================================

# =============================================================================
# list_all = []
# temp = []
# count = 0
# for i in range(1,105):
#     temp.append(i)
#     count+=1
#     if count == 4:
#         list_all.append(temp)
#         count = 0
#         temp = []
# print(list_all)
# =============================================================================

dic = {}
for i in range(97,123):
    dic[chr(i).lower()]= chr(i).upper()

for i in range(97,123):
    dic[chr(i).upper()]= chr(i).lower()

print(dic)
