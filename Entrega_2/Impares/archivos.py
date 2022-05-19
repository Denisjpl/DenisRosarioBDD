from datetime import datetime, date
import pandas as pd
import csv 


def modificar_pilotos(archivo_CSV):

    trabajadores_pilotos = archivo_CSV[(archivo_CSV["rol"] == "Piloto") | (archivo_CSV["rol"] == "Copiloto")]
    trabajadores_pilotos['fecha_nacimiento'] = pd.to_datetime(trabajadores_pilotos['fecha_nacimiento'])
    trabajadores_pilotos.to_csv('trabajadores_pilotos.csv', index = False)

def modificar_tripulacion(archivo_CSV):

    trabajadores_tripulacion = archivo_CSV[(archivo_CSV["rol"] != "Piloto") & (archivo_CSV["rol"] != "Copiloto")]
    trabajadores_tripulacion = trabajadores_tripulacion.drop(['licencia_actual_id'], axis=1)
    trabajadores_tripulacion.to_csv('trabajadores_tripulacion.csv', index = False)

def modificar_csv_tripulacion():
    # Primero abrimos el csv y lo convertimos en una lista de listas
    with open('trabajadores.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # Passing the cav_reader object to list() to get a list of lists
        lista_trabajadores = list(csv_reader)

    # Luego le cambiamos el formato a todas las columnas que tengan fecha
    for i in range(len(lista_trabajadores)):
        if i == 0:
            continue
        else:
            lista_trabajadores[i][2] = datetime.strptime(lista_trabajadores[i][2], '%d-%m-%Y')
            lista_trabajadores[i][2] = datetime.strftime(lista_trabajadores[i][2],'%d/%m/%Y')
    
    # Posteriormente, ponemos NULL a todos los valores vacios
    for i in range(len(lista_trabajadores)):
        for j in range(len(lista_trabajadores[i])):
            if lista_trabajadores[i][j] == '':
                lista_trabajadores[i][j] = 'NULL'
    # Por ultimo, escribimos el nuevo CSV
    with open('trabajadores_nuevo.csv', 'w', newline='') as student_file:
        writer = csv.writer(student_file)
        for i in range(len(lista_trabajadores)):
            writer.writerow(lista_trabajadores[i])

def modificar_csv_vuelos():
    # Primero abrimos el csv y lo convertimos en una lista de listas
    with open('vuelos.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # Passing the cav_reader object to list() to get a list of lists
        lista_vuelos = list(csv_reader)

    # Luego le cambiamos el formato a todas las columnas que tengan fecha
    for i in range(len(lista_vuelos)):
        if i == 0:
            continue
        else:
            lista_vuelos[i][7] = datetime.strptime(lista_vuelos[i][7], '%Y-%m-%d %H:%M:%S')
            lista_vuelos[i][7] = datetime.strftime(lista_vuelos[i][7],'%d/%m/%Y %H:%M:%S')
            lista_vuelos[i][8] = datetime.strptime(lista_vuelos[i][8], '%Y-%m-%d %H:%M:%S')
            lista_vuelos[i][8] = datetime.strftime(lista_vuelos[i][8],'%d/%m/%Y %H:%M:%S')
    # Posteriormente, ponemos NULL a todos los valores vacios
    for i in range(len(lista_vuelos)):
        for j in range(len(lista_vuelos[i])):
            if lista_vuelos[i][j] == '':
                lista_vuelos[i][j] = 'NULL'

    # Por ultimo, escribimos el nuevo CSV
    with open('vuelos_nuevo.csv', 'w', newline='') as student_file:
        writer = csv.writer(student_file)
        for i in range(len(lista_vuelos)):
            writer.writerow(lista_vuelos[i])

def modificar_csv_reservas():
    # Primero abrimos el csv y lo convertimos en una lista de listas
    with open('reservasV2.csv', 'r') as csv_file:
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
                lista_reservas[i][7] = datetime.strftime(lista_reservas[i][7],'%d/%m/%Y')
            if lista_reservas[i][14] == '':
                continue
            else:
                lista_reservas[i][14] = datetime.strptime(lista_reservas[i][14], '%d-%m-%Y')
                lista_reservas[i][14] = datetime.strftime(lista_reservas[i][14],'%d/%m/%Y')
    # Posteriormente, ponemos NULL a todos los valores vacios
    for i in range(len(lista_reservas)):
        for j in range(len(lista_reservas[i])):
            if lista_reservas[i][j] == '':
                lista_reservas[i][j] = 'NULL'
    
    print(lista_reservas[1])

    # Por ultimo, escribimos el nuevo CSV
    with open('reserva_nuevo.csv', 'w', newline='') as student_file:
        writer = csv.writer(student_file)
        for i in range(len(lista_reservas)):
            writer.writerow(lista_reservas[i])


if __name__ == "__main__":

    #modificar_csv_tripulacion()
    #modificar_csv_vuelos()
    # modificar_csv_reservas()

    # vuelos = pd.read_csv('vuelos.csv')
    # trabajadores = pd.read_csv('trabajadores.csv')



    # print(trabajadores.dtypes)

    # modificar_pilotos(trabajadores)

    # printea los primeros 5 datos de la data
    # print(vuelos.head())
    # print(trabajadores.head())

    # printea las columnas especificas de la data
    #print(vuelos[["vuelo_id", "nombre_compania"]])


    # print(trabajadores_pilotos.head())
    # print(trabajadores_pilotos)
    # print(trabajadores["rol"] == "Piloto")
