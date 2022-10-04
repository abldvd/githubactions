"""
    Este módulo contiene el preprocesamiento de datos
"""
import numpy as np

def get_numerical_features(df):
    """Devuelve una lista con el nombre de las columnas
    que contienen datos de tipo numérico
    
    Parámetros
    ----------
    
    df: dataframe

    Ejemplos
    --------

    >>> from  modeltools.preprocessing import get_numerical_features
    >>> import pandas as pd
    >>> df = pd.DataFrame({"a":[1]})
    >>> get_numerical_features(df)
    ['a']
    """
    return list(df.select_dtypes(include=[np.number]).columns)
