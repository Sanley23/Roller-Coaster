import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt

# load rankings data here:
steel_df = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')
wood_df = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
roller_coaster_df = pd.read_csv('roller_coasters.csv')

# write function to plot rankings over time for 1 roller coaster here:


def one_coaster_ranking(name, park ,dataframe):
  coaster_rank = dataframe[(dataframe['Name'] == name) & (dataframe['Park'] == park)]
  
  ax1 = plt.subplot(1,1,1)
  
  plt.plot(coaster_rank['Rank'], coaster_rank['Year of Rank'], marker = 'o')
  
  ax1.set_yticks(coaster_rank['Year of Rank'])
  ax1.set_xlabel('Ranking')
  ax1.set_ylabel('Year')
  ax1.set_title('Ranking per Year')

  plt.show()

#one_coaster_ranking('El Toro', 'Six Flags Great Adventure', wood_df)


plt.clf()

# write function to plot rankings over time for 2 roller coasters here:

def two_coaster_ranking(name1, park1, name2, park2, dataframe):
  ranking1 = dataframe[(dataframe['Name'] == name1) & (dataframe['Park'] == park1)]
  ranking2 = dataframe[(dataframe['Name'] == name2) & (dataframe['Park'] == park2)]
  
  ax = plt.subplot()
  plt.plot(ranking1['Rank'], ranking1['Year of Rank'], marker='o')
  plt.plot(ranking2['Rank'], ranking2['Year of Rank'], marker='s', color='yellow')
  
  ax.set_xticks(range(len(ranking1['Rank'])))
  ax.set_xlabel('Ranking')
  ax.set_ylabel('Years')
  ax.set_title('Two Coasters ranking per Year')
  ax.legend([name1, name2])
  
  plt.show()

#two_coaster_ranking('El Toro','Six Flags Great Adventure', 'Boulder Dash','Lake Compounce', wood_df)

plt.clf()

# write function to plot top n rankings over time here:

def ranking_time(number, dataframe):
  top_ranking = dataframe[dataframe['Rank'] <= number]
  #print(top_ranking)
  #ax = plt.subplot()

  for coaster in set(top_ranking['Name']):
    coaster_rankings = top_ranking[top_ranking['Name'] == coaster]
    plt.plot(coaster_rankings['Year of Rank'], coaster_rankings['Rank'],marker='o', label=coaster)
    
  plt.title('Ranking from N° ' + str(number) + 'th to 1st')
  plt.show()

ranking_time(4, wood_df)

plt.clf()

# load roller coaster data here:
#print(roller_coaster_df.head(10))
def plot_a_hist(dataframe, the_column):
  datas_from_the_column_to_plot = dataframe[the_column]
  plt.hist(datas_from_the_column_to_plot.dropna(), normed = True)
  plt.title("The Distribution of " + the_column + " for Roller Coasters")
  plt.xlabel(the_column)
  plt.ylabel("Frequency")
  plt.show()

#plot_a_hist(roller_coaster_df, "speed")

# write function to plot histogram of column values here:

def inversions_bar(df, park):
  park_df = df[df['park'] == park]
  #print(park_df)
  park_df = park_df.sort_values('num_inversions', ascending = False)

  ax = plt.subplot()
  plt.bar( range(len(park_df['name'])), park_df['num_inversions'])

  ax.set_xticks(range(len(park_df['name'])))
  ax.set_xticklabels(park_df['name'], rotation = 40)
  ax.set_xlabel('Roller Coaster')
  ax.set_ylabel('Investmen')
  ax.set_title('Investement amount per Roller Coaster in: ' + park )

  plt.show()


#inversions_bar(roller_coaster_df, 'Bobbejaanland')

#inversions_bar(roller_coaster_df,'Parque Warner Madrid')


plt.clf()

# write function to plot inversions by coaster at a park here:

# Es el ejercicio de arriba, le pifie en uno y quedaron desfasados

plt.clf()
    
# write function to plot pie chart of operating status here:

def operative_pie(df):
  operating = df[df['status'] == 'status.operating']
  
  not_operating = df[df['status'] == 'status.closed.definitely']
  compare_list = [len(operating), len(not_operating)]
  labels = ['operating Parks', 'Closed Parks']
  
  plt.pie(compare_list, labels = labels, autopct = '%0.1f%%')
  plt.axis('equal')
  plt.legend(labels)
  plt.title('Open Vs Closed Parks')

  plt.show()

#print(roller_coaster_df)
#operative_pie(roller_coaster_df)

plt.clf()
  
# write function to create scatter plot of any two numeric columns here:

def scatter_columns(df, column1, column2):
  one = df[column1]
  two = df[column2]

  plt.scatter(one, two)
  plt.xlabel(column1)
  plt.ylabel(column2)
  plt.title('Scatterplot of ' + column1 + ' Vs '+ column2)

  plt.show()

#scatter_columns(roller_coaster_df, 'speed', 'num_inversions' )


plt.clf()