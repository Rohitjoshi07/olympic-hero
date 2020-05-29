# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data= pd.read_csv(path)
data.rename(columns = {'Total':'Total_Medals'},inplace=True)
print(data.head(10))
#Code starts here



# --------------
#Code starts here0
#Code starts here0
data['Better_Event'] = np.where(data['Total_Summer']>data['Total_Winter'] ,
'Summer','Winter' )

data['Better_Event'] = np.where(data['Total_Summer']==data['Total_Winter'] ,
'Both',data['Better_Event'] )

better_event = data['Better_Event'].value_counts().idxmax()
print(better_event)


# --------------
#Code starts here
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter',
'Total_Medals']]
top_countries.drop(data.index[-1],inplace=True)
def top_ten(top_countries,column):
     country_list = []
     countries = top_countries.nlargest(10,column)
     country_list = countries['Country_Name'].tolist()
     return country_list
top_10_summer =top_ten(top_countries,'Total_Summer')
top_10_winter =top_ten(top_countries,'Total_Winter')
top_10 =top_ten(top_countries,'Total_Medals')

common = [i for i in top_10_summer for  j in top_10_winter  for k in top_10 if i==j==k]
print(common)



# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

#fig, (ax_1,ax_2,ax_3) = plt.subplot(1,3, figsize = (20,10))
#plot 1
summer_df.plot('Country_Name','Total_Summer',kind='bar',color='r')
plt.xlabel("Countries")
plt.xticks(rotation=45)
plt.title('Medal counts for summer top 10 teams')
plt.show()

#plot 2
winter_df.plot('Country_Name','Total_Winter',kind='bar',color='b')
plt.xlabel("Countries")
plt.xticks(rotation=45)
plt.title('Medal counts for winter top 10 teams')
plt.show()

#plot 3
top_df.plot('Country_Name','Total_Medals',kind='bar',color='g')
plt.xlabel("Countries")
plt.xticks(rotation=45)
plt.title('Medal counts for all over top 10 teams')
plt.show()


# --------------
#Code starts here
#summer max gold
summer_df['Golden_Ratio'] = summer_df['Gold_Summer'] / summer_df['Total_Summer']
summer_max_ratio = summer_df['Golden_Ratio'].max()
summer_country_gold = summer_df[summer_df['Golden_Ratio'] == summer_max_ratio]['Country_Name'].to_string(index=False)


#winter max gold
winter_df['Golden_Ratio'] = winter_df['Gold_Winter'] / winter_df['Total_Winter']
winter_max_ratio = winter_df['Golden_Ratio'].max()
winter_country_gold =winter_df[winter_df['Golden_Ratio'] == winter_max_ratio]['Country_Name'].to_string(index=False)

#top max gold
top_df['Golden_Ratio'] = top_df['Gold_Total'] / top_df['Total_Medals']
top_max_ratio = top_df['Golden_Ratio'].max()
top_country_gold = top_df[top_df['Golden_Ratio'] == top_max_ratio]['Country_Name'].to_string(index=False)




# --------------
#Code starts here
data_1 = data.drop(data.index[-1])
data_1['Total_Points'] = 3*data_1['Gold_Total'] + 2*data_1['Silver_Total'] + 1*data_1['Bronze_Total']
most_points = data_1['Total_Points'].max()
best_country = data_1[data_1['Total_Points'] == most_points]['Country_Name'].to_string(index=False)


# --------------
#Code starts here
best = data[data['Country_Name'] == best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot(kind='bar',stacked=True)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)
plt.show()


