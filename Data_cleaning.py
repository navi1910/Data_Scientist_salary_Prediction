# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 10:37:10 2022

@author: Navi
"""
#Data Cleaning
import os
os.chdir('D:/Ken_jee_project')
os.getcwd()

import pandas as pd
df = pd.read_csv("D:/ken_jee_project/uncleaned_data.csv")

df['Per Hour'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['Employer Provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided' in x.lower() else 0)

#Salary Estimate
df = df[df['Salary Estimate'] != '-1']
df['Salary Estimate'] = df['Salary Estimate'].apply(lambda x:x.split('(')[0])
df['Salary Estimate'] = df['Salary Estimate'].apply(lambda x:x.replace('$',"").replace('K', ""))
df['Salary Estimate'] = df['Salary Estimate'].apply(lambda x:x.lower().replace('per hour','').replace('employer provided salary:',''))

df['max_salary'] = df['Salary Estimate'].apply(lambda x: int(x.split('-')[1]))
df['min_salary'] = df['Salary Estimate'].apply(lambda x: int(x.split('-')[0]))
df['average_salary'] = (df['max_salary'] + df['min_salary'])/2

#Company Name
df['Company_text'] = df.apply(lambda x: x['Company Name'] if x['Rating']<0 else x['Company Name'][:-3], axis =1)

#Location and State
df['State'] = df['Location'].apply(lambda x:x.split(',')[1])
df['State'] = df['State'].apply(lambda x:x.strip() if x.strip() != 'Los Angeles' else 'CA')
df['State'].value_counts()
df['True_hq'] = df.apply(lambda x: 1 if x['Location'] == x['Headquarters'] else 0, axis =1)

#Age of Company
df['Company_age'] = df['Founded'].apply(lambda x: int(2022-x) if x>0 else -1)

#Parsing the Job Description
#Python
df['python'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
#r studio
df['rstudio'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
#spark
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
#aws
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
#excel
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)

df.to_csv('D:/ken_jee_project/cleaned_dssalary_data.csv', index = False)

































