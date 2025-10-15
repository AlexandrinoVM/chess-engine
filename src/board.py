import cairosvg 
import pygame
import io
from pathlib import Path
import os
class Board:
    def __init__(self) -> None:
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.path = "./assets/images/pieces/"
        self.surfaces  ={}
        self.tiles = {}
        self.get_svgs()
        self.setup_tiles()
        self.setup_pieces()


    def setup_tiles(self):
       pasta_path = Path("./assets/images/tiles/")
       for arquivo in pasta_path.glob("*.svg"):
           if arquivo.is_file():
               try:
                   tile_name = arquivo.stem
                   self.tiles[tile_name] = self.svg_to_surface(str(arquivo))

               except Exception as e:
                   print(f"ERROR LOADING TILES")


    def get_svgs(self):
       pasta_path = Path(self.path)
       for arquivo in pasta_path.glob("*.svg"):
           if arquivo.is_file():
               try:
                    piece_name = arquivo.stem
                    self.surfaces[piece_name] = self.svg_to_surface(str(arquivo))

               except Exception as e:
                    print(f"ERROR LOADIND IMAGES")

    def svg_to_surface(self,svg_path,size=80):
        png_data = cairosvg.svg2png(url=svg_path,output_width=80,output_height=80)
        return pygame.image.load(io.BytesIO(png_data))


    def drawBoard(self,screen):
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if (row + col)% 2 != 0:
                    screen.blit(self.tiles["brown_dark"],(col*80,row*80))
                else:
                    screen.blit(self.tiles["brown_light"],(col*80,row*80))
                if piece:
                    screen.blit(self.surfaces[piece],(col*80,row*80))

    def setup_pieces(self):
        self.board[0] = [
                "b_rook", "b_knight", "b_bishop", "b_queen",
                "b_king", "b_bishop", "b_knight", "b_rook"
                ]
        self.board[1] = ["b_pawn" for  _ in range(8)]

        for row in range(2,6):
            self.board[row] = [None for _ in range(8)]

        self.board[6] = ["w_pawn" for _ in range(8)]
        self.board[7] = [
                "w_rook", "w_knight", "w_bishop", "w_queen",
                "w_king", "w_bishop", "w_knight", "w_rook"
                ]
