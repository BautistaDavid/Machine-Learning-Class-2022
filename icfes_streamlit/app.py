import streamlit as st 
import seaborn as sns 
import matplotlib.pyplot as plt 
import pandas as pd 
from matplotlib import rcParams
# from processing_data import data_processing_function

def dic_depto():
    dic = {'BOGOTÁ':'Region Andina','ANTIOQUIA':'Region Andina','VALLE':'Region Pacifica',
    'CUNDINAMARCA':'Region Andina','ATLANTICO':'Region Caribe','SANTANDER':'Region Andina',
    'BOLIVAR':'Region Caribe','CORDOBA':'Region Caribe','NARIÑO':'Region Pacifica',
    'BOYACA':'Region Andina', 'MAGDALENA':'Region Caribe', 'TOLIMA':'Region Andina',
    'NORTE SANTANDER':'Region Andina','HUILA':'Region Andina','CAUCA':'Region Pacifica',
    'CESAR':'Region Caribe','META':'Region Orinoquia','SUCRE':'Region Caribe',
    'RISARALDA':'Region Andina','CALDAS':'Region Andina','LA GUAJIRA':'Region Caribe',
    'QUINDIO':'Region Andina','CASANARE':'Region Orinoquia','CHOCO':'Region Pacifica',
    'CAQUETA':'Region Amazonica','PUTUMAYO':'Region Amazonica','ARAUCA':'Region Orinoquia',
    'GUAVIARE':'Region Orinoquia','AMAZONAS':'Region Amazonica','SAN ANDRES':'Region Caribe',
    'VICHADA':'Region Orinoquia','VAUPES':'Region Amazonica','GUAINIA':'Region Amazonica'}
    return dic  


def dic_educacion():
    dic = {'Secundaria (Bachillerato) completa': 11,
            'Primaria incompleta': 3,
            'Secundaria (Bachillerato) incompleta':8,
            'Primaria completa':5,
            'Educación profesional completa':15,
            'Técnica o tecnológica completa':13,
            'No sabe':0,
            '-':0,
            'Ninguno':0,
            'Técnica o tecnológica incompleta':12,
            'Educación profesional incompleta':14,
            'Postgrado':17,
            'No Aplica':0}
    return dic



def data_processing_function():
    df = pd.read_csv('icfes_streamlit/data_icfes.csv')
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


df = data_processing_function()
df['Region'].replace({'EXTRANJERO':'Extranjero'},inplace=True)




with st.sidebar:
    st.markdown('''
    # Seleccione una de las áreas a evaluar dentro del examen que desea explorar ...
    ''')
    area = st.selectbox(
     '',
     ('Ciencias Naturales', 'Ingles','Lectura Critica','Matemáticas','Sociales Ciudadanas', ''))


st.markdown(
'''
# Análisis Exploratorio Resultados del Examen ICFES Saber 11 - 2019 -II
##### Esta APP desarrolla un breve análisis exploratorio sobre los resultados del examen ICFES Saber 11 del 2019-II.\
 En un principio se realizar una exploración centrada en el comportamiento de las distribuciones del puntaje global\
del examen asociada con diferentes características categóricas de los individuos. Después de esto se buscará analizar \
correlaciones entre los puntajes de cada Área 

### **¿Como están caracterizados estos datos?**

##### Antes de visualizar las distribuciones de los puntajes contrastados con algunas categorías de los individuos es pertinente\
 entender de qué manera dichas categorías conforman la muestra total. A continuación, se utilizarán Tablas y HeatMaps para denotar \
visualmente la participación de cada grupo especificado dentro del total. 

#### Regiones y estratos de vivienda
''')

pivot1 = pd.pivot_table(data = df,index =['Region'], values = 'Puntaje Global' ,columns =['Estrato Vivienda'],aggfunc = 'count')
st.markdown('''\n'''    
)

fig1 = plt.figure(figsize=(9,8))
plt.title('Participación Porcentual de Regiones\n y Estratos de Vivienda', fontsize = 18)
plt.xticks(rotation = 0)
pivot1_heat = sns.heatmap((pivot1 *100)/len(df), cmap="viridis",linewidth=1, linecolor='w', square=True, annot = True,
                          annot_kws={"size":10})

st.pyplot(fig1)

st.markdown('''
\n
##### Como la tabla y el grafico anterior lo permite denotar, la Región Andina representa mas del 50% de los registros del total \
de los datos, y estos en su mayoría focalizados en los estratos Uno, dos y tres. En contraposición, Regiones como la amazónica \
aportan menos del 2% de los registros. Esto en parte da muestra de la misma naturaleza de las estructuras educativas que están \
conformadas a lo largo del país, las cuales dependen de la densidad poblacional de cada territorio. Cabe resaltar que lo más \
probable es que gran parte de los registros que se encuentran dentro de la Región Andina sean de Bogota.DC.   


##### De hecho, demos un vistazo rapido a como están conformadas las participaciones por departamento dentro de la Región Andina.

'''
)

