from Laboratorio_Mundo_PC.Dispositivos_Salida import dispositivosSalida

class Parlantes(dispositivosSalida):
    def __init__(self, marca, tipoEntrada, potencia):
        super().__init__(marca, tipoEntrada)
        self._potencia = potencia

    @property
    def potencia(self):
        return self._potencia
    @potencia.setter
    def potencia(self, potencia):
        self._potencia = potencia

    def __str__(self):
        return f'{self._marca} - {self._tipoEntrada} - {self._potencia}'




parlante1 = Parlantes('Noga', 'USB', '8 Watts')
parlante2 = Parlantes('Genius', 'Jack 3.5', '4 Watts')
