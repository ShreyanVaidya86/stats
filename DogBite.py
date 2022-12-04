import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from matplotlib.gridspec import GridSpec

#Read Dataset
mydataset = pd.read_csv('https://raw.githubusercontent.com/karenalicia14/stats/main/dogs_file.csv')

### Setting Variables and additional dataframes for plots
year_counter = Counter(mydataset['Year'])
#print(year_counter)                                                                         #Distribution of 'Year' column
df_year_counter = pd.DataFrame.from_dict(year_counter, orient='index').reset_index()        #Convert counter into Pandas Dataframe
year_df = df_year_counter.rename(columns={'index':'Year', 0:'Dog Bites'})                       #Rename columns of the dataframe

breed_counter = Counter(mydataset['Breed'])                  #Distribution of 'Breed' column
#print(breed_counter)                                                                         #Distribution of 'Breed' column
df_breed_counter = pd.DataFrame.from_dict(breed_counter, orient='index').reset_index()        #Convert counter into Pandas Dataframe
breed_df = df_breed_counter.rename(columns={'index':'Breed', 0:'Bites by Breed'}) #Rename columns of the dataframe
breed_df = breed_df.sort_values('Bites by Breed', ascending=True)

season_counter= Counter(mydataset['Season'])                 #Distribution of 'Season' column
#print(season_counter)
df_season_counter = pd.DataFrame.from_dict(season_counter, orient='index').reset_index()        #Convert counter into Pandas Dataframe
season_df = df_season_counter.rename(columns={'index':'Season', 0:'Bites by Season'}) #Rename columns of the dataframe
season_df = season_df.sort_values('Bites by Season')

#print(Counter(mydataset['Gender']))                 #Distribution of 'Gender' column
gender = mydataset.groupby('Gender').agg('count')   #Grouping our data by the number of values for each ‘Gender’
gender_labels = gender.ID.sort_values().index       #sorting the indexes for our aggregated types
gender_counts = gender.ID.sort_values()             #sorting the counts for our aggregated types

#print(Counter(mydataset['CrossBreed']))                      #Distribution of 'Breed' column
cross_breed = mydataset.groupby('CrossBreed').agg('count')   #Grouping our data by the number of values for each ‘CrossBreed’
cross_breed_labels = cross_breed.ID.sort_values().index      #sorting the indexes for our aggregated types
cross_breed_counts = cross_breed.ID.sort_values()            #sorting the counts for our aggregated types

#print(Counter(mydataset['SpayNeuter']))                      #Distribution of 'SpayNeuter' column
spay_neuter = mydataset.groupby('SpayNeuter').agg('count')   #Grouping our data by the number of values for each ‘CrossBreed’
spay_neuter_labels = cross_breed.ID.sort_values().index      #sorting the indexes for our aggregated types
spay_neuter_counts = cross_breed.ID.sort_values()            #sorting the counts for our aggregated types

########  Let's answer our questions!  #######

#Line Graph Questions
#1.i. Throughout the years has the dog bite decreased?
year_df.plot(x ='Year', y='Dog Bites', kind='line')
plt.xlabel("Year", labelpad=15)
plt.ylabel("Number of Bites", labelpad=15)
plt.title("Number of Dog's Bites trough out the years", y=1.02, fontsize=22)
plt.show()
print("Answer 1.i.: In 2020 & 2021 there has been a sharp decrease in dog bites.\n")


#Bar Graph Questions
#2.i. Which is the most aggressive 10 dog breeds?
breed_mode = mydataset.loc[:,"Breed"].mode()          #Finding the mode in column 'Breed'
top_10 = breed_df.tail(10)
top_10.plot(x ='Breed', y='Bites by Breed', kind='barh')
plt.xlabel("Breed", labelpad=15)
plt.ylabel("Number of Bites", labelpad=15)
plt.title("Number of Bites by Dog's Breed", y=1.02, fontsize=22)
plt.show()
print("Answer 2.i.: The most aggressive breed is the ", breed_mode[0],"\n")


#2.ii. Does the season change the aggressiveness of dogs?
season_mode = mydataset.loc[:,"Season"].mode()        #Finding the mode in column Season
#Let's plot the information
season_df.plot(x ='Season', y='Bites by Season', kind='bar')
plt.xlabel("Season", labelpad=15)
plt.ylabel("Number of Bites", labelpad=15)
plt.title("Number of Bites by Season", y=1.02, fontsize=22)
plt.show()
print("Answer 2.ii.:In ", season_mode[0], " dogs bite more.\n")

#2.iii. Which is the age at which dogs are more aggressive?
dogage=mydataset["Age"]
agebite_mode = mydataset.loc[:,"Age"].mode()            #Finding the mode in column Age
dogage.value_counts().sort_index().plot(kind='bar')     #Plotting bargraph
plt.xlabel('age') # x-axis label
plt.ylabel('Frequency') # y-axis label
plt.show()
print("Answer 2.iii.:",agebite_mode[0], "years old, dogs bite more often.\n")

#Piechart Questions:
#3.i. Do neutered dogs bite less?
spay_neuter_mode = mydataset.loc[:,"SpayNeuter"].mode()      #Finding the mode in column SpayNeuter
the_grid = GridSpec(2, 2)                                                   #Figure details
plt.subplot(the_grid[0, 1], aspect=1, title='Neutered Dog Bites')
spay_neuter_id = plt.pie(spay_neuter_counts, labels=spay_neuter_labels, autopct='%1.1f%%')
plt.show()
if spay_neuter_mode[0] == True:
    print("Answer 3.i.: Neutered dogs bite more.\n")
elif spay_neuter_mode[0] == False:
    print("Answer 3.i.: Neutered dogs don't bite more.\n")

#3.ii. Do dogs with mixed breeds tend to bite more?
cross_breed_mode = mydataset.loc[:,"CrossBreed"].mode()      #Finding the mode in column CrossBreed
the_grid = GridSpec(2, 2)                                                   #Figure details
plt.subplot(the_grid[0, 1], aspect=1, title='Cross Breed Dog Bites')
cross_breed_id = plt.pie(cross_breed_counts, labels=cross_breed_labels, autopct='%1.1f%%')
plt.show()
if cross_breed_mode[0] == True:
    print("Answer 3.ii.: Mixed breed dogs definitely tend to bite more.\n")
elif cross_breed_mode[0] == False:
    print("Answer 3.ii.: Mixed breed dogs don't bite more than non-cross breed ones.\n")

#3.i. What is the most aggressive gender?
gender_mode = mydataset.loc[:,"Gender"].mode()
if gender_mode[0] == "M":
    print("Answer 3.iii.: Masculine dog gender is the most aggressive\n")
elif gender_mode[0] == "F":
    print("Answer 3.iii.: Feminine dog gender is the most aggressive\n")
else:
    print("Answer 3.iii.: The most aggressive gender is unknown\n")
#Let's plot the information
plt.subplot(the_grid[0, 1], aspect=1, title='Dog Bites by Gender')
gender_id = plt.pie(gender_counts, labels=gender_labels, autopct='%1.1f%%')
plt.show()

######################-- Coded by: Lucy, Karen, Miguel,Shreyan --######################
####-- Git Hub Link: https://github.com/karenalicia14/stats/edit/main/DogBite.py --####

#######################-----------END OF PROJECT CODE-----------#######################
