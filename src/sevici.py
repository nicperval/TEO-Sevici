import csv
from collections import namedtuple
from math import *
import folium

Coordenadas = namedtuple('Coordenadas', 'latitud, longitud')
Estacion = namedtuple('Estacion', 'nombre, bornetas, bornetas_vacias, bicis_disponibles, coordenadas')

def lee_estaciones(ruta):
    with open(ruta, encoding='utf-8') as f:
        next(f)
        fichero = csv.reader(f)
        lista = []
        for name,slots,empty_slots,free_bikes,latitude,longitude in fichero:
            slots = int(slots)
            empty_slots = int(empty_slots)
            free_bikes = int(free_bikes)
            latitude = float(latitude)
            longitude = float(longitude)
            Coordenadas = (latitude,longitude)
            Estacion = (name,slots,empty_slots,free_bikes,Coordenadas)
            lista.append(Estacion)
    return lista


if __name__ == '__main__':
    lista = lee_estaciones('data/estaciones.csv')
    