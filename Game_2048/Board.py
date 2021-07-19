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

    def __init__(self):
        self.score = 0

        # 盤面の2次元配列の作成
        self.tiles = np.zeros((4,4),dtype = "uint8")

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

    # upキーを押したときの挙動を定義
    def keyUp(self):
        while True:
            # どのタイルも動かなくなるまで繰り返す
            if self.oneUpTile(self.tiles):
                break


    # 1マスだけ全てのタイルを上に上げる
    # どのタイルも動かなかったらFalseを返す
    def oneUpTile(self,tiles):
        flag = False
        for i in range(3):
            for j in range(4):
                # 上のマスがblankだった場合
                if tiles[i,j] == 0:
                    tiles[i,j] = tiles[i+1,j]
                    tiles[i+1,j] = 0
                    flag = True
        return flag
