import pygame as pg
import random

posicionesPosibles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
casillasOcupadas = [0, 0, 0,
                    0, 0, 0,
                    0, 0, 0]  # 1 = Circulo, 2 = Cruz

jugadorGanador = ""

gano = False

def escanearFilasPara(num):
    if (casillasOcupadas[0] == num and casillasOcupadas[1] == num and casillasOcupadas[2] == num) or \
            (casillasOcupadas[3] == num and casillasOcupadas[4] == num and casillasOcupadas[5] == num) or \
            (casillasOcupadas[6] == num and casillasOcupadas[7] == num and casillasOcupadas[8] == num):
        return True
    return False


def escanearColumnasPara(num):
    if (casillasOcupadas[0] == num and casillasOcupadas[3] == num and casillasOcupadas[6] == num) or \
            (casillasOcupadas[1] == num and casillasOcupadas[4] == num and casillasOcupadas[7] == num) or \
            (casillasOcupadas[2] == num and casillasOcupadas[5] == num and casillasOcupadas[8] == num):
        return True
    return False


def escanearDiagonalesPara(num):
    if (casillasOcupadas[0] == num and casillasOcupadas[4] == num and casillasOcupadas[8] == num) or \
            (casillasOcupadas[2] == num and casillasOcupadas[4] == num and casillasOcupadas[6] == num):
        return True
    return False


def escanearGanador():
    global jugadorGanador

    if escanearFilasPara(1) or escanearColumnasPara(1) or escanearDiagonalesPara(1):
        jugadorGanador = "Circulo"
        return True

    if escanearFilasPara(2) or escanearColumnasPara(2) or escanearDiagonalesPara(2):
        jugadorGanador = "Cruz"
        return True

    return False


def generarMovimientoDeMaquina():
    if len(posicionesPosibles) == 0:
        return
    posicionUsada = posicionesPosibles[random.randrange(0, len(posicionesPosibles))]

    index = 1

    columnaX = 200
    filaY = 100

    for fila in range(0, 3):
        for columna in range(0, 3):
            if index == posicionUsada:
                # Genero la cruz
                dibujarCruzEn(columnaX, filaY)
                casillasOcupadas[index - 1] = 2
                posicionesPosibles.remove(index)

                global turno
                turno = 0

                return

            columnaX += 100
            index += 1
        columnaX = 200
        filaY += 100


def dibujarCruzEn(columna, fila):
    pg.draw.line(window, crossColor, (columna + 80, fila + 20), (columna + 20, fila + 80), 5)
    pg.draw.line(window, crossColor, (columna + 20, fila + 20), (columna + 80, fila + 80), 5)


def dibujarCirculoEn(columna, fila):
    pg.draw.circle(window, circleColor, (columna + 50, fila + 50), 40, 5)


def escanearClicks(mousePos):
    posX, posY = mousePos[0], mousePos[1]

    index = 1

    columnaX = 200
    filaY = 100

    for fila in range(0, 3):
        for columna in range(0, 3):
            if columnaX < posX < columnaX + 100 and filaY < posY < filaY + 100:
                if index not in posicionesPosibles:
                    return

                # Genero el circulo
                dibujarCirculoEn(columnaX, filaY)
                casillasOcupadas[index - 1] = 1
                posicionesPosibles.remove(index)

                global turno
                turno = 1

                print(casillasOcupadas)

                return
            columnaX += 100
            index += 1
        columnaX = 200
        filaY += 100


pg.init()

window = pg.display.set_mode((640, 480))
window.fill((255, 255, 255))

run = True

linesColor = (0, 0, 0)
crossColor = (46, 53, 255)
circleColor = (255, 41, 41)

point1 = (200, 200)
point2 = (500, 200)
point3 = (200, 300)
point4 = (500, 300)

point5 = (300, 100)
point6 = (300, 400)
point7 = (400, 100)
point8 = (400, 400)

# 0 = Jugador, 1 = Maquina
turno = 0

while run:
    pg.draw.line(window, linesColor, point1, point2)
    pg.draw.line(window, linesColor, point3, point4)
    pg.draw.line(window, linesColor, point5, point6)
    pg.draw.line(window, linesColor, point7, point8)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if not gano:
                if turno == 0:
                    escanearClicks(pg.mouse.get_pos())
                if turno == 1:
                    generarMovimientoDeMaquina()

                ganoJuego = escanearGanador()

                if ganoJuego:
                    gano = True
                    print(jugadorGanador)

    pg.display.update()

pg.quit()
