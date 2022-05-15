import streamlit as st 
import time
import streamlit.components.v1 as components
import seaborn as sns 
import matplotlib.pyplot as plt 
import pandas as pd 

df = pd.read_csv('data/data_icfes.csv')

with st.sidebar:
    st.markdown('''
    # Seleccione una de las áreas a evaluar dentro del examen que desea explorar ...
    ''')
    area = st.selectbox(
     '',
     ('Ciencias Naturales', 'Ingles','Lectura Critica','Matemáticas','Sociales Ciudadanas', ''))


st.markdown(f'''
# Análisis Exploratorio Resultados del Examen ICFES Saber 11 - 2019 -II
#### A continuación, se presentan un reporte de estadísticos descriptivos según la categoría seleccionada en la SideBar de esta App.

''')
st.markdown(f'''
## Área seleccionada: {area}''')

if area == 'Ciencias Naturales':
    fig_naturales = sns.boxplot(data=df,x='punt_c_naturales')
    st.pyplot(fig_naturales)
