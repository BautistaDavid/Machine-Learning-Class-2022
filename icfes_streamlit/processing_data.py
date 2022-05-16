from math import floor
from utils import dic_depto
import pandas as pd
import seaborn as sns 

def data_processing_function():
    df = pd.read_csv('data_icfes.csv')
# Creamos y modificamos algunas variables 
    df['region'] = df['estu_depto_reside'].replace(dic_depto())

    df['edad'] = [2020 - int(value.split('/')[2]) for value in df['estu_fechanacimiento']]
    df['edad'].replace({edad:int(df['edad'].mean()) for edad in [2018,2019,5,110,120,2,1,9,6,3,4,7,8,11,10]},inplace=True)

    df['estu_genero'].replace({1:'Hombre',0:'Mujer'}, inplace=True)
    df.drop(columns=['estu_fechanacimiento'],inplace=True)

    for col in ['fami_tieneinternet', 'fami_tieneserviciotv', 'fami_tienecomputador', 'fami_tieneautomovil','fami_tieneconsolavideojuegos']:
        df[col].replace({'0':'No'},inplace=True)

    cols_category = ['estu_genero','estu_etnia','estu_depto_reside','fami_tieneinternet', 'fami_tieneserviciotv',
        'fami_tienecomputador', 'fami_tieneautomovil','fami_tieneconsolavideojuegos', 'estu_dedicacionlecturadiaria',
        'estu_dedicacioninternet', 'estu_horassemanatrabaja', 'cole_genero','cole_naturaleza', 'cole_bilingue', 'cole_caracter',
        'cole_area_ubicacion', 'cole_jornada','region']

    for col in cols_category:
        df[col] = df[col].astype('category')

    cols_int_8 = ['fami_estratovivienda', 'fami_educacionpadre','fami_educacionmadre','punt_lectura_critica','percentil_lectura_critica', 'punt_matematicas','percentil_matematicas', 'punt_c_naturales', 'percentil_c_naturales',
    'punt_sociales_ciudadanas', 'percentil_sociales_ciudadanas','punt_ingles', 'percentil_ingles', 'percentil_global','edad']

    for col in cols_int_8:
        df[col] = df[col].astype('int8')
   
    df.columns = ['Genero','Etnia','Departamento','Estrato Vivienda','Educacion Padre','Educacion Madre','Internet','Television','Computadora','Automovil','Consola de Juegos',
               'Lectura Diaria','Tiempo Internet', 'Horas Trabajo Semanal','Genero Colegio', 'Categoria Colegio', 'Colegio Bilingue','Tipo Colegio','Sector Colegio','Jornada Colegio',
               'Puntaje Lectura Critica', 'perct_lectura_critica','Puntaje Matematicas', 'percentil_matematicas','Puntaje Ciencias Naturales','percentil_c_naturales',
               'Puntaje Sociales Ciudadanas','percentil_sociales_ciudadanas','Puntaje Ingles','percentil_ingles','Puntaje Global','percentil_global','Region','Edad' ]

    df = df[df['Puntaje Global']>5]
    return df




