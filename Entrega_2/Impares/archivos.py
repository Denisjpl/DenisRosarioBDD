from datetime import datetime, date
import pandas as pd
import numpy as np
import csv 


def modificar_pilotos(base ):

    trabajadores_pilotos = base[(base["rol"] == "Piloto") | (base["rol"] == "Copiloto")]
    # trabajadores_pilotos['fecha_nacimiento'] = pd.to_datetime(trabajadores_pilotos['fecha_nacimiento'])
    trabajadores_pilotos.to_csv('CSV/trabajadores_pilotos.csv', index = False)
    trabajadores_pilotos = trabajadores_pilotos.drop_duplicates()

def modificar_tripulacion(base):

    trabajadores_tripulacion = base[(base["rol"] != "Piloto") & (base["rol"] != "Copiloto")]
    trabajadores_tripulacion = trabajadores_tripulacion.drop(['licencia_actual_id'], axis=1)
    trabajadores_tripulacion.to_csv('CSV/trabajadores_tripulacion.csv', index = False)
    trabajadores_tripulacion = trabajadores_tripulacion.drop_duplicates()

def modificar_csv_trabajadores(trabajadores_CSV, vuelos_CSV):
    # Primero abrimos el csv de trabajadores y lo convertimos en una lista de listas
    with open(trabajadores_CSV, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # Passing the cav_reader object to list() to get a list of lists
        lista_trabajadores = list(csv_reader)
    # Segundo, abrimos el CSV de vuelos y lo convertimos en una lista de lista
    with open('CSV/vuelos.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # Passing the cav_reader object to list() to get a list of lists
        lista_vuelos = list(csv_reader)

    # Luego le cambiamos el formato a todas las columnas que tengan fecha
    for i in range(len(lista_trabajadores)):
        if i == 0:
            continue
        else:
            lista_trabajadores[i][2] = datetime.strptime(lista_trabajadores[i][2], '%d-%m-%Y')
            lista_trabajadores[i][2] = datetime.strftime(lista_trabajadores[i][2],'%Y/%m/%d')
    
    # Posteriormente, ponemos NULL a todos los valores vacios
    for i in range(len(lista_trabajadores)):
        for j in range(len(lista_trabajadores[i])):
            print(lista_trabajadores[i][2])
            if lista_trabajadores[i][j] == '':
                lista_trabajadores[i][j] = 'NULL'
    
    # Despues areglamos y sacamos datos inconsistentes de la base de trabajadores
    lista_trabajadores_arreglado = []
    for i in range(len(lista_trabajadores)):
        for j in range(len(lista_vuelos)):
            if lista_trabajadores[i][7] == lista_vuelos[j][0] and lista_trabajadores[i][5] == lista_vuelos[j][6]:
                lista_trabajadores_arreglado.append(lista_trabajadores[i])

    # Por ultimo, escribimos el nuevo CSV
    with open('trabajadores_arreglado.csv', 'w', newline='') as student_file:
        writer = csv.writer(student_file)
        for i in range(len(lista_trabajadores_arreglado)):
            writer.writerow(lista_trabajadores_arreglado[i])

def modificar_csv_vuelos(archivo_CSV):
    # Primero abrimos el csv y lo convertimos en una lista de listas
    with open(archivo_CSV, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # Passing the cav_reader object to list() to get a list of lists
        lista_vuelos = list(csv_reader)

    # Luego le cambiamos el formato a todas las columnas que tengan fecha
    for i in range(len(lista_vuelos)):
        if i == 0:
            continue
        else:
            lista_vuelos[i][7] = datetime.strptime(lista_vuelos[i][7], '%Y-%m-%d %H:%M:%S')
            lista_vuelos[i][7] = datetime.strftime(lista_vuelos[i][7],'%Y/%m/%d %H:%M:%S')
            lista_vuelos[i][8] = datetime.strptime(lista_vuelos[i][8], '%Y-%m-%d %H:%M:%S')
            lista_vuelos[i][8] = datetime.strftime(lista_vuelos[i][8],'%Y/%m/%d %H:%M:%S')
    # Posteriormente, ponemos NULL a todos los valores vacios
    for i in range(len(lista_vuelos)):
        for j in range(len(lista_vuelos[i])):
            if lista_vuelos[i][j] == '':
                lista_vuelos[i][j] = 'NULL'

    # Por ultimo, escribimos el nuevo CSV
    with open('vuelos_arreglado.csv', 'w', newline='') as student_file:
        writer = csv.writer(student_file)
        for i in range(len(lista_vuelos)):
            writer.writerow(lista_vuelos[i])

def modificar_csv_reservas(archivo_CSV):
    # Primero abrimos el csv y lo convertimos en una lista de listas
    with open(archivo_CSV, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # Passing the cav_reader object to list() to get a list of lists
        lista_reservas = list(csv_reader)

    # Luego le cambiamos el formato a todas las columnas que tengan fecha
    for i in range(len(lista_reservas)):
        if i == 0:
            continue
        else:
            if lista_reservas[i][7] == '':
                continue
            else:
                lista_reservas[i][7] = datetime.strptime(lista_reservas[i][7], '%d-%m-%Y')
                lista_reservas[i][7] = datetime.strftime(lista_reservas[i][7],'%Y/%m/%d')
            if lista_reservas[i][14] == '':
                continue
            else:
                lista_reservas[i][14] = datetime.strptime(lista_reservas[i][14], '%d-%m-%Y')
                lista_reservas[i][14] = datetime.strftime(lista_reservas[i][14],'%Y/%m/%d')
    # Posteriormente, ponemos NULL a todos los valores vacios
    for i in range(len(lista_reservas)):
        for j in range(len(lista_reservas[i])):
            if lista_reservas[i][j] == '':
                lista_reservas[i][j] = 'NULL'

    # Por ultimo, escribimos el nuevo CSV
    with open('reserva_arreglado.csv', 'w', newline='') as student_file:
        writer = csv.writer(student_file)
        for i in range(len(lista_reservas)):
            writer.writerow(lista_reservas[i])

def crear_nuevos_csv_vuelos(archivo_CSV):
    # Se crea el nuevo csv que contiene solo a los aviones
    base_aviones = archivo_CSV
    base_aviones = base_aviones.drop(['vuelo_id'], axis=1)
    base_aviones = base_aviones.drop(['aerodromo_salida_id'], axis=1)
    base_aviones = base_aviones.drop(['aerodromo_llegada_id'], axis=1)
    base_aviones = base_aviones.drop(['ruta_id'], axis=1)
    base_aviones = base_aviones.drop(['codigo_vuelo'], axis=1)
    base_aviones = base_aviones.drop(['codigo_compania'], axis=1)
    base_aviones = base_aviones.drop(['fecha_salida'], axis=1)
    base_aviones = base_aviones.drop(['fecha_llegada'], axis=1)
    base_aviones = base_aviones.drop(['velocidad'], axis=1)
    base_aviones = base_aviones.drop(['altitud'], axis=1)
    base_aviones = base_aviones.drop(['estado'], axis=1)
    base_aviones = base_aviones.drop(['valor'], axis=1)
    base_aviones = base_aviones.drop(['nombre_compania'], axis=1)
    base_aviones = base_aviones.drop_duplicates()
    # Se crea el nuevo csv que contiene solo los datos del vuelo
    base_vuelos = archivo_CSV
    base_vuelos = base_vuelos.drop(['nombre_aeronave'], axis=1)
    base_vuelos = base_vuelos.drop(['modelo'], axis=1)
    base_vuelos = base_vuelos.drop(['nombre_compania'], axis=1)
    base_vuelos = base_vuelos.drop(['peso'], axis=1)
    base_vuelos = base_vuelos.drop_duplicates()
    # Se crea un nuevo csv que contiene solo los datos de la compania
    base_compania = archivo_CSV
    base_compania = base_compania.drop(['vuelo_id'], axis=1)
    base_compania = base_compania.drop(['aerodromo_salida_id'], axis=1)
    base_compania = base_compania.drop(['aerodromo_llegada_id'], axis=1)
    base_compania = base_compania.drop(['ruta_id'], axis=1)
    base_compania = base_compania.drop(['codigo_vuelo'], axis=1)
    base_compania = base_compania.drop(['codigo_aeronave'], axis=1)
    base_compania = base_compania.drop(['fecha_salida'], axis=1)
    base_compania = base_compania.drop(['fecha_llegada'], axis=1)
    base_compania = base_compania.drop(['velocidad'], axis=1)
    base_compania = base_compania.drop(['altitud'], axis=1)
    base_compania = base_compania.drop(['estado'], axis=1)
    base_compania = base_compania.drop(['nombre_aeronave'], axis=1)
    base_compania = base_compania.drop(['modelo'], axis=1)
    base_compania = base_compania.drop(['peso'], axis=1)
    base_compania = base_compania.drop(['valor'], axis=1)
    base_compania = base_compania.drop_duplicates()
    
    base_aviones.to_csv('CSV/aviones.csv', index = False)
    base_vuelos.to_csv('CSV/vuelos.csv', index = False)
    base_compania.to_csv('CSV/compania.csv', index = False)

def crear_nuevos_csv_trabajadores(base_trabajadores):
    
    base_trabajadores = base_trabajadores.drop(['nombre_compania'], axis=1)
    return base_trabajadores

def crear_nuevos_csv_reservas(archivo_CSV):

    # Se crea el nuevo csv de reservas
    base_reservas = archivo_CSV
    base_reservas = base_reservas.drop(['nombre_comprador'], axis=1)
    base_reservas = base_reservas.drop(['nacionalidad_comprador'], axis=1)
    base_reservas = base_reservas.drop(['fecha_nacimiento_comprador'], axis=1)
    base_reservas = base_reservas.drop(['nombre_pasajero'], axis=1)
    base_reservas = base_reservas.drop(['nacionalidad_pasajero'], axis=1)
    base_reservas = base_reservas.drop(['fecha_nacimiento_pasajero'], axis=1)
    base_reservas = base_reservas.drop_duplicates()
    # Se crea el nuevo csv de comprador
    base_comprador = archivo_CSV
    base_comprador = base_comprador.drop(['reserva_id'], axis=1)
    base_comprador = base_comprador.drop(['codigo_reserva'], axis=1)
    base_comprador = base_comprador.drop(['numero_ticket'], axis=1)
    base_comprador = base_comprador.drop(['vuelo_id'], axis=1)
    base_comprador = base_comprador.drop(['numero_asiento'], axis=1)
    base_comprador = base_comprador.drop(['clase'], axis=1)
    base_comprador = base_comprador.drop(['comida_y_maleta'], axis=1)
    base_comprador = base_comprador.drop(['pasaporte_pasajero'], axis=1)
    base_comprador = base_comprador.drop(['nombre_pasajero'], axis=1)
    base_comprador = base_comprador.drop(['nacionalidad_pasajero'], axis=1)
    base_comprador = base_comprador.drop(['fecha_nacimiento_pasajero'], axis=1)
    base_comprador = base_comprador.drop_duplicates()
    # Se crea el nuevo csv del pasajero
    base_pasajero = archivo_CSV
    base_pasajero = base_pasajero.drop(['reserva_id'], axis=1)
    base_pasajero = base_pasajero.drop(['codigo_reserva'], axis=1)
    base_pasajero = base_pasajero.drop(['numero_ticket'], axis=1)
    base_pasajero = base_pasajero.drop(['vuelo_id'], axis=1)
    base_pasajero = base_pasajero.drop(['pasaporte_comprador'], axis=1)
    base_pasajero = base_pasajero.drop(['nombre_comprador'], axis=1)
    base_pasajero = base_pasajero.drop(['nacionalidad_comprador'], axis=1)
    base_pasajero = base_pasajero.drop(['fecha_nacimiento_comprador'], axis=1)
    base_pasajero = base_pasajero.drop(['numero_asiento'], axis=1)
    base_pasajero = base_pasajero.drop(['clase'], axis=1)
    base_pasajero = base_pasajero.drop(['comida_y_maleta'], axis=1)
    base_pasajero = base_pasajero.drop_duplicates()


    base_reservas.to_csv('CSV/reservas.csv', index = False)
    base_comprador.to_csv('CSV/cliente_comprador.csv', index = False)
    base_pasajero.to_csv('CSV/cliente_pasajero.csv', index = False)


if __name__ == "__main__":
    # Creamos todos los archivos que provienen de vuelos
    modificar_csv_vuelos("vuelos.csv")
    vuelos_arreglado = pd.read_csv("vuelos_arreglado.csv")
    crear_nuevos_csv_vuelos(vuelos_arreglado)
    # Creamos todos los csv que provienen de trabajadores
    modificar_csv_trabajadores('trabajadores.csv', 'CSV/vuelos.csv')
    trabajadores_arreglado = pd.read_csv('trabajadores_arreglado.csv')
    base_trabajadores = crear_nuevos_csv_trabajadores(trabajadores_arreglado)
    modificar_pilotos(base_trabajadores)
    modificar_tripulacion(base_trabajadores)
    # Creamos todos los archivos que provienen de reservas
    modificar_csv_reservas('reservasV2.csv')
    reservas_arreglado = pd.read_csv('reserva_arreglado.csv')
    crear_nuevos_csv_reservas(reservas_arreglado)