df2 = df[df['Region'] == 'Region Andina']
pivot2 = pd.pivot_table(data = df2,index =['Departamento'], values = 'Puntaje Global' ,columns =['Estrato Vivienda'],aggfunc = 'count')
pivot2 = pivot2[pivot2[6]!=0]
pivot2['Total'] = sum(pivot2[i] for i in range(1,7))
pivot2.index = [i.capitalize() for i in pivot2.index]
fig2 = plt.figure(figsize=(9,8))
plt.title('Participación Porcentual de Departamentos de \nla Region Andina y Estratos de Vivienda', fontsize = 16)
plt.yticks(fontsize = 12)
plt.xticks(rotation = 0)
pivot2_heat = sns.heatmap((pivot2 *100)/len(df2), cmap="viridis",linewidth=1, linecolor='w', square=True, annot = True,
                          annot_kws={"size":10})

st.pyplot(fig2)

st.markdown('''
##### Efectivamente, Bogotá acumula el mayor porcentaje de registros entre todos los departamentos de la Región Andina, \
contando con aproximadamente el 26 % del total de registros de dicha región, por debajo de la capital se encuentran \
importantes departamentos de Colombia como Antioquia con un 22%.

#### Regiones y Genero 

##### Conociendo ya la participación de los subgrupos de regiones y estratos de vivienda podemos ahora interesarnos por la \
participación de los géneros dentro del total de los datos. 

##### Para hacer un análisis detallado podemos nuevamente contrastar los subgrupos que se conforman tanto por los géneros como las regiones, \
aun así, es importante comentar que el total de la muestra analizada está conformado por un 54.2% de Mujeres contra un 45.8% de Hombres. \
Esta razón entre géneros resulta beneficiosa a la hora de plantear algún tipo de modelo de predicción de puntaje usando estos datos y tomando \
esta característica como variable de control. 
''')


pivot3 = pd.pivot_table(data = df,index =['Region'], values = 'Puntaje Global' ,columns =['Genero'],aggfunc = 'count')

fig3 = plt.figure(figsize=(7 ,5))
plt.title('Participación Porcentual de \nGenero por Regiones', fontsize=10)
plt.xticks(rotation=15, fontsize=8)
plt.yticks(fontsize=8)
pivot3_heat = sns.heatmap((pivot3*100)/len(df), cmap="viridis",linewidth=1, linecolor='w', square=True, annot= True,annot_kws={"size":8},)
# pivot3_heat.set_ylabel('Region',fontsize=8)
# pivot3_heat.set_xlabel('Genero',fontsize=8)
st.pyplot(fig3)

st.markdown('''
##### El grafico anterior permite terminar que en todas las regiones y así mismo en el exterior es mayor el peso porcentual de registros que corresponden \
a mujeres que los de hombres, sin embargo se mantiene un balance que puede ser importante como lo mencionábamos anteriormente a la hora de usar estos \
datos en algún modelo de predicción de puntajes. 
''')

st.markdown('''
### Distribuciones del Puntaje Global

##### Habiendo realizado un acercamiento rápido a los subgrupos que conforman los datos se puede ahora analizar las distribuciones del puntaje global sujetos\
a diferentes características.

#### Puntaje Global por Genero
'''
)

fig4 = plt.figure(figsize=(13,7))
plt.yticks(fontsize=22)
plt.xticks(rotation = 0, fontsize=22)
plt.title("BoxPlots del Puntaje Global por Genero", fontsize = 28)
box1 = sns.boxplot(y='Genero',x="Puntaje Global", data=df,palette='rainbow')
box1.set_xlabel('Puntaje Global',fontsize=25)
box1.set_ylabel('Genero',fontsize=25)
st.pyplot(fig4)

stat_hombre = df[df['Genero'] == 'Hombre']['Puntaje Global'].describe()
stat_mujer = df[df['Genero'] == 'Mujer']['Puntaje Global'].describe()

stat = pd.DataFrame({'Hombre':stat_hombre,
                    'Mujer': stat_mujer})
stat.drop('count',inplace=True)
st.write(stat.T)

st.markdown('''
_
##### El Boxplot y la tabla anterior permite denotar las diferencias entre las distribuciones del puntaje entre Géneros, se puede notar que los hombres presentan \
un promedio aproximadamente 8 puntos más altos que las mujeres, así miamo la distribución tiende a estar más a la derecha, de manera que tanto los cuartiles como el \
punto mínimo y máximo están unos puntos por encima.

### Distribuciones de Puntajes Areas Especificas por Región y Genero

#### Lectura Critica
''')

