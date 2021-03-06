def dic_latitud():
    dic = {'BOGOTA':4.60971,'ANTIOQUIA':6.25184,'VALLE DEL CAUCA':3.43722,
    'ATLANTICO':10.96854,'SANTANDER':7.12539,'BOLIVAR':10.39972,'CORDOBA':8.74798,
    'NARIÑO':1.21361,'BOYACA':5.53528, 'MAGDALENA':11.24079, 'TOLIMA':4.43889,
    'NORTE DE SANTANDER':7.89391,'HUILA':2.9273,'CAUCA':2.43823,
    'CESAR':10.46314,'META':4.142,'SUCRE':9.30472,
    'RISARALDA':4.81333,'CALDAS':5.06889,'LA GUAJIRA':11.54444,
    'QUINDIO':4.53389,'CASANARE':5.33775,'CHOCO':5.69188,
    'CAQUETA':1.61438,'SAN ANDRES':12.58317}
    return dic  

def dic_longitud():
    dic = {'BOGOTA':-74.08175,
           'ANTIOQUIA':-75.56359,'VALLE DEL CAUCA':-76.5225,
    'ATLANTICO':-74.78132,'SANTANDER':-73.1198,'BOLIVAR':-75.51444,'CORDOBA':-75.88143,
    'NARIÑO':-77.28102,'BOYACA':-73.36778, 'MAGDALENA':-74.19904, 'TOLIMA':-75.23222,
    'NORTE DE SANTANDER':-72.50782,'HUILA':-75.28189,'CAUCA':-76.61316,
    'CESAR':-73.25322,'META':-73.62664,'SUCRE':-75.39778,
    'RISARALDA':-75.69611,'CALDAS':-75.51738,'LA GUAJIRA':-72.90722,
    'QUINDIO':-75.68111,'CASANARE':-72.39586,'CHOCO':-76.65835,
    'CAQUETA':-75.60623,'SAN ANDRES':-81.70636}
    return dic

df_viajeros = df[df['viaje'] == 1]
# df_viajeros['area'] = df_viajeros['area'].str.upper()

df_viajeros['latitud'] = df_viajeros['area'].replace(dic_latitud()) 
df_viajeros['longitud'] = df_viajeros['area'].replace(dic_longitud()) 
