import random

cantidad_cartas = 3

def repartirCarta():
    palo = ["Oro", "Basto", "Espada", "Copa"]
    numero = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    p = random.randint(0, 3)
    n = random.randint(0, 9)
    carta = [palo[p], numero[n]]
    return carta

def recuperarMayorValor(cartas: list):
    carta_mayor = 0
    for carta in range(0, cantidad_cartas):
        carta_actual = cartas[carta][1]
        if carta_actual >= 10:
            carta_actual = 0

        if carta_actual > carta_mayor:
            carta_mayor = carta_actual

    return carta_mayor

def tieneFlor(cartas: list):
    if cartas[0][0] == cartas[1][0] == cartas[2][0]:
        return True

def sumarFlor(cartas: list):
    valor_flor = 20
    for carta in range(0, cantidad_cartas):
        if cartas[carta][1] >= 10:
            valor_flor = valor_flor + 0
        else:
            valor_flor = valor_flor + cartas[carta][1]

    return valor_flor

def tieneEnvido(cartas: list):
    for carta in range(0, cantidad_cartas):
        if carta == 0:
            if cartas[carta][0] == cartas[1][0]:
                return True
            elif cartas[carta][0] == cartas[2][0]:
                return True
        elif carta == 1:
            if cartas[carta][0] == cartas[0][0]:
                return True
            elif cartas[carta][0] == cartas[2][0]:
                return True

def contarEnvido(cartas: list):
    for carta in range(0, cantidad_cartas):
        if carta == 0:
            if cartas[carta][0] == cartas[1][0]:
                return sumarEnvido(cartas[carta][1], cartas[1][1])
            elif cartas[carta][0] == cartas[2][0]:
                return sumarEnvido(cartas[carta][1], cartas[2][1])
        elif carta == 1:
            if cartas[carta][0] == cartas[0][0]:
                return sumarEnvido(cartas[carta][1], cartas[0][1])
            elif cartas[carta][0] == cartas[2][0]:
                return sumarEnvido(cartas[carta][1], cartas[2][1])

def sumarEnvido(carta_1: int, carta_2: int):
    if carta_1 >= 10:
        carta_1 = 0
    if carta_2 >= 10:
        carta_2 = 0
    return carta_1 + carta_2 + 20

def recuperarGanadorTanto(tanto_ia: int, tanto_usuario: int, es_mano: bool):
    if es_mano:
        if tanto_usuario >= tanto_ia:
            return True
        else:
            return False
    else:
        if tanto_ia >= tanto_usuario:
            return False
        else:
            return True

def jerarquizar_cartas(cartas: list):
    valores_cartas = []
    for carta in range(0, cantidad_cartas):
        num = cartas[carta][1]
        palo = cartas[carta][0]
        if num == 1:
            if palo == 'Oro' or palo == 'Copa':
                valores_cartas.append(8)
            elif palo == 'Basto':
                valores_cartas.append(13)
            else:
                valores_cartas.append(14)
        elif num == 2:
            valores_cartas.append(9)
        elif num == 3:
            valores_cartas.append(10)
        elif num == 4:
            valores_cartas.append(1)
        elif num == 5:
            valores_cartas.append(2)
        elif num == 6:
            valores_cartas.append(3)
        elif num == 7:
            if palo == 'Basto' or palo == 'Copa':
                valores_cartas.append(4)
            elif palo == 'Oro':
                valores_cartas.append(11)
            else:
                valores_cartas.append(12)
        elif num == 10:
            valores_cartas.append(5)
        elif num == 11:
            valores_cartas.append(6)
        elif num == 12:
            valores_cartas.append(7)

    return valores_cartas

def recuperar_pregunta(largo_lista: int):
    if largo_lista <= 1:
        return 'Seleccione la carta restante: '
    elif largo_lista == 2:
        return 'Seleccione la carta 1 o 2: '
    else:
        return 'Seleccione la carta 1, 2 o 3: '

def recuperar_canto(valor_mano: int):
    if valor_mano == 1:
        return 'truco'
    elif valor_mano == 2:
        return 'retruco'
    else:
        return 'vale cuatro'

def recuperar_respuesta_ia(valor_cartas_ia: int, valor_mano: int):
    if valor_mano == 1:
        if valor_cartas_ia > 5:
            return True
    elif valor_mano == 2:
        if valor_cartas_ia > 7:
            return True
    elif valor_mano == 3:
        if valor_cartas_ia > 8:
            return True
    elif valor_mano == 4:
        if valor_cartas_ia > 9:
            return True

