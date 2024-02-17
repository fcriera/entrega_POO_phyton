from functions import Clase_dia
def test_inicio():
    d = Clase_dia(2023,11,4)
    assert d.año == 2023
    assert d.mes == 11
    assert d.dia == 4
