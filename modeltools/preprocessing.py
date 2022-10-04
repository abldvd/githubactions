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
    
    >>> df = pd.DataFrame([[1,"a"]])
    >>> get_numerical_features(df)
    [0]

    >>> df = pd.DataFrame({"a": [" "]})
    >>> get_numerical_features(df)
    []

    >>> get_numerical_features(pd.DataFrame())
    []

    >>> df = pd.DataFrame({"a": pd.Series(dtype=int)})
    >>> get_numerical_features(df)
    ['a']

    >>> df = pd.DataFrame({"int": [1],"float": [1.]})
    >>> get_numerical_features(df)
    ['int', 'float']



    """
    return list(df.select_dtypes(include=[np.number]).columns)
