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
import matplotlib.ticker as ticker
import matplotlib.cm as cm
import matplotlib as mpl
from matplotlib.gridspec import GridSpec

#Read Dataset
mydataset = pd.read_csv('https://raw.githubusercontent.com/karenalicia14/stats/main/dogs_file.csv')

### Setting Variables and additional dataframes for plots
year_counter = Counter(mydataset['Year'])
print(year_counter)                                                                         #Distribution of 'Year' column
df_year_counter = pd.DataFrame.from_dict(year_counter, orient='index').reset_index()        #Convert counter into Pandas Dataframe
year_df = df_year_counter.rename(columns={'index':'Year', 0:'Dog Bites'})                       #Rename columns of the dataframe

breed_counter = Counter(mydataset['Breed'])                  #Distribution of 'Breed' column
print(breed_counter)                                                                         #Distribution of 'Breed' column
df_breed_counter = pd.DataFrame.from_dict(breed_counter, orient='index').reset_index()        #Convert counter into Pandas Dataframe
breed_df = df_breed_counter.rename(columns={'index':'Breed', 0:'Bites by Breed'}) #Rename columns of the dataframe
breed_df = breed_df.sort_values('Bites by Breed', ascending=True)

season_counter= Counter(mydataset['Season'])                 #Distribution of 'Season' column
print(season_counter)
df_season_counter = pd.DataFrame.from_dict(season_counter, orient='index').reset_index()        #Convert counter into Pandas Dataframe
season_df = df_season_counter.rename(columns={'index':'Season', 0:'Bites by Season'}) #Rename columns of the dataframe
season_df = season_df.sort_values('Bites by Season')

print(Counter(mydataset['Gender']))                 #Distribution of 'Gender' column
gender = mydataset.groupby('Gender').agg('count')   #Grouping our data by the number of values for each ‘Gender’
gender_labels = gender.ID.sort_values().index       #sorting the indexes for our aggregated types
gender_counts = gender.ID.sort_values()             #sorting the counts for our aggregated types

print(Counter(mydataset['CrossBreed']))                      #Distribution of 'Breed' column
cross_breed = mydataset.groupby('CrossBreed').agg('count')   #Grouping our data by the number of values for each ‘CrossBreed’
cross_breed_labels = cross_breed.ID.sort_values().index      #sorting the indexes for our aggregated types
cross_breed_counts = cross_breed.ID.sort_values()            #sorting the counts for our aggregated types

print(Counter(mydataset['SpayNeuter']))                      #Distribution of 'SpayNeuter' column
spay_neuter = mydataset.groupby('SpayNeuter').agg('count')   #Grouping our data by the number of values for each ‘CrossBreed’
spay_neuter_labels = cross_breed.ID.sort_values().index      #sorting the indexes for our aggregated types
spay_neuter_counts = cross_breed.ID.sort_values()            #sorting the counts for our aggregated types

########  Let's answer our questions!  #######

#1. Throughout the years has the dog bite decreased?
year_df.plot(x ='Year', y='Dog Bites', kind='line')
plt.xlabel("Year", labelpad=15)
plt.ylabel("Number of Bites", labelpad=15)
plt.title("Number of Dog's Bites trough out the years", y=1.02, fontsize=22)
plt.show()

#1.i. During which season do dogs bite more?
season_mode = mydataset.loc[:,"Season"].mode()        #Finding the mode in column Season
print("In ", season_mode[0], " dogs bite more.")
#Let's plot the information
season_df.plot(x ='Season', y='Bites by Season', kind='bar')
plt.xlabel("Season", labelpad=15)
plt.ylabel("Number of Bites", labelpad=15)
plt.title("Number of Bites by Season", y=1.02, fontsize=22)
plt.show()
