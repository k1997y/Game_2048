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
        self.genTileRandomly()
        self.genTileRandomly()
    
    # upキーを押したときの挙動を定義
    def keyUp(self):
        i = 0
        while True:
            # どのタイルも動かなくなるまで繰り返す
            if self.oneUpTile(self.tiles):
                break
            i = i + 1
        if i != 0:
            self.genTileRandomly()


        

    # 1マスだけ全てのタイルを上に上げる
    # どのタイルも動かなかったらTrueを返す
    def oneUpTile(self,tiles):
        flag = True
        for i in range(3):
            for j in range(4):
                # 上のマスがblankだった場合
                if tiles[i,j] == 0 and tiles[i + 1,j] != 0:
                    tiles[i,j] = tiles[i + 1,j]
                    tiles[i + 1,j] = 0
                    flag = False
                # 上のマスと下のマスの番号が同じ場合マージする
                elif tiles[i,j] == tiles[i + 1,j] and tiles[i,j] != 0:
                    tiles[i,j] = tiles[i,j] * 2
                    tiles[i + 1,j] = 0
                    flag = False
        return flag

    # 1マスだけ全てのタイルを右に移動する
    # どのタイルも動かなかったらTrueを返す



    # 予め設定された確率で2か4を盤面上に生成する
    def genTileRandomly(self):
         genNum = 0
         if self.P_2 > random.random():
            genNum = 2
         else:
            genNum = 4

         while(True):
            rand_i = random.randrange(0,3,1)
            rand_j = random.randrange(0,3,1)
            if self.tiles[rand_i][rand_j] == 0:
                self.tiles[rand_i,rand_j] = genNum
                break