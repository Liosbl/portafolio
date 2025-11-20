#############################################################
#
# Juego de 21 cartas.....Adivina la carta elejida en 3 intentos.
#
# En vez de cartas se hace com letras.
#
# En tres intentos indicando solo en que columna se encuentra la
# letra seleccionada adivina la carta elejida.
#

import random

MAX_TARJETAS_GRUPO = 7
MAX_GRUPOS = 3
MAX_TARJETAS = MAX_TARJETAS_GRUPO * MAX_GRUPOS
MIN_TARJETA_VALOR = 65
MAX_TARJETA_VALOR = MAX_TARJETAS + MIN_TARJETA_VALOR - 1

# Cargo letras aleatoriamente
i = 0
deck = ""
for i in range(0, MAX_TARJETAS):
    bExiste = True 
    while bExiste:
        j = 0
        bExiste = False
        # Obtengo una letra del mapa de caracteres ASCII desde la A(65) a la Z(90)
        posibleLetra = chr(random.randint( 65, 90))
        # Verifico que la letra obtenida no exista.
        while j < i :
            if i != 0:
                if posibleLetra == deck[j] :
                    bExiste = True
                    break
                else :
                    j += 1
    # Asigno a la cadena la letra obtenida solo si no esta repetida.
    deck = deck + posibleLetra

k = int(0)
# Cantidad de intentos a obtener la letra elejida.
while k < 4:
    # Verifico si es el último intento (parte de 0).
    if k == 3:
        print(f"La letra Seleccionada es la {deck[10]}")
        break
    # Separo en 3 columnas las 21 letras obtenidas e imprimo en pantalla.
    # Distribuyendo cada letra en una columna de las 3 es decir:
    #               01er letra 1er columna 02da letra 2 coluna 03er letra 3er columna 
    #               04ta letra 1er columna 05ta letra 2 coluna 06er letra 3er columna
    #               ....
    #               19na letra 1er columna 20ma letra 2 coluna 21ra letra 3er columna)
    i = 0
    grupo1 = ""
    grupo2 = ""
    grupo3 = ""
    while i < MAX_TARJETAS:
        grupo1 = grupo1 + deck[i];
        grupo2 = grupo2 + deck[i+1];
        grupo3 = grupo3 + deck[i+2];
        print(f" {deck[i]} \t {deck[i + 1]} \t {deck[i + 2]}" )
        i += 3
    # Selecciono la columna donde esta la letra elejida.
    print(f" Seleccion  {k} \n")
    nColSel = int(input("Ingrese el nro. de columna donde esta la letra elegida:"))
    deck = ""
    # Dependiendo de donde esta la letra elejida es que agrupo las letras
    # Siempre teniendo en cuenta que la columna donde esta la letra elejida
    # debe ir al medio.
    match nColSel:
        case 1:
            for j in range(0,MAX_TARJETAS_GRUPO):
                deck = deck + grupo2[j]
            for j in range(0, MAX_TARJETAS_GRUPO):
                deck = deck + grupo1[j];
            for j in range(0, MAX_TARJETAS_GRUPO):
                deck = deck + grupo3[j];
        case 2:
            for j in range(0,MAX_TARJETAS_GRUPO):
                deck = deck + grupo1[j];
            for j in range(0,MAX_TARJETAS_GRUPO):
                deck = deck + grupo2[j];
            for j in range(0,MAX_TARJETAS_GRUPO):
                deck = deck + grupo3[j];
        case _:
            for j in range(0,MAX_TARJETAS_GRUPO):
                deck = deck + grupo1[j];
            for j in range(0,MAX_TARJETAS_GRUPO):
                deck = deck + grupo3[j];
            for j in range(0,MAX_TARJETAS_GRUPO):
                deck = deck + grupo2[j];
    k += 1


#    //for (i = 0; i < MAX_TARJETAS; i += 3)
#    //{
#    //    cout << deck[i] << "\t" << deck[i + 1] << "\t" << deck[i + 2] << "\n";
#    //}

#    exit(0);

