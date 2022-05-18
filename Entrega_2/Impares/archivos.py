import pandas as pd


def modificar_pilotos(trabajadores_CSV):

    trabajadores_pilotos = trabajadores_CSV[(trabajadores_CSV["rol"] == "Piloto") | (trabajadores_CSV["rol"] == "Copiloto")]
    trabajadores_pilotos.to_csv('trabajadores_pilotos.csv', index = False)

def modificar_tripulacion(trabajadores_CSV):

    trabajadores_tripulacion = trabajadores_CSV[(trabajadores_CSV["rol"] != "Piloto") & (trabajadores_CSV["rol"] != "Copiloto")]
    trabajadores_tripulacion = trabajadores_tripulacion.drop(['licencia_actual_id'], axis=1)
    trabajadores_tripulacion.to_csv('trabajadores_tripulacion.csv', index = False)






vuelos = pd.read_csv('vuelos.csv')
trabajadores = pd.read_csv('trabajadores.csv')

# printea los primeros 5 datos de la data
# print(vuelos.head())
# print(trabajadores.head())

# printea las columnas especificas de la data
#print(vuelos[["vuelo_id", "nombre_compania"]])

# print(trabajadores_pilotos.head())
#print(trabajadores_pilotos)
# print(trabajadores["rol"] == "Piloto")

