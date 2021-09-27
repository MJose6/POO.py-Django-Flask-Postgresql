from Laboratorio_Mundo_PC.Dispositivos_Entrada import dispositivoEntrada

class Mouse(dispositivoEntrada):
    def __init__(self, marca, tipoEntrada):
        super().__init__(marca, tipoEntrada)

    def __str__(self):
        return f'{self._marca} - {self._tipoEntrada}'




raton1 = Mouse('Logitech', 'usb')
raton2 = Mouse('Genius','Bluetooth')