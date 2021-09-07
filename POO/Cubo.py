class Cubo:
    """
        Clase para calcular volumen de un cubo
    """
    def __init__(self, alto, ancho, profundidad):
        self.alto = alto
        self.ancho = ancho
        self.profundidad = profundidad

    def calcularVolumen(self):
        return self.alto * self.ancho * self.profundidad

numero1 = float(input("Proporcione la altura del cubo: "))
numero2 = float(input("Proporcione el ancho del cubo: "))
numero3 = float(input("Proporcione la profundidad del cubo: "))

cubo1 = Cubo(numero1, numero2, numero3)
print(f'El volumen del cubo es: {cubo1.calcularVolumen():.2f}')