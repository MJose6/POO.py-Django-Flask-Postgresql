from Laboratorio_Mundo_PC.Mouse import Mouse
from Laboratorio_Mundo_PC.Teclado import Teclado
from Laboratorio_Mundo_PC.Monitor import Monitor
from Laboratorio_Mundo_PC.Parlantes import Parlantes


class Computadora:
    def __init__(self, gabinete, cpu, gpu, fuente, disco, mouse, teclado, monitor, parlantes):
        self._gabinete = gabinete
        self._cpu = cpu
        self._gpu = gpu
        self._fuente = fuente
        self._disco = disco
        self._mouse = mouse
        self._teclado = teclado
        self._monitor = monitor
        self._parlantes = parlantes

    @property
    def gabinete(self):
        return self._gabinete
    @gabinete.setter
    def gabinete(self, gabinete):
        self._gabinete = gabinete

    @property
    def cpu(self):
        return self._cpu
    @cpu.setter
    def cpu(self, cpu):
        self._cpu = cpu

    @property
    def gpu(self):
        return self._gpu
    @gpu.setter
    def gpu(self, gpu):
        self._gpu = gpu

    @property
    def fuente(self):
        return self._fuente
    @fuente.setter
    def fuente(self, fuente):
        self._fuente = fuente

    @property
    def disco(self):
        return self._disco
    @disco.setter
    def disco(self, disco):
        self._disco = disco

    def __str__(self):
        return f'''
        Gabinete: {self._gabinete}
        Procesador: {self._cpu}
        Video: {self._gpu}
        Alimentacion: {self._fuente}
        Almacenamiento: {self._disco}
        Mouse: {self._mouse}
        Teclado: {self._teclado}
        Monitor: {self._monitor}
        Parlantes: {self._parlantes}
        '''



raton1 = Mouse('Logitech', 'usb')
raton2 = Mouse('Genius', 'Bluetooth')
teclado1 = Teclado('Logitech', 'USB')
teclado2 = Teclado('Genius', 'Bluetooth')
monitor1 = Monitor('HP', 'HDMI', '22 Pulgadas')
monitor2 = Monitor('LG', 'VGA', '27 pulgadas')
parlante1 = Parlantes('Noga', 'USB', '8 Watts')
parlante2 = Parlantes('Genius', 'Jack 3.5', '4 Watts')
computadora1 = Computadora('Cougar', 'Intel i5 11400', 'Nvidia gtx 1060ti OC 6GB', 'Termaltake 600w 80Plus Gold', 'Kingston SSD 500GB', raton1, teclado1, monitor1, parlante1)
computadora2 = Computadora('Sentey', 'Ryzen 5 3500x', 'Radeon RX 570 OC 4Gb', 'GIGABYTE 500w 80Plus Gold', 'Cucial SSD 240GB', raton2, teclado2, monitor2, parlante2)
