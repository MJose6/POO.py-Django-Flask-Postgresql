class Vehiculo:
    def __init__(self, color, ruedas):
        self._color = color
        self._ruedas = ruedas

    def __str__(self):
        return f'Color: {self._color} - Ruedas: {self._ruedas}'

class Coche(Vehiculo):
    def __init__(self, _color, _ruedas, velocidad):
        super().__init__(_color, _ruedas)
        self._velocidad = velocidad


    def __str__(self):
        return f'Vehiculo: {super().__str__()} - Velocidad: {self._velocidad} Km/h'

class Bicicleta(Vehiculo):
    def __init__(self, _color, _ruedas, velocidad):
        super().__init__(_color, _ruedas)
        self._velocidad = velocidad


    def __str__(self):
        return f'Vehiculo: {super().__str__()} - Velocidad: {self._velocidad} Km/h'

vehiculo1 = Vehiculo('Amarillo', 4)
print(vehiculo1)
coche1 = Coche('Rojo', 4, 100)
print(coche1)
bicicleta1 = Bicicleta('Azul', 2, 20)
print(bicicleta1)