fig5 = plt.figure(figsize=(12,5))
plt.yticks(fontsize=22)
plt.xticks(rotation = 0, fontsize=22)
boxfig5 = sns.boxplot(x='Puntaje Lectura Critica',y='Genero', data=df, palette='rainbow')
boxfig5.set_xlabel('Puntaje Lectura Critica',fontsize=25)
boxfig5.set_ylabel('Genero',fontsize=25)
st.pyplot(fig5)


st.markdown('''
#### Matematicas
''')
fig6 = plt.figure(figsize=(12,5))
plt.yticks(fontsize=22)
plt.xticks(rotation = 0, fontsize=22)
boxfig6 = sns.boxplot(x='Puntaje Matematicas',y='Genero', data=df, palette='rainbow')
boxfig6.set_xlabel('Puntaje Matematicas',fontsize=25)
boxfig6.set_ylabel('Genero',fontsize=25)
st.pyplot(fig6)

st.markdown('''
#### Ciencias Naturales
''')
fig7 = plt.figure(figsize=(12,5))
plt.yticks(fontsize=22)
plt.xticks(rotation = 0, fontsize=22)
boxfig7 = sns.boxplot(x='Puntaje Ciencias Naturales',y='Genero', data=df, palette='rainbow')
boxfig7.set_xlabel('Puntaje Ciencias Naturales',fontsize=25)
boxfig7.set_ylabel('Genero',fontsize=25)
st.pyplot(fig7)

st.markdown('''
#### Sociales Ciudadanas
''')
fig8 = plt.figure(figsize=(12,5))
plt.yticks(fontsize=22)
plt.xticks(rotation = 0, fontsize=22)
boxfig8 = sns.boxplot(x='Puntaje Sociales Ciudadanas',y='Genero', data=df, palette='rainbow')
boxfig8.set_xlabel('Puntaje Sociales Ciudadanas',fontsize=25)
boxfig8.set_ylabel('Genero',fontsize=25)
st.pyplot(fig8)

st.markdown('''
#### Ingles
''')
fig9 = plt.figure(figsize=(12,5))
plt.yticks(fontsize=22)
plt.xticks(rotation = 0, fontsize=22)
boxfig9 = sns.boxplot(x='Puntaje Ingles',y='Genero', data=df, palette='rainbow')
boxfig9.set_xlabel('Puntaje Ingles',fontsize=25)
boxfig9.set_ylabel('Genero',fontsize=25)
st.pyplot(fig9)











fig5 = plt.figure(figsize=(12,5))
plt.xticks(rotation = 15)
boxfig5 = sns.boxplot(y='Puntaje Lectura Critica',x='Region',hue ='Genero' ,data=df)
st.pyplot(fig5)





scores = df[['Puntaje Lectura Critica','Puntaje Matematicas','Puntaje Ciencias Naturales','Puntaje Sociales Ciudadanas','Puntaje Ingles']]

















if area == 'Ciencias Naturales':
    fig_naturales= plt.figure(figsize=(8, 6)) 
    sns.set(style='whitegrid', rc={"grid.linewidth": 0.1})  
    sns.set_context("notebook", font_scale=1.25)            
    rcParams['axes.titlepad'] = 20                          
    fig_naturales.suptitle('Distribución del puntaje por Genero', y=1.01, fontsize=16, fontstyle ='oblique')
    ax1 = fig_naturales.add_subplot(1,1,1)
    fig_nat = sns.violinplot(data=df,y='punt_c_naturales', x='estu_genero', ax=ax1)
    fig_nat.set_xlabel("Genero", fontsize = 16)
    fig_nat.set_ylabel("Puntaje Ciencias Naturales", fontsize = 16)
    plt.show()
    st.pyplot(fig_naturales)

    st.markdown('### Genero vs ... ')
    desp = st.selectbox('',['cole_jornada','cole_caracter'])

    fig_naturales2= plt.figure(figsize=(15, 6)) 
    sns.set(style='whitegrid', rc={"grid.linewidth": 0.1})  
    sns.set_context("notebook", font_scale=1.25)            
    rcParams['axes.titlepad'] = 20                          
    fig_naturales2.suptitle('Distribución del puntaje por Genero', y=1.01, fontsize=16, fontstyle ='oblique')
    ax1 = fig_naturales2.add_subplot(1,1,1)
    fig_nat = sns.violinplot(data=df,y='punt_c_naturales', x=desp,hue='estu_genero', ax=ax1)
    fig_nat.set_xlabel("Genero", fontsize = 16)
    fig_nat.set_ylabel("Puntaje Ciencias Naturales", fontsize = 16)
    st.pyplot(fig_naturales2)

    
