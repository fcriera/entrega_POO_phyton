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

def zeller(anio, mes, dia):
        a = int((14 - mes) / 12)
        y = anio - a
        m = int(mes + (12 * a) - 2)
        d = int(dia + y + int(y/4) - int(y/100) + int(y/400)+((31*m) / 12)) % 7
        return d

def nombre_de_dia(numero_dia):
    return ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"][numero_dia]
print (zeller(2024,2,17))
print(nombre_de_dia(zeller(2024,2,17)))
