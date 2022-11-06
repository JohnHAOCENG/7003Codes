# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 10:00:08 2022

@author: John
"""

import matplotlib as mpl
import numpy as np

student_num = 20
course_num = 4

student_score_int = np.random.randint(40,100,(20, 4))
student_socre_float = np.random.rand(20,4)

student_scores = np.round(student_score_int+student_socre_float, 1)
# print(student_scores)

course_lib_get = lambda x, y: x[:, y]
course_name = ['Math', 'Economics', 'Finance', 'Science']
course_scores_dict = {course_name[x]:[] for x in range(4)}
course_first = {course_name[x]:[] for x in range(4)}

for i in range(len(student_scores[1,:])):
    course_scores = course_lib_get(student_scores, i)
    course_scores = np.unique(course_scores)
    course_scores_dict[course_name[i]] = course_scores.tolist()
    course_first[course_name[i]] = np.max(course_scores).tolist()
    
# print(course_first)

students_mean = np.mean(student_scores, axis=1).round(1)

student_mean_index = {students_mean[x]:x for x in range(20)}
student_mean_rank ={student_mean_index[x]:x for x in np.flip(np.sort(students_mean))}
print(student_mean_rank)

rank_index = 1
for x in student_mean_rank:
    print('Rank {0}:{1}: {2}'.format(rank_index, x, student_mean_rank[x]))
    rank_index +=1
    if rank_index > 5:
        break