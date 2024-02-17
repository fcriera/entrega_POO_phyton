class Dia:
    def __init__(self, anio = 1970, mes = 1, dia = 1):
            self.validar_fecha(anio, mes, dia)
            self.anio = anio
            self.mes = mes
            self.dia = dia 
            self.dia_semana = self.zeller(anio, mes, dia)
            

    def anio_bisiesto(self):
        es_bisiesto = False
        if (self.anio % 4 == 0) and (not self.anio % 100 == 0 or self.anio % 400 == 0):
            es_bisiesto = True
        return es_bisiesto
    
    def validar_fecha(self, anio, mes, dia):
        if anio < 0:
            raise ValueError("Ingresar un año D.C.")
        if mes <1 or mes > 12:
            raise ValueError("Ingresar un mes válido")
        if dia < 0 or dia > 31: 
            raise ValueError("Ingresar un día que exista")
        return True

    def zeller(self, anio, mes, dia):
        a = int((14 - mes) / 12)
        y = anio - a
        m = int(mes + (12 * a) - 2)
        d = int(dia + y + int(y/4) - int(y/100) + int(y/400)+((31*m) / 12)) % 7
        return d

    def nombre_de_dia(self, numero_dia):
        return ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"][numero_dia]
        
