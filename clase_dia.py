from functions import Dia

#d = Dia()
#d.info()

anio = int(input("Ingresar año: "))
#d.validar_fecha(d.anio, d.mes, d.dia)
    
mes = int(input("Ingresar mes: "))
#d.validar_fecha(d.anio, d.mes, d.dia)

dia = int(input("Ingresar día: "))
#d.validar_fecha(d.anio, d.mes, d.dia)

d = Dia(anio, mes, dia)

d.info()