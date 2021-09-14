class FiguraGeometrica:
    def __init__(self, alto, ancho):
        if self._validacion(alto):
            self._alto = alto
        else:
            self._alto = 0
            print(f'Valor fuera de rango {alto}')
        if self._validacion(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f'Valor fuera de rango {ancho}') 

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if self._validacion(alto):
            self._alto = alto
        else:
            print(f'Valor fuera de rango {alto}')


    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        if self._validacion(ancho):
            self._ancho = ancho
        else:
            print(f'Valor fuera de rango {ancho}')

    
    def __str__(self):
        return f'Figura geometrica: ancho: {self.alto} - alto: {self.ancho}'

    def _validacion(self, valor):
        return True if 1 < valor < 100 else False