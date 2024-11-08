import csv
from collections import namedtuple
from math import *
import folium
Coordenadas = namedtuple('Coordenadas', 'latitude, longitude')
Estacion = namedtuple('Estacion', 'nombre, bornetas, bornetas_vacias, bicis_disponibles, coordenadas')
def estaciones_bicis_libres(lista,k):
    estaciones = []
    if k == None:
        k = 5
    for name,slots,empty_slots,free_bikes,Coordenadas in lista:
        if free_bikes >= k :
            tupla = (name,free_bikes)
            estaciones.append(tupla)
    res = sorted(estaciones, key=lambda filtro:filtro[1])
    res.reverse()
    return res

def calcula_distancia(coord1,coord2):
    distancia = sqrt((coord2[0]-coord1[0])**2 + (coord2[1]-coord2[1])**2)
    return distancia
    
def estaciones_cercanas(lista,coord,k):
    lis = []
    for name,slots,empty_slots,free_bikes,Coordenadas in lista:
        dist = calcula_distancia(coord,Coordenadas)
        tupla = (name,slots,empty_slots,free_bikes,dist)
        lis.append(tupla)
    orden = sorted(lis,key=lambda filtro:filtro[4])
    res = []
    for name,slots,empty_slots,free_bikes,dist in orden:
            if len(res) == k:
                break
            tupla = (dist,name,free_bikes)
            res.append(tupla)
    return res

def media_coordenadas(lista):
    lat = []
    lon = []
    for name,slots,empty_slots,free_bikes,Coordenadas in lista:
        lat.append(Coordenadas[0])
        lon.append(Coordenadas[1])
    mlat = sum(lat)/len(lat)
    mlon = sum(lon)/len(lat)
    Coordenadas = (mlat,mlon)
    return Coordenadas