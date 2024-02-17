from functions import Dia
def test_inicio():
    d = Dia()
    assert d.anio == 1970
    assert d.mes == 1
    assert d.dia == 1

    d = Dia(2023,11,4)
    assert d.anio == 2023
    assert d.mes == 11
    assert d.dia == 4 
    
def test_validar_fechas_correctas():
    d = Dia(-1,-1,33)
    print(d.anio)