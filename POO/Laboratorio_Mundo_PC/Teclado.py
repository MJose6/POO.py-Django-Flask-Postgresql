from Laboratorio_Mundo_PC.Dispositivos_Entrada import dispositivoEntrada

class Teclado(dispositivoEntrada):
    def __init__(self, marca, tipoEntrada):
        super().__init__(marca, tipoEntrada)

    def __str__(self):
        return f'{self._marca} - {self._tipoEntrada}'



teclado1 = Teclado('Logitech', 'USB')
teclado2 = Teclado('Genius','Bluetooth')
