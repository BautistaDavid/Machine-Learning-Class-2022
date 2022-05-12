import streamlit as st 

import pandas as pd 
# datos = pd.read_json('https://www.datos.gov.co/api/views/ynam-yc42/rows.json?accessType=DOWNLOAD')
datos = pd.read_csv('data\saber_11_2019.csv')
print('hola')

len(datos) / 3

datos.info()


len(datos)/4

data1 = datos.loc[:136553]
data2 = datos.loc[136554:273106]
data3 = datos.loc[273107:409659]
data4 = datos.loc[409660:546212]



data1.to_csv('icfes_1.csv')
data2.to_csv('icfes_2.csv')
data3.to_csv('icfes_3.csv')
data4.to_csv('icfes_4.csv')

pd.concat([data1,data2,data3,data4], axis = 0).reset_index()


len(datos)
136553 * 3
data1