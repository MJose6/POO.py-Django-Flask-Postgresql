from dominio.Pelicula import Pelicula
from servicio.Catalogo_Peliculas import CatalogoPeliculas as cp

opcion = None

while opcion != 4:
    try:
        print('Opciones:')
        print('1: Agregar pelicula')
        print('2: Listar peliculas')
        print('3: Eliminar pelicula')
        print('4: Salir')
        opcion = int(input('Escribe la opcion (1-4): '))

        if opcion == 1:
            nombrePelicula = input('Ingrese el nombre de la pelicula que desea agregar: ')
            pelicula = Pelicula(nombrePelicula)
            cp.agregarPelicula(pelicula)

        elif opcion == 2:
            cp.listarPeliculas()

        elif opcion == 3:
            cp.eliminarPeliculas()

    except Exception as e:
        print(f'Ocurrio un error, vuelva a intentarlo {e}')
        opcion = True

else:
    print('Salio del programa, gracias.')