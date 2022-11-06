# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 17:31:38 2021

@author: zez
"""
import numpy as np
import pandas as pd
from selenium import webdriver 
from selenium import common
from selenium.webdriver import ActionChains  
import time

path = r"D:\Python_study\chromedriver.exe"
browser = webdriver.Chrome(path)
university_path = 'https://www.topuniversities.com/university-rankings/world-university-rankings/2022'
browser.get(university_path)
# maximize the window size:
browser.maximize_window()
browser.find_element_by_xpath('//*[@id="popup-buttons"]/button').click()
# login operation
browser.find_element_by_xpath('/html/body/div[1]/div/div/header/div[1]/div/div[2]/ul/li[3]/a').click()
browser.find_element_by_xpath('//*[@id="edit-name"]').send_keys('enzhizhu8@gmail.com')
browser.find_element_by_xpath('//*[@id="edit-pass"]').send_keys('znz18096122860')
browser.find_element_by_xpath('//*[@id="edit-submit"]').click()
time.sleep(1)




time.sleep(10)
# creating the empty list
ranking1 = []
location1 = []
overall_score1 = []

# Get elements from the website:
for i in range(0,20):
# get the ranking,location and score of these universities. 
    ranking = browser.find_elements_by_xpath('//*[@id="ranking-data-load"]/div[position()>=1]/div/div/div/div[2]/div/div[1]/a')
    ranking = list(map(lambda x: x.text,ranking))
    ranking1 = ranking1 +ranking
    location = browser.find_elements_by_xpath('//*[@id="ranking-data-load"]/div[position()>=1]/div/div/div/div[2]/div/div[2]')
    location = list(map(lambda x: x.text,location))
    location1 = location1 + location
    overall_score = browser.find_elements_by_xpath('//*[@id="ranking-data-load"]/div[position()>=1]/div/div/div/div[3]')
    overall_score = list(map(lambda x: x.text,overall_score))
    overall_score1 = overall_score1 + overall_score
    
    page_tmp = browser.find_element_by_xpath('//*[@id="alt-style-pagination"]')
    # //*[@id="alt-style-pagination"]/li[3]
    page_num = page_tmp.text.split('\n')
    # get the location for next page button
    next_path = r'//*[@id="alt-style-pagination"]/li[{}]'.format(len(page_num) + 2)
    loc_path = r'//*[@id="ranking-data-load"]/div[12]/div/div/div/div[2]/div/div[1]/a'
    next_button = browser.find_element_by_xpath(loc_path)
    # scroll to specific position.
    browser.execute_script("arguments[0].scrollIntoView();", next_button) 
    # click the next button
    browser.find_element_by_xpath(next_path).click()
    
    time.sleep(2)
    
# move to rankings indicators section.
move_place = r'//*[@id="block-tu-d8-content"]/div/article/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div[1]'
next_button1 = browser.find_element_by_xpath(move_place)
# move to location of ranking indicators button
browser.execute_script("arguments[0].scrollIntoView();", next_button1)
ranking_indicators = '//*[@id="block-tu-d8-content"]/div/article/div/div[3]/div/div/div/div[1]/div/div/ul/li[2]/a'
browser.find_element_by_xpath(ranking_indicators).click()
# find columns names of each criteria
column_names = browser.find_elements_by_xpath('//*[@id="move-all-js"]/div[position()>=1]/div/div')
column_names = list(map(lambda x :x.text,column_names))
column_names = column_names[1:]
browser.find_element_by_xpath('//*[@id="alt-style-pagination"]/li[2]/a').click()

international_student_ratio1 = []
international_faculty_ratio1 = []
faculty_student_ratio1 = []
citations_per_faculty1 = []
academic_reputation1 = []
employment_reputation1 = []

# find first 20 pages of each ranking criterias
for j in range(20):
    time.sleep(1)
    international_student_ratio = browser.find_elements_by_xpath('//*[@id="ranking-data-load_ind"]/div[position()>=1]/div/div/div/div[2]/div/div/div/div[2]/div/div/span/div/div')
    international_student_ratio = list(map(lambda x: x.text,international_student_ratio))
    international_student_ratio1 = international_student_ratio1 +international_student_ratio
    international_faculty_ratio = browser.find_elements_by_xpath('//*[@id="ranking-data-load_ind"]/div[position()>=1]/div/div/div/div[2]/div/div/div/div[3]/div/div/span/div/div')
    international_faculty_ratio = list(map(lambda x: x.text,international_faculty_ratio))
    international_faculty_ratio1 =  international_faculty_ratio1 + international_faculty_ratio
    browser.find_element_by_xpath('//*[@id="indicator-tab"]/div[1]/div/div/div/div[2]/span[2]/i').click()
    faculty_student_ratio = browser.find_elements_by_xpath('//*[@id="ranking-data-load_ind"]/div[position()>=1]/div/div/div/div[2]/div/div/div/div[4]/div/div/span/div/div')
    faculty_student_ratio = list(map(lambda x: x.text,faculty_student_ratio))
    faculty_student_ratio1 = faculty_student_ratio1 + faculty_student_ratio
    browser.find_element_by_xpath('//*[@id="indicator-tab"]/div[1]/div/div/div/div[2]/span[2]/i').click()
    citations_per_faculty = browser.find_elements_by_xpath('//*[@id="ranking-data-load_ind"]/div[position()>=1]/div/div/div/div[2]/div/div/div/div[5]/div/div/span/div/div')
    citations_per_faculty = list(map(lambda x: x.text,citations_per_faculty))
    citations_per_faculty1 = citations_per_faculty1 +citations_per_faculty
    browser.find_element_by_xpath('//*[@id="indicator-tab"]/div[1]/div/div/div/div[2]/span[2]/i').click()
    academic_reputation = browser.find_elements_by_xpath('//*[@id="ranking-data-load_ind"]/div[position()>=1]/div/div/div/div[2]/div/div/div/div[6]/div/div/span/div/div')
    academic_reputation = list(map(lambda x: x.text,academic_reputation))
    academic_reputation1 = academic_reputation1 +academic_reputation
    browser.find_element_by_xpath('//*[@id="indicator-tab"]/div[1]/div/div/div/div[2]/span[2]/i').click()
    employment_reputation = browser.find_elements_by_xpath('//*[@id="ranking-data-load_ind"]/div[position()>=1]/div/div/div/div[2]/div/div/div/div[7]/div/div/span/div/div')
    employment_reputation = list(map(lambda x: x.text,employment_reputation))
    employment_reputation1 = employment_reputation1 + employment_reputation
    
    page_tmp = browser.find_element_by_xpath('//*[@id="alt-style-pagination"]')
    page_num = page_tmp.text.split('\n')
    # location of next page button.
    next_path = r'//*[@id="alt-style-pagination"]/li[{}]'.format(len(page_num) + 2)
    browser.find_element_by_xpath(next_path).click()
    time.sleep(2)

   
# create a dictionary that contains each ranking information  
dict1 = {'name':ranking1,'location':location1,'overall_score':overall_score1,'International Students Ratio':international_student_ratio1,
         'International Faculty Ratio':international_faculty_ratio1,'Faculty Student Ratio':faculty_student_ratio1,'Citations per Faculty':citations_per_faculty1,
         'Academic Reputation':academic_reputation1,'Employer Reputation':employment_reputation1}
# create rankings
dict1['Ranking'] = list(range(1,len(ranking1)+1))

dataframe = pd.DataFrame(dict1)

# change location of each column
dataframe = dataframe[['Ranking',
                       'name', 
                       'location', 
                       'overall_score',
                       'International Students Ratio',
                       'International Faculty Ratio',
                       'Faculty Student Ratio',
                       'Citations per Faculty',
                       'Academic Reputation',
                       'Employer Reputation']]

dataframe.to_csv('output.csv',encoding = 'utf_8_sig',index=False)  

  

    



















