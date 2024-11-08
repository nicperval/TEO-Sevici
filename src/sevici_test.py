import csv
from collections import namedtuple
from sevici import *
from mapas import *
from coordenadas import *
Coordenadas = namedtuple('Coordenadas', 'latitud, longitud')

Estacion = namedtuple('Estacion', 'nombre, bornetas, bornetas_vacias, bicis_disponibles, coordenadas')
def test_lee_estaciones(lista):
    lis = []
    for nombre,bornetas,bornetas_vacias,bicis_disponibles,Coordenadas in lista:
        Estacion = (nombre,bornetas,bornetas_vacias,bicis_disponibles,Coordenadas)
        lis.append(Estacion)
    print('Las tres primeras son:')
    for i in range(0,3):
        print(lis[i])
    print('Las tres últimas son:')
    for i in range(3,0,-1):
        print(lis[-i])
    
def test_estaciones_bicis_libres(lista):
    lib5 = estaciones_bicis_libres(lista,5)
    k = len(lib5)
    print(f'Hay {k} estaciones con 5 o más bicis libres y las 5 primeras son:')
    for i in range(0,5):
        print(lib5[i])
    lib10 = estaciones_bicis_libres(lista,10)
    k = len(lib10)
    print(f'Hay {k} estaciones con 10 o más bicis libres y las 5 primeras son:')
    for i in range(0,5):
        print(lib5[i])
    lib1 = estaciones_bicis_libres(lista,1)
    k = len(lib1)
    print(f'Hay {k} estaciones con 1 o más bicis libres y las 5 primeras son:')
    for i in range(0,5):
        print(lib5[i])

def test_estaciones_cercanas(lista,Coordenadas):
    cerca = estaciones_cercanas(lista,Coordenadas,5)
    print(f'Las 5 estaciones mas cercanas a {Coordenadas[0]}, {Coordenadas[1]} son:')
    for i in range(0,5):
        print(cerca[i])

def crea_mapa_estaciones(lista):
    '''Genera un objeto de tipo folium.Map con un marcador por cada
    estación dada como parámetro. El marcador tendrá como etiqueta
    el nombre de la estación, y su color se obtendrá a partir de la 
    función ```funcion_color``` que se pasa como parámetro
    ENTRADA
        :param estaciones: lista de estaciones disponibles
        :type estaciones: [Estacion(str, int, int, int, Coordenadas(float, float))]
        :param funcion_color: Función que se aplica a una estación y devuelve una cadena
            que representa el color en el que se dibuja el marcador
        :type funcion_color: function(Estacion)->str
    SALIDA
        :return: objeto mapa creado con los marcadores
        :rtype: folium.Map
    '''
    #Calculamos la media de las coordenadas de las estaciones, para poder centrar el 
    #mapa
    centro_mapa = media_coordenadas(lista)
    # creamos el mapa con folium
    mapa = crea_mapa(centro_mapa[0], centro_mapa[1], 13)

    for name,slots,empty_slots,free_bikes,Coordenadas in lista:
        etiqueta = name
        color = obten_color_bornetas_libres(empty_slots)
        marcador = crea_marcador (Coordenadas[0], Coordenadas[1], etiqueta,color)
        marcador.add_to(mapa)
    
    return mapa

if __name__ == '__main__':
    lista = lee_estaciones('data/estaciones.csv')
    mapa = crea_mapa_estaciones(lista)
    guarda_mapa(mapa,'img/bornetas_libres.html')