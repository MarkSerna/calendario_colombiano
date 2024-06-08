import datetime
from datetime import timedelta

class Calendariocolombiano:
    def __init__(self):
        self.festivos_fijos = [
            (1, 1),  # Año Nuevo
            (5, 1),  # Día del Trabajo
            (7, 20),  # Grito de Independencia
            (8, 7),  # Batalla de Boyacá
            (12, 8),  # Inmaculada Concepción
            (12, 25),  # Navidad
        ]
        
    def _es_lunes(self, fecha):
        return fecha.weekday() == 0
    
    def _proximo_lunes(self, fecha):
        return fecha + timedelta(days=(7 - fecha.weekday()))
    
    def _calcular_pascua(self, año):
        # Algoritmo de Butcher
        a = año % 19
        b = año // 100
        c = año % 100
        d = b // 4
        e = b % 4
        f = (b + 8) // 25
        g = (b - f + 1) // 3
        h = (19 * a + b - d - g + 15) % 30
        i = c // 4
        k = c % 4
        l = (32 + 2 * e + 2 * i - h - k) % 7
        m = (a + 11 * h + 22 * l) // 451
        mes = (h + l - 7 * m + 114) // 31
        dia = ((h + l - 7 * m + 114) % 31) + 1
        return datetime.date(año, mes, dia)
    
    def _calcular_festivos_moviles(self, año):
        pascua = self._calcular_pascua(año)
        festivos_moviles = [
            (pascua + timedelta(days=-3)),  # Jueves Santo
            (pascua + timedelta(days=-2)),  # Viernes Santo
            (pascua + timedelta(days=43)),  # Ascensión de Jesús
            (pascua + timedelta(days=64)),  # Corpus Christi
            (pascua + timedelta(days=71)),  # Sagrado Corazón
        ]
        return festivos_moviles
    
    def _calcular_festivos_colombianos(self, año):
        festivos = []
        for mes, dia in self.festivos_fijos:
            fecha = datetime.date(año, mes, dia)
            if self._es_lunes(fecha):
                festivos.append(fecha)
            else:
                festivos.append(self._proximo_lunes(fecha))
                
        festivos.extend(self._calcular_festivos_moviles(año))
        return festivos
    
    def es_festivo(self, fecha):
        año = fecha.year
        festivos = self._calcular_festivos_colombianos(año)
        return fecha in festivos
    
    def obtener_festivos(self, año):
        return self._calcular_festivos_colombianos(año)