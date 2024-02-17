from functions import Dia



anio = int(input("Ingresar año: "))

mes = int(input("Ingresar mes: "))
dia = int(input("Ingresar día: "))
d = Dia(anio, mes, dia)
'''
fecha_valida = False
while not fecha_valida:
    try:
        fecha_valida = d.validar_fecha(anio, mes , dia)
    except:
        fecha_valida = False
        anio = int(input("Ingresar año: "))
        mes = int(input("Ingresar mes: "))
        dia = int(input("Ingresar día: "))
'''

print(f"la fecha es {d.nombre_de_dia(d.dia_semana)}  del mes {d.mes}, del año {d.anio}")