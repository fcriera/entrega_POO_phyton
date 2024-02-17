from functions import Dia


d = Dia()
d.anio = int(input("Ingresar año: "))
Dia.validar_fecha(d, d.anio, d.mes, d.dia)
    
d.mes = int(input("Ingresar mes: "))
Dia.validar_fecha(d, d.anio, d.mes, d.dia)

d.dia = int(input("Ingresar día: "))
Dia.validar_fecha(d, d.anio, d.mes, d.dia)

d = Dia(d.anio, d.mes, d.dia)

print(f"la fecha es {d.nombre_de_dia(d.dia_semana)} {d.dia} de {d.nombre_de_mes(d.mes)}, del año {d.anio}")