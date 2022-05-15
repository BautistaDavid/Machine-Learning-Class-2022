from math import floor
from tkinter.tix import Tree
from icfes_streamlit.utils import dic_depto
import pandas as pd
import seaborn as sns 

df = pd.read_csv('data/data_icfes.csv')

# Creamos y modificamos algunas variables 
df['region'] = df['estu_depto_reside'].replace(dic_depto())

df['edad'] = [2020 - int(value.split('/')[2]) for value in df['estu_fechanacimiento']]
df['edad'].replace({edad:int(df['edad'].mean()) for edad in [2018,2019,5,110,120,2,1,9,6,3,4,7,8,11,10]},inplace=True)


cols_category = ['estu_etnia', 'estu_depto_reside']
cols_int_8 = ['estu_genero','edad','fami_estratovivienda','fami_educacionpadre','fami_educacionmadre']

for col in cols_category:
    df[col] = df[col].astype('category')

for col in cols_int_8:
    df[col] = df[col].astype('int8')


df.drop(columns=['estu_fechanacimiento'],inplace=True)


df.info()

for i in df.columns:
    print(i)

sns.boxplot(data=df,x='punt_ingles')