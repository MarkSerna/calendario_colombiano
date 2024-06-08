import unittest
from datetime import date
from calendario_colombiano.calendario import CalendarioColombiano

class TestCalendarioColombiano(unittest.TestCase):
    def setUp(self):
        self.calendario = CalendarioColombiano()
    
    def test_festivos_fijos(self):
        festivos_2024 = self.calendario.obtener_festivos(2024)
        self.assertIn(date(2024, 1, 1), festivos_2024) # Año Nuevo
        self.assertIn(date(2024, 5, 1), festivos_2024) # Día del Trabajo
        
    def test_festivos_moviles(self):
        festivos_2024 = self.calendario.obtener_festivos(2024)
        self.assertIn(date(2024, 3, 28), festivos_2024) # Jueves Santo
        self.assertIn(date(2024, 3, 29), festivos_2024) # Viernes Santo
        
    