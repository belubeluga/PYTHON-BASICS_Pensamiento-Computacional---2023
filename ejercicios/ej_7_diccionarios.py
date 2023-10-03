#%% 13
subtes = ['A','C','D','E']
estaciones = {'A':['Acoyte','Avenida de Mayo','Callao'],
              'C': ['Pellegrini','Congreso','Urquiza'],
              'D':['Pellegrini','Urquiza','Callao'],
              'E':['Pellegrini','Lima','Avenida de Mayo']}

def lineas_por_estacion(estacion:str)->list:
    lineas_que_pasan = []
    for linea in subtes:
        if estacion in estaciones[linea]:
            lineas_que_pasan.append(linea)
    return lineas_que_pasan


def recorrido(origen:str,destino:str)->list:
    lineas_o = lineas_por_estacion(origen)
    lineas_d = lineas_por_estacion(destino)
    for linea_o in lineas_o:
        if linea_o in lineas_d:
            return [linea_o]
    
    for linea_o in lineas_o:
        for estacion in estaciones[linea_o]:
            lineas_estacion = lineas_por_estacion(estacion)
            for linea_o2 in lineas_estacion:
                if linea_o2 in lineas_estacion:
                    return [linea_o,linea_o2]