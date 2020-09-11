import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly
import plotly.graph_objects as go


excel_file_path_plant1_generation = 'Plant_1_Generation_Data.csv'
excel_file_path_plant1_weather = 'Plant_1_Weather_Sensor_Data.csv'


# The Code Below is to identify the column names in the excel file

df_plant1_generation = pd.read_csv(excel_file_path_plant1_generation)
df_plant1_weather = pd.read_csv(excel_file_path_plant1_weather)
#print(df_plant1_generation.columns)
#print(df_plant1_weather.columns)


# The code below is to get information about the number of rows, column and information about data in the cell

#df_info_plant1_generation = df_plant1_generation.info()
#df_info_plant1_weather = df_plant1_weather.info()
#print(df_info_plant1_generation)
#print(df_info_plant1_weather)


# The code below provides statistical information about the data for each coloumn

#print(df_plant1_generation.describe())
#print(df_plant1_weather.describe())


# The code below can describe once specific cell, insert any column name into the square bracket to get its statistical information

#print(df_plant1_generation.describe()['DAILY_YIELD'])
#print(df_plant1_weather.describe()['MODULE_TEMPERATURE'])


# The following code combines both the plant generation data sheet and the plant weather data sheet to one file and represenrs data
df_all = pd.concat([df_plant1_generation,df_plant1_weather])
print(df_all)

#df_plot = df_all.loc[(df_all['DATE'] == '15-05-2020')]
#df_plot = df_plot.sort_values(by=['DATE'])

#df_all.plot(x='DATE', y='IRRADIATION')
#plt.show()

data_source_by_yield = [go.Scatter( x=df_all['SOURCE_KEY'], y=df_all['TOTAL_YIELD'])]
fig = go.Figure(data_source_by_yield)
fig.update_xaxes(title_text="Source Key")
fig.update_yaxes(title_text="Total Yeild")
fig.layout.plot_bgcolor = '#DCDCDC'
fig.layout.paper_bgcolor = '#DCDCDC'
fig.show()

plotly.offline.plot(fig, filename='Graphs.html')


data_date_by_yield = [go.Bar( x=df_all['PLANT_ID'], y=df_all['TOTAL_YIELD'])]
fig = go.Figure(data_date_by_yield)
fig.update_xaxes(title_text="DATE")
fig.update_yaxes(title_text="Total Yeild")
fig.layout.plot_bgcolor = '#DCDCDC'
fig.layout.paper_bgcolor = '#DCDCDC'
fig.show()


plotly.offline.plot(fig, filename='Graphs.html')

data_irradiation_by_date = [go.Scatter( x=df_all['DATE_TIME'], y=df_all['IRRADIATION'])]
fig = go.Figure(data_irradiation_by_date)
fig.update_xaxes(title_text="DATE")
fig.update_yaxes(title_text="IR IRRADIATION")
fig.layout.plot_bgcolor = '#DCDCDC'
fig.layout.paper_bgcolor = '#DCDCDC'
fig.show()

plotly.offline.plot(fig, filename='Graphs.html')