def recuperar_promedio_cartas(cartas_ia: list):
    valor_cartas_ia = 0
    for carta in cartas_ia:
        valor_cartas_ia = valor_cartas_ia + carta[1]

    return valor_cartas_ia // len(cartas_ia)


puntos_usuario = 0
puntos_ia = 0
hasta_cuantos_puntos = int(input('Hasta cuantos puntos quiere jugar? 15/30   '))

es_mano = False
juega_jugador = False
puede_cantar = True

while puntos_usuario < hasta_cuantos_puntos and puntos_ia < hasta_cuantos_puntos:
    print(f'La partida va {puntos_usuario} a {puntos_ia}')
    cartas_usuario = []
    cartas_ia = []

    for carta in range(0, cantidad_cartas):
        cartas_usuario.append(repartirCarta())
        cartas_ia.append(repartirCarta())

    print('Estas son sus cartas: ')
    for carta in cartas_usuario:
        print(f'{carta[1]} de {carta[0]}')

    valor_tanto = recuperarMayorValor(cartas_usuario)
    tiene_flor = False

    if tieneFlor(cartas_usuario):
        tiene_flor = True
        valor_tanto = sumarFlor(cartas_usuario)
    elif tieneEnvido(cartas_usuario):
        valor_tanto = contarEnvido(cartas_usuario)

    print()
    print(f"Usted tiene {valor_tanto} de tanto")

    if tiene_flor:
        canta_flor = input("Tiene flor, desea cantar flor? SI/NO  ").upper()
        print()
        if canta_flor == 'SI':
            if tieneFlor(cartas_ia):
                tanto_ia = sumarFlor(cartas_ia)
                gano_usuario = recuperarGanadorTanto(tanto_ia, valor_tanto, es_mano)
                if gano_usuario:
                    puntos_usuario = puntos_usuario + 3
                    print('Ganaste el tanto')
                else:
                    puntos_ia = puntos_ia + 3
                    print(f'La IA tiene {str(tanto_ia)} de tanto')
                    print('Perdiste el tanto')
            else:
                print()
                print('La IA no tiene flor')
                puntos_usuario = puntos_usuario + 3
        elif tieneFlor(cartas_ia):
            puntos_ia = puntos_ia + 3
            print('La IA tiene flor')
    else:
        canta_envido = input('Desea cantar envido? SI/NO  ').upper()
        print()
        if canta_envido == 'SI':
            tanto_ia = recuperarMayorValor(cartas_ia)
            if tieneFlor(cartas_ia):
                puntos_ia = puntos_ia + 3
                print('La IA tiene flor')
            else:
                if tieneEnvido(cartas_ia):
                    tanto_ia = contarEnvido(cartas_ia)

                if recuperarGanadorTanto(tanto_ia, valor_tanto, es_mano):
                    puntos_usuario = puntos_usuario + 2
                    print('Ganaste el tanto')
                else:
                    puntos_usuario = puntos_usuario + 2
                    print(f'La IA tiene {str(tanto_ia)} de tanto')
                    print('Perdiste el tanto')
        elif tieneFlor(cartas_ia):
            puntos_ia = puntos_ia + 3
            print('La IA tiene flor')
        elif tieneEnvido(cartas_ia):
            tanto_ia = contarEnvido(cartas_ia)
            if tanto_ia > 28:
                print('La IA canta envido')
                acepto_envido = input('Acepta? SI/NO   ').upper()

                if acepto_envido == 'SI':
                    if tieneEnvido(cartas_usuario):
                        valor_tanto = contarEnvido(cartas_usuario)

                    if recuperarGanadorTanto(tanto_ia, valor_tanto, es_mano):
                        puntos_usuario = puntos_usuario + 2
                        print('Ganaste el tanto')
                    else:
                        puntos_usuario = puntos_usuario + 2
                        print(f'La IA tiene {str(tanto_ia)} de tanto')
                        print('Perdiste el tanto')

    valores_cartas_usuario = jerarquizar_cartas(cartas_usuario)
    valores_cartas_ia = jerarquizar_cartas(cartas_ia)

    print()
    mano_puntos_usuario = 0
    mano_puntos_ia = 0
    valor_mano = 1

    while mano_puntos_usuario < 2 and mano_puntos_ia < 2:
        promedio_cartas_ia = recuperar_promedio_cartas(cartas_ia)
        if juega_jugador:
            que_canta = recuperar_canto(valor_mano)
            if valor_mano < 4:
                if puede_cantar:
                    canta = input(f'Quiere cantar {que_canta}? SI/NO  ').upper()
                    if canta == 'SI':
                        respuesta_ia = recuperar_respuesta_ia(promedio_cartas_ia, valor_mano)
                        if respuesta_ia == 1:
                            print('La IA aceptó')
                            valor_mano = valor_mano + 1
                        else:
                            print('La IA rechazó')
                            mano_puntos_usuario = 2
                            continue
            print('Seleccione la posicion de una de sus cartas: ')
            for carta in cartas_usuario:
                print(f'{carta[1]} de {carta[0]}')

            pregunta = recuperar_pregunta(len(cartas_usuario))
            posicion_carta_elegida = int(input('Seleccione 0 para irse al mazo o ' + pregunta))
            print()
            if posicion_carta_elegida == 0:
                mano_puntos_ia = 2
                continue

            carta_elegida = cartas_usuario[posicion_carta_elegida - 1]
            valor_carta_elegida = valores_cartas_usuario[posicion_carta_elegida - 1]

            print(f'El jugador tiro la carta {cartas_usuario[posicion_carta_elegida - 1][1]} de {cartas_usuario[posicion_carta_elegida - 1][0]}')
            cartas_usuario.pop(posicion_carta_elegida - 1)
            print()

            posicion_carta_ia = random.randint(0, len(cartas_ia) - 1)
            carta_elegida_ia = cartas_ia[posicion_carta_ia]
            valor_carta_ia = valores_cartas_ia[posicion_carta_ia]

            print(f'La IA tiró la carta {cartas_ia[posicion_carta_ia][1]} de {cartas_ia[posicion_carta_ia][0]}')
            cartas_ia.pop(posicion_carta_ia)
            print()
        else:
            que_canta = recuperar_canto(valor_mano)
            canta = recuperar_respuesta_ia(promedio_cartas_ia, valor_mano)
            if canta:
                print(f'La IA canta {que_canta}')
                usuario_acepta = input(f'Acepta el {que_canta}? SI/NO   ')
                if usuario_acepta:
                    valor_mano = valor_mano + 1

            posicion_carta_ia = random.randint(0, len(cartas_ia) - 1)
            carta_elegida_ia = cartas_ia[posicion_carta_ia]
            valor_carta_ia = valores_cartas_ia[posicion_carta_ia]

            print(f'La IA tiró la carta {cartas_ia[posicion_carta_ia][1]} de {cartas_ia[posicion_carta_ia][0]}')
            cartas_ia.pop(posicion_carta_ia)
            print()

            que_canta = recuperar_canto(valor_mano)
            if valor_mano < 4:
                canta = input(f'Quiere cantar {que_canta}? SI/NO  ').upper()
                if canta == 'SI':
                    respuesta_ia = recuperar_respuesta_ia(promedio_cartas_ia, valor_mano)
                    if respuesta_ia == 1:
                        print('La IA aceptó')
                        valor_mano = valor_mano + 1
                    else:
                        print('La IA rechazó')
                        mano_puntos_usuario = 2
                        continue
            print('Seleccione la posicion de una de sus cartas: ')
            for carta in cartas_usuario:
                print(f'{carta[1]} de {carta[0]}')

            pregunta = recuperar_pregunta(len(cartas_usuario))
            posicion_carta_elegida = int(input('Seleccione 0 para irse al mazo o ' + pregunta))
            print()

            if posicion_carta_elegida == 0:
                mano_puntos_ia = 2
                continue
            carta_elegida = cartas_usuario[posicion_carta_elegida - 1]
            valor_carta_elegida = valores_cartas_usuario[posicion_carta_elegida - 1]

            print(
                f'El jugador tiro la carta {cartas_usuario[posicion_carta_elegida - 1][1]} de {cartas_usuario[posicion_carta_elegida - 1][0]}')
            cartas_usuario.pop(posicion_carta_elegida - 1)
            print()

        if valor_carta_elegida > valor_carta_ia:
            mano_puntos_usuario = mano_puntos_usuario + 1
            juega_jugador = True
            print('El usuario ganó la mano')
        elif valor_carta_ia > valor_carta_elegida:
            mano_puntos_ia = mano_puntos_ia + 1
            juega_jugador = False
            print('La IA ganó la mano')
        elif valor_carta_elegida == valor_carta_ia:
            mano_puntos_usuario = mano_puntos_usuario + 1
            mano_puntos_ia = mano_puntos_ia + 1
            print('Empataron la mano')
        print()
    else:
        if mano_puntos_usuario == 2:
            puntos_usuario = puntos_usuario + valor_mano
            print('El usuario ganó la mano')
        else:
            puntos_ia = puntos_ia + valor_mano
            print('La IA ganó la mano')
