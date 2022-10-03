import pandas as pd
from modeltools.preprocessing import get_numerical_features

def test_get_numerical_features_simple():
    """Probamos que logra distinguir entre cadenas de
     texto y numeros enteros"""

    df = pd.DataFrame({
        "numerica": [5],
        "categorica": ["rojo"]
    })
    assert get_numerical_features(df) == ["numerica"]


def test_get_numerical_features_empty():
    """Este test comprueba que se devuelve una lista 
    vacia si no hay variable num"""

    df = pd.DataFrame({
        "numerica": ["no hay"],
        "categorica": ["rojo"]
    })
    assert get_numerical_features(df) == []


def test_get_numerical_features_withoutname():
    """Este test comprueba que funciona correctamente 
    cuando hay columnas numéricas sin nombre"""
    
    df = pd.DataFrame(
        [[1,"a"]]
    )
    assert get_numerical_features(df) == [0]




def test_get_numerical_features_zero_columns():
    """ Este test comprueba que se devuelve una variable si el 
    DF tiene una variable numérica pero ninguna columna"""
    assert get_numerical_features(pd.DataFrame()) == []


def test_get_numerical_features_zero_rows():
    """ Este test comprueba que se devuelve algo si el 
    DF tiene una variable numérica pero ninguna fila"""
    df = pd.DataFrame({
    "numerica": pd.Series(dtype=int)
    })
    assert get_numerical_features(df) == ["numerica"]


def test_get_numerical_features_int_and_float():
    """Este test comprueba que funciona correctamente cuano 
    hay una columna integer y una flotante"""

    df = pd.DataFrame({
        "entero": [5],
        "flotante": [5.1],
        "categorica": ["rojo"]
    })
    assert get_numerical_features(df) == ["entero", "flotante"]


def test_get_numerical_features_complex():
    """Este test comprueba que funciona correctamente con números complejos"""

    df = pd.DataFrame({
        "numerica": [5],
        "complejos": [5+1j],
        "categorica": ["rojo"]
    })
    assert get_numerical_features(df) == ["numerica", "complejos"]