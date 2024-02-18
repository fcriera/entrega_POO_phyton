class Dia:
    # Inicio el programa
    def __init__(self, anio = 1970, mes = 1, dia = 1):
        self.anio = anio
        self.mes = mes
        self.dia = dia 
        self.validar_fecha(anio, mes ,dia)
        self.dia_semana = self.zeller(anio, mes, dia)
            
    # información de la fecha
    def info(self):
        return print(f"la fecha es {self.nombre_de_dia(self.dia_semana)} {self.dia} de {self.nombre_de_mes(self.mes)}, del año {self.anio}")

    # define si un año es bisiesto
    def anio_bisiesto(self):
        es_bisiesto = False
        if (self.anio % 4 == 0) and (not self.anio % 100 == 0 or self.anio % 400 == 0):
            es_bisiesto = True
        return es_bisiesto
    
    # Creo mis values error para cada uno de los casos que ingrese mal un dato
    def validar_fecha(self, anio, mes, dia):
        if anio < 0:
                raise ValueError("Ingresar un año D.C.")    
        if mes <1 or mes > 12:
            raise ValueError("Ingresar un mes válido") 
        if self.anio_bisiesto():
            list_dias = [31,29,31,30,31,30,31,31,30,31,30,31]
            if dia < 1 or dia > list_dias[mes-1]:
                raise ValueError("Ingresar un día que exista")
        else:
            list_dias = [31,28,31,30,31,30,31,31,30,31,30,31]     
            if dia < 1 or dia > list_dias[mes-1]:
                raise ValueError("Ingresar un día que exista")
        
        return True

    # algortimo de zeller, calculo el dia de la semana
    def zeller(self, anio, mes, dia):
        a = int((14 - mes) / 12)
        y = anio - a
        m = int(mes + (12 * a) - 2)
        d = int(dia + y + int(y/4) - int(y/100) + int(y/400)+((31*m) / 12)) % 7
        return d

    # retorna el nombre del día asignado en zeller
    def nombre_de_dia(self, numero_dia):
        return ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"][numero_dia]

    # nos devuelve el nombre del mes    
    def nombre_de_mes(self, numero_mes):
        return ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"][(numero_mes-1)]