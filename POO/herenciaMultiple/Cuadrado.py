from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcularArea(self):
        return self.alto * self.ancho

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'

lado = int(input('Ingrese la medida de un lado del cuadrado: '))
color = input('Ingrese el color del cuadrado: ')
cuadrado1 = Cuadrado(lado, color)
print(f'{cuadrado1} - Area del cuadrado: {cuadrado1.calcularArea()}')