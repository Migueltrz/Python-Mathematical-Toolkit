import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns




DF = pd.read_csv('seattle-weather.csv')

# Convert the date column to datetime format
DF['date'] = pd.to_datetime(DF['date'])

# Extract the year from the date column and filter the DataFrame
DF_filteredDF = DF[(DF['date'].dt.year == 2015)]

print(DF_filteredDF)

# Save the filtered DataFrame to a CSV file
DF_filteredDF.to_csv('clima.csv', index=False)




arr_x=[]
arr_y =[]

precip = DF_filteredDF.iloc[:, [1]].values
arr_x.append(precip)
wind = DF_filteredDF.iloc[:, [4]].values

arr_y.append(wind)

arr = np.array(arr_x)
arr2 = np.array(arr_y)
vec = arr.flatten()
vec2 = arr2.flatten()
sns.displot([vec])
#plt.show()

sns.boxplot([DF_filteredDF.temp_min])
plt.show()