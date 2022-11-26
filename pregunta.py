    """
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------
Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.
"""
import pandas as pd

def limpiar_fecha(linea):
    linea = linea.split("/")
    if(len(linea[0]) < 3):
        aux = linea[0]
        linea[0] = linea[2]
        linea[2] = aux
    joined = "/".join(linea)
    return joined

def clean_data():
    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    df.drop(df.columns[0], inplace=True, axis=1)

    #df.drop_duplicates(inplace=True) # Eliminar duplicados
    df.dropna(inplace=True) # Eliminar vacios

    # Minusculas
    df['sexo'] = df['sexo'].str.lower() 
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.lower()
    df['idea_negocio'] = df['idea_negocio'].str.lower() 
    df['barrio'] = df['barrio'].str.lower() 
    df['línea_credito'] = df['línea_credito'].str.lower()

    # Limpieza de strings
    df.idea_negocio = df.idea_negocio.str.replace('-',' ')
    df.idea_negocio = df.idea_negocio.str.replace('_',' ')
    df.idea_negocio = df.idea_negocio.str.strip()

    df.barrio = df.barrio.str.replace('-',' ')
    df.barrio = df.barrio.str.replace('_',' ')
    #df.barrio = df.barrio.str.strip()

    df.línea_credito = df.línea_credito.str.replace('-',' ')
    df.línea_credito = df.línea_credito.str.replace('_',' ')
    df.línea_credito = df.línea_credito.str.strip()

    # Tipos
    df.comuna_ciudadano = df.comuna_ciudadano.astype(float)

    # Fecha
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].apply(limpiar_fecha)
    df['fecha_de_beneficio'] = pd.to_datetime(df.fecha_de_beneficio, format='%Y/%m/%d')
    # df.fecha_de_beneficio = df.fecha_de_beneficio.apply(lambda x : pd.to_datetime(x, format="%Y/%m/%d") if re.match('^\d{4}/', x) else pd.to_datetime(x, format="%d/%m/%Y"))

    # # Monto
    df.monto_del_credito = df.monto_del_credito.str.replace('$',"")
    df.monto_del_credito = df.monto_del_credito.str.replace(' ',"")
    df.monto_del_credito = df.monto_del_credito.str.replace(',',"")
    df['monto_del_credito'] = df['monto_del_credito'].str.replace('\.00',"")
    df.monto_del_credito = df.monto_del_credito.astype(int)

    # Final
    df.dropna(inplace=True) # Eliminar vacios
    df.drop_duplicates(inplace=True) # Eliminar duplicados

    return df
