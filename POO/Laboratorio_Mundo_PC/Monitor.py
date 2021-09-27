from Laboratorio_Mundo_PC.Dispositivos_Salida import dispositivosSalida

class Monitor(dispositivosSalida):
    def __init__(self, marca, tipoEntrada, tamanio):
        super().__init__(marca, tipoEntrada)
        self._tamanio = tamanio

    @property
    def tamanio(self):
        return self._tamanio
    @tamanio.setter
    def tamanio(self, tamanio):
        self._tamanio = tamanio


    def __str__(self):
        return f'{self._marca} - {self._tipoEntrada} - {self._tamanio}'




monitor1 = Monitor('HP', 'HDMI', '22 Pulgadas')
monitor2 = Monitor('LG', 'VGA', '27 pulgadas')
