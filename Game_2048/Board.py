import pygame
import numpy as np
import random

class Board():
    # 定数
    BOARD_WIDTH = 500 # 盤面の幅
    BOARD_HEIGHT = 500 # 盤面の高さ
    TILE_WIDTH = 100 # タイルの幅
    TILE_HEIGHT = 100 # タイルの高さ
    INTERVAL = 25 # タイル間の隙間
    P_2 = 0.9 # 2の出現確率
    P_4 = 0.1 # 4の出現確率


    # filenames: ファイルパスのリスト
    def __init__(self):
        #pygame.sprite.Sprite.__init__(self)

        # 画像データをロードする
        #self.images = []
        #for filename in filenames:
        #    self.images.append(pygame.image.load(filename).convert())

        self.score = 0

        # 盤面の2次元配列の作成
        self.tiles = np.zeros((4,4),dtype = "uint8")
        #self.tiles = [[0 for i in range(4)] for j in range(4)]
        #for i in range(4):
        #    for j in range(4):
        #        #self.tiles[i][j] = Tile.Tile(None)
        #        self.tiles[i][j] = 0


        #self.tiles = []
        #for i in range(4):
        #    sublist = []
        #    for j in range(4):
        #        sublist.append(Tile.Tile(None) #blankで埋める
        #        #self.tiles[i][j] = Tile.Tile(None) #blankで埋める
        #    self.tiles.append(sublist)

        # ランダムで盤面に2枚のタイルを作成する
        rand_i = random.randrange(0,3,1)
        rand_j = random.randrange(0,3,1)
        #self.tiles[rand_i][rand_j] = Tile.Tile(self.genTileRandomly())
        self.tiles[rand_i,rand_j]=self.genTileRandomly()

        # 1枚目のタイルと被りがあるなら再度他の場所に生成する
        while(True):
            rand_i = random.randrange(0,3,1)
            rand_j = random.randrange(0,3,1)
            if self.tiles[rand_i][rand_j] == 0:
                #self.tiles[rand_i][rand_j] = Tile.Tile(self.genTileRandomly())
                self.tiles[rand_i,rand_j]=self.genTileRandomly()
                break

    # 予め設定された確率で2or4のタイルを出す
    def genTileRandomly(self):
        if self.P_2 > random.random():
            return 2
        else:
            return 4