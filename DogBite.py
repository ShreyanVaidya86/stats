import pandas as pd
import numpy as np
import math
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt
from plotnine.data import mpg
import plotnine
import pylab
from sklearn.linear_model import LinearRegression
import sklearn.metrics
import statsmodels.api as sm
from collections import Counter

#Read Dataset
#mydataset= pd.read_csv(r'C:\\Users\\karen\\Documents\\Karen\\Canadá\\Lambton\\Academic\\Term 1\\BAM 1024 - Introduction to Statistical Analysis\\Project\\dogs_file.csv')
mydataset = pd.read_csv('https://raw.githubusercontent.com/karenalicia14/stats/main/dogs_file.csv'
#Let's answer our questions!'

#TREND CHARTS
#1. Throughout the years has the dog bite declined? (Trend Line)

#1.i. During which season do dogs bite more? (Bar Chart)
season_mode = mydataset.loc[:,"Season"].mode()
print("In ", season_mode, " dogs bite more.")


#BAR/PIE GRAPHS - MODE
#2. Which is the most aggressive dog breed? (Bar Chart)
breed_mode = mydataset.loc[:,"Breed"].mode()
print("The most aggressive breed is the ", breed_mode)
print(Counter(mydataset['Breed']))
title_type = mydataset.groupby('Breed').agg('count')
print(title_type)

#2.i. What is the most aggressive gender (Pie Chart)
gender_mode = mydataset.loc[:,"Gender"].mode()
print(gender_mode)
#if gender_mode == 'M':
#   print('The most aggressive gender is Masculine')
#elif gender_mode == 'F':
#   print('The most aggressive gender is Feminine')
#else:
#   print('The most aggressive is unknown')

#2.ii. Which is the age at which dogs are more aggressive? (Bar Chart)
age_mode = mydataset.loc[:,"Age"].mode()
print("At  ", age_mode, " years, dogs become more aggressive")

#2.iii. Do dogs with mixed breeds tend to bite more? (Pie Chart)
cross_breed = mydataset.groupby("CrossBreed")["Breed"].count().sort_values(ascending=False)
print(cross_breed)


#HYPOTHESIS TESTING
#3. Do neutered dogs bite less?
#Ho = probability of neutered dog to bite = probability of non neutered dog to bite
#Ha = probability of neutered dog to bite != probability of non neutered dog to bite

#4. Which city has the highest number of dog bite vs least number of dog bites? (Back up question)
city_bite = mydataset.groupby("Borough")["DateOfBite"].count().sort_values(ascending=False)
city_bite_max = mydataset.groupby("Borough")["DateOfBite"].count().max()
city_bite_min = mydataset.groupby("Borough")["DateOfBite"].count().min()
print(city_bite)
