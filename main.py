import json
#test sera la descripcion a buscar



# with open('bd/test.json') as file:
#     test = json.load(file)

# #data sera donde se buscara

# with open('bd/data.json') as file:
#     data = json.load(file)



# VARIABLES MOMENTARIAS SOLO PARA PRUEBAS ----------------
puntos = 0

# -----------------------------------


# VARIABLES --------------------------

# PREPARANDO LOS DATOS
def buscarPersona(persona, comparar) :
    max1 = 0
    max2 = 0
    max3 = 0
    max4 = 0
    max5 = 0
    pos1 = ''
    pos2 = ''
    pos3 = ''
    pos4 = ''
    pos5 = ''
    json_ax = comparar
    for buscar in json_ax:
        puntos=0
        #CONTEXTURA
        contextura = ["Obesa","Robusta", "Mediana", "Delgada", "No recuerda"]
        #CARA
        cara_color = ["Albino", "Blanco", "Trigueño", "Amarillo", "Negro", "Moreno", "No recuerda"]
        #CABELLO
        cabello_color = ["Albino", "Cano", "Entrecano", "Rubio", "Castaño claro", "Castaño oscuro", "Rojizo", "Negro", "Tinturado", "No recuerda"]
        cabello_longitud = ["Rapado", "Corto", "Mediano", "Largo", "No recuerda"]
        cabello_forma = ["Liso", "Ondulado", "Lanoso", "Crespo", "No recuerda"]

        #PUNTAJE
        #contextura
        i = 0
        pos_per = 0
        pos_bus = 0
        for res in contextura:
            if persona["contextura"] == res:
                pos_per = i
            if buscar["contextura"] == res:
                pos_bus = i 
            i = i+1

        x = abs(pos_bus - pos_per)
        x = 15/(x+1)
        puntos = puntos + x

        #cara
        i = 0
        pos_per = 0
        pos_bus = 0
        for res in cara_color:
            if persona["cara"]["color"] == res:
                pos_per = i
            if buscar["cara"]["color"] == res:
                pos_bus = i 
            i = i+1

        x = abs(pos_bus - pos_per)
        x = 5/(x+1)
        puntos = puntos + x

        if persona["cara"]["contorno"] == buscar["cara"]["contorno"]:
            puntos = puntos + 5

        if persona["cara"]["particularidad"] == buscar["cara"]["particularidad"]:
            puntos = puntos + 5

        #cabello
        i = 0
        pos_per = 0
        pos_bus = 0
        for res in cabello_color:
            if persona["cabello"]["color"] == res:
                pos_per = i
            if buscar["cabello"]["color"] == res:
                pos_bus = i 
            i = i+1

        x = abs(pos_bus - pos_per)
        x = 3/(x+1)
        puntos = puntos + x
        # ----------------------------------------
        i = 0
        pos_per = 0
        pos_bus = 0
        for res in cabello_longitud:
            if persona["cabello"]["longitud"] == res:
                pos_per = i
            if buscar["cabello"]["longitud"] == res:
                pos_bus = i 
            i = i+1

        x = abs(pos_bus - pos_per)
        x = 3/(x+1)
        puntos = puntos + x
        # ----------------------------------------
        i = 0
        pos_per = 0
        pos_bus = 0
        for res in cabello_forma:
            if persona["cabello"]["forma"] == res:
                pos_per = i
            if buscar["cabello"]["forma"] == res:
                pos_bus = i 
            i = i+1

        x = abs(pos_bus - pos_per)
        x = 3/(x+1)
        puntos = puntos + x

        if persona["cabello"]["calvicie"] == buscar["cabello"]["calvicie"]:
            puntos = puntos + 3

        if persona["cabello"]["particularidad"] == buscar["cabello"]["particularidad"]:
            puntos = puntos + 3

        #ojos

        if persona["ojos"]["color"] == buscar["ojos"]["color"]:
            puntos = puntos + 3

        if persona["ojos"]["tamano"] == buscar["ojos"]["tamano"]:
            puntos = puntos + 3

        if persona["ojos"]["particularidad"] == buscar["ojos"]["particularidad"]:
            puntos = puntos + 4

        #nariz
        if persona["nariz"] == buscar["nariz"]:
            puntos = puntos + 5

        #boca
        if persona["boca"] == buscar["boca"]:
            puntos = puntos + 5

        #labios
        if persona["labios"] == buscar["labios"]:
            puntos = puntos + 5


        #barba
        if persona["barba"]["existe"] == buscar["barba"]["existe"]:
            if persona["barba"]["existe"] == "no":
                puntos = puntos + 10
            else:
                puntos = puntos + 2

        if persona["barba"]["capilaridad"] == buscar["barba"]["capilaridad"]:
            puntos = puntos + 2

        if persona["barba"]["estilo"] == buscar["barba"]["estilo"]:
            puntos = puntos + 2

        if persona["barba"]["longitud"] == buscar["barba"]["longitud"]:
            puntos = puntos + 2

        if persona["barba"]["particularidad"] == buscar["barba"]["particularidad"]:
            puntos = puntos + 2

        #bigote
        if persona["bigote"]["existe"] == buscar["bigote"]["existe"]:
            if persona["barba"]["existe"] == "no":
                puntos = puntos + 5
            else:
                puntos = puntos + 2

        if persona["bigote"]["capilaridad"] == buscar["bigote"]["capilaridad"]:
            puntos = puntos + 1

        if persona["bigote"]["particularidad"] == buscar["bigote"]["particularidad"]:
            puntos = puntos + 1

        if persona["bigote"]["longitud"] == buscar["bigote"]["longitud"]:
            puntos = puntos + 1


        #orejas
        if persona["orejas"] == buscar["orejas"]:
            puntos = puntos + 5


        #CALCULO FINAL
        final = (puntos*100)/90
        
        print(final, "% DE COINCIDENCIA")

        if(final>max1): 
            pos5 = pos4
            pos4 = pos3
            pos3 = pos2
            pos2 = pos1
            pos1 = buscar["_id"]
            max5 = max4
            max4 = max3
            max3 = max2
            max2 = max1
            max1=final
        else:
            if(final>max2):
                pos5 = pos4
                pos4 = pos3
                pos3 = pos2
                pos2=buscar["_id"]
                max5 = max4
                max4 = max3
                max3 = max2
                max2=final
            else:
                if(final>max3):
                    pos5 = pos4
                    pos4 = pos3
                    pos3=buscar["_id"]
                    max5 = max4
                    max4 = max3
                    max3=final
                else:
                    if(final>max4):
                        pos5 = pos4
                        pos4=buscar["_id"]
                        max5 = max4
                        max4=final
                    else:
                        if(final>max5):
                            pos5=buscar["_id"]
                            max5=final


    resultadosFinales = []
    resultadosFinales.append(pos1)
    resultadosFinales.append(pos2)
    resultadosFinales.append(pos3)
    resultadosFinales.append(pos4)
    resultadosFinales.append(pos5)
    return resultadosFinales
                            