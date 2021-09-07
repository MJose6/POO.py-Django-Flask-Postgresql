class Rectangulo:
    """
        Clase para calcular area de un rectangulo
    """
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura

numero1 = float(input("Proporcione la base del rectangulo: "))
numero2 = float(input("Proporcione la altura del rectangulo: "))

rectangulo1 = Rectangulo(numero1, numero2)
print(f'El area del rectangulo es: {rectangulo1.calcularArea():.2f}')