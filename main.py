import pygame as pg


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
                print(index)
                dibujarCirculoEn(columnaX, filaY)
            columnaX += 100
            index += 1
        columnaX = 200
        filaY += 100


pg.init()

window = pg.display.set_mode((640, 480))
window.fill((255, 255, 255))

run = True

linesColor = (0, 0, 0)
crossColor = (80,80,80)
circleColor = (80,80,80)

point1 = (200, 200)
point2 = (500, 200)
point3 = (200, 300)
point4 = (500, 300)

point5 = (300, 100)
point6 = (300, 400)
point7 = (400, 100)
point8 = (400, 400)

while run:
    pg.draw.line(window, linesColor, point1, point2)
    pg.draw.line(window, linesColor, point3, point4)
    pg.draw.line(window, linesColor, point5, point6)
    pg.draw.line(window, linesColor, point7, point8)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN:
            escanearClicks(pg.mouse.get_pos())

    pg.display.update()

pg.quit()
