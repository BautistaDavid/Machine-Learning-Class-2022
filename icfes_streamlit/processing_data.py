from icfes_streamlit.utils import dic_depto, dic_educacion
import pandas as pd 
import numpy as np 
df = pd.read_csv('data\saber_11_2019.csv')

# data1 = data.loc[:136553]
# data2 = data.loc[136554:273106]
# data3 = data.loc[273107:409659]
# data4 = data.loc[409660:546212]




df.columns =[i.lower() for i in df.columns]
cols = ['estu_fechanacimiento', 'estu_genero', 'estu_etnia', 'estu_depto_reside','estu_mcpio_reside', 'fami_estratovivienda','fami_educacionpadre', 'fami_educacionmadre', 'fami_tieneinternet', 'fami_tienecomputador','cole_genero', 'cole_naturaleza','cole_calendario', 'cole_bilingue','cole_sede_principal', 'cole_area_ubicacion', 'cole_jornada', 'estu_privado_libertad',
            'punt_lectura_critica','percentil_lectura_critica','desemp_lectura_critica','punt_matematicas', 'percentil_matematicas', 'desemp_matematicas','punt_c_naturales', 'percentil_c_naturales', 'desemp_c_naturales', 'punt_sociales_ciudadanas', 'percentil_sociales_ciudadanas',
            'desemp_sociales_ciudadanas', 'punt_ingles', 'percentil_ingles','desemp_ingles', 'punt_global', 'percentil_global']
df = df.filter(cols)
# simplificando algunos nombres de las columnas que comienzan con la palabra 'estu'
df.columns = [col.split('_')[1] if col.split('_')[0] == 'estu' else col for col in df.columns ]

# fechanacimiento
df = df[df['fechanacimiento'].isna().replace({True:False, False:True})]
df['fechanacimiento'] = [value.split(' ')[0] for value in df['fechanacimiento']]
df['fechanacimiento'] = pd.to_datetime(df['fechanacimiento'])

# Genero
df['genero'].replace({'M':1,'F':0}, inplace=True)

# Etnia
df['etnia'].replace({'-':'no_etnia','Otro grupo étnico minoritario':'otro', 'Comunidad afrodescendiente':'afro', 'Ninguno':'no_etnia'}, inplace=True)
df['etnia'] = ['otro' if (value != 'no_etnia') and (value != 'afro') else value for value in df['etnia']]

# deepto
df['region'] = df['depto'].replace(dic_depto())
df['depto'] = df['depto'].str.lower()
df['region'] = df['region'].str.lower()

# Estrato
df['fami_estratovivienda'].replace({'Sin Estrato':'Estrato 0'}, inplace=True)
df['fami_estratovivienda'] = [value[-1] for value in df['fami_estratovivienda']]

df[df['fami_estratovivienda'] == '-']['etnia'].value_counts()

df['fami_estratovivienda'].value_counts()

# Educacion Padre 
df['fami_educacionpadre'].replace(dic_educacion(), inplace=True)
df['fami_educacionpadre']


df['fami_educacionpadre'].value_counts()



df.drop(columns=['etnia', 'mcpio',], inplace=True)


df['fechanacimiento'] = [col.split(' ')[0] for col in df['fechanacimiento']]
for i in df.columns:
    print(df[i].value_counts())
    print('--------------')

df.columns

df['fami_educacionpadre']