from Laboratorio_Mundo_PC.Computadora import Computadora
from Laboratorio_Mundo_PC.Monitor import Monitor
from Laboratorio_Mundo_PC.Mouse import Mouse
from Laboratorio_Mundo_PC.Parlantes import Parlantes
from Laboratorio_Mundo_PC.Teclado import Teclado
from Laboratorio_Mundo_PC.Pedido import Pedido


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


lista1 = [computadora1]
lista2 = [computadora2]
pedido1 = Pedido(lista1)
pedido2 = Pedido(lista2)
print(pedido1, pedido2)