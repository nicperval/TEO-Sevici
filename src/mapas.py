import csv
from collections import namedtuple
from math import *
import folium
def crea_mapa(latitud, longitud, zoom):
    '''
    Función que crea un mapa folium que está centrado en la latitud y longitud
    dados como parámetro y mostrado con el nivel de zoom dado.
    ENTRADA:
        :param latitud: latitud del centro del mapa en pantalla
        :type latitud:float
        :param longitud: longitud del centro del mapa  en pantalla
        :type longitud: float
        :param zoom: nivel del zoom con el que se muestra el mapa
        :type zoom: int
    SALIDA:
        :return: objeto mapa creado
        :rtype: folium.Map
    '''
    mapa = folium.Map(location=[latitud, longitud], 
                      zoom_start=zoom)
    return mapa   

def crea_marcador (latitud, longitud, etiqueta, color):
    '''
    Función que crea un marcador rojo con un icono de tipo señal de información.
    El marcador se mostrará en el punto del mapa dado por la latitud y longitud
    y cuandos se mueva el ratón sobre él, se mostrará una etiqueta con el texto
    dado por el parámetro etiqueta
    ENTRADA:
        :param latitud: latitud del marcador
        :type latitud: float
        :param longitud: longitud del marcador
        :type longitud: float
        :param etiqueta: texto de la etiqueta que se asociará al marcador 
        :type etiqueta: str
    SALIDA:
        :return: objeto marcador creado
        :rtype:folium.Marker
    '''
    marcador = folium.Marker([latitud,longitud], 
                   popup=etiqueta, 
                   icon=folium.Icon(color=color, icon='info-sign')) 
    return marcador

def guarda_mapa(mapa, ruta_fichero):
    '''Guard un mapa como archivo html

    :param mapa: Mapa a guardar
    :type mapa: folium.Map
    :param ruta_fichero: Nombre y ruta del fichero
    :type ruta_fichero: str
    '''
    mapa.save(ruta_fichero)

def obten_color_bicis_disponibles(free_bikes):
    if free_bikes == 0:
        color = 'red'
    else:
        color = 'green'
    return color

def obten_color_bornetas_libres(empty_slots):
    if empty_slots == 0:
        color = 'red'
    else:
        color = 'green'
    return color