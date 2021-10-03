import psycopg2

conexion = psycopg2.connect(user='postgres', password='admin', host="127.0.0.1", port='5432', database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:

            #Consulta

            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
            entrada = 1,2,3
            llavesPrimarias = (tuple(entrada),)
            cursor.execute(sentencia, llavesPrimarias)
            registro = cursor.fetchall()
            for registros in registro:
                print(registros)

            #Insertar valor a BD

            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
            valores = ('Roberto', 'Perez', 'Rperez@mail.com')
            cursor.execute(sentencia, valores)
            '''cursor.executemany() en caso de querer agregar varios valores realizando una tupla de tuplas en variable valores, 
            conexion.commit() guardar cambios en BD siempre y cuando no se use el manejo de recursos con with'''
            registroInsertado = cursor.rowcount
            print(f'Registros insertados: {registroInsertado}, {valores}')

            #Actualizar registros

            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = (('Raul', 'Olivera', 'Rolivera@mail.com', 5),
                       ('Sergio', 'Sanchez', 'Ssanchez@mail.com', 6),
                       )
            cursor.executemany(sentencia, valores)
            registrosActualizados = cursor.rowcount
            print(f'Registros actualizados: {registrosActualizados}')

            #Eliminar valores

            sentencia = 'DELETE FROM persona WHERE id_persona=%s'
            valores = (7,)
            cursor.execute(sentencia, valores)
            registrosEliminados = cursor.rowcount
            print(f'Registros eliminados: {registrosEliminados}')


except Exception as e:
    print(f'Ocurrio un error {e}')
finally:
    conexion.close()

