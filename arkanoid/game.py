import os

import pygame as pg

from arkanoid import ALTO, ANCHO
from arkanoid.escenas import Portada, Partida, HallOfFame


class Arkanoid:
    def __init__(self) -> None:
        print("Arranaca el juego!!")
        pg.init()
        self.display = pg.display.set_mode((ANCHO, ALTO))
        pg.display.set_caption("Arkanoid BZ XI")

        icon = pg.image.load(os.path.join("resources", "images", "ball1.png"))
        pg.display.set_icon(icon)

        self.escenas = [
            Portada(self.display),
            Partida(self.display),
            HallOfFame(self.display),
        ]

    def jugar(self):
        """Este es el bucle principal"""
        #salir = False
        # while not salir:
        # for event in pg.event.get():
        # if event.type == pg.QUIT:
        #salir = True
        #self.display.fill((99, 99, 99))
        # pg.display.flip()
        for escena in self.escenas:
            escena.bucle_principal()


if __name__ == "__main__":
    game = Arkanoid()
    game.jugar()
