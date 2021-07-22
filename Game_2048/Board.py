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
    # タイルが動いたらTrue, 1つも動かなかったらFalse
    def keyUp(self):
        i = 0
        while True:
            # どのタイルも動かなくなるまで繰り返す
            if self.moveTilesUp(self.tiles):
                break
            i = i + 1
        if i != 0:
            #self.genTileRandomly()
            return True

    def keyUp(self):
        flag = False    # タイルが1つも動かないままならFalseとなる
        for column in range(4):
            # 縦に4つ同じ数字が並んでいる場合上半分、下半分でそれぞれマージを行う
            if self.tiles[0,column] == self.tiles[1,column] and self.tiles[1,column] == self.tiles[2,column] and self.tiles[2,column] == self.tiles[3,column] and self.tiles[0,column] != 0:
                self.tiles[0,column] = self.tiles[0,column] * 2
                self.tiles[1,column] = self.tiles[2,column] * 2
                self.tiles[2,column] = 0
                self.tiles[3,column] = 0
                flag = True
            elif self.moveTilesUp(self.tiles,column):
                flag = True
        return flag


    # downキーを押したときの挙動を定義
    def keyDown(self):
        i = 0
        while True:
            # どのタイルも動かなくなるまで繰り返す
            if self.oneDownTile(self.tiles):
                break
            i = i + 1
        if i != 0:
            self.genTileRandomly()

     # leftキーを押したときの挙動を定義
    def keyLeft(self):
        i = 0
        while True:
            # どのタイルも動かなくなるまで繰り返す
            if self.oneLeftTile(self.tiles):
                break
            i = i + 1
        if i != 0:
            self.genTileRandomly()

    # rightキーを押したときの挙動を定義
    def keyRight(self):
        i = 0
        while True:
            # どのタイルも動かなくなるまで繰り返す
            if self.oneRightTile(self.tiles):
                break
            i = i + 1
        if i != 0:
            self.genTileRandomly()


        

    # TODO: フラグ変数が多く可読性が低いため、関数で分割するなど工夫できないか
    # 指定された行のタイルを上に移動させる
    def moveTilesUp(self,tiles,column):
        isMovedInThisLoop = True # その周で1度でも動いたらTrueにする
        isNotMerged = True  # マージ済みならFalse
        isMoved = False # この関数内で1度も動かなかったらFalse

        # タイルが動かなくなるまでループする
        while isMovedInThisLoop:
            isMovedInThisLoop = False
            for row in range(3):
                # 上のマスが空ならタイルを移動
                if tiles[row,column] == 0 and tiles[row + 1,column] != 0:
                    tiles[row,column] = tiles[row + 1,column]
                    tiles[row + 1,column] = 0
                    isMovedInThisLoop = True
                    isMoved = True
                # 上のマスと下のマスの数字が同じ場合マージする(既にこの列でマージがあった場合はマージしない)
                elif tiles[row,column] == tiles[row + 1,column] and tiles[row,column] != 0 and isNotMerged:
                        tiles[row,column] = tiles[row,column] * 2
                        tiles[row + 1,column] = 0
                        isNotMerged = False
                        isMovedInThisLoop = True
                        isMoved = True
        return isMoved

        #flag = True
        #for i in range(3):
        #    for j in range(4):
        #        # 上のマスがblankだった場合
        #        if tiles[i,j] == 0 and tiles[i + 1,j] != 0:
        #            tiles[i,j] = tiles[i + 1,j]
        #            tiles[i + 1,j] = 0
        #            flag = False
        #        # 上のマスと下のマスの番号が同じ場合マージする
        #        elif tiles[i,j] == tiles[i + 1,j] and tiles[i,j] != 0:
        #            tiles[i,j] = tiles[i,j] * 2
        #            tiles[i + 1,j] = 0
        #            flag = False
        #return flag


     # 1マスだけ全てのタイルを下に上げる
    # どのタイルも動かなかったらTrueを返す
    def oneDownTile(self,tiles):
        flag = True
        for i in range(3):
            for j in range(4):
                # 下のマスがblankだった場合
                if tiles[i + 1,j] == 0 and tiles[i,j] != 0:
                    tiles[i + 1,j] = tiles[i,j]
                    tiles[i,j] = 0
                    flag = False
                # 上のマスと下のマスの番号が同じ場合マージする
                elif tiles[i + 1,j] == tiles[i,j] and tiles[i + 1,j] != 0:
                    tiles[i + 1,j] = tiles[i + 1,j] * 2
                    tiles[i ,j] = 0
                    flag = False
        return flag

    # 1マスだけ全てのタイルを左に移動する
    # どのタイルも動かなかったらTrueを返す
    def oneLeftTile(self,tiles):
        flag = True
        for i in range(4):
            for j in range(3):
                # 左のマスがblankだった場合
                if tiles[i,j] == 0 and tiles[i,j + 1] != 0:
                    tiles[i,j] = tiles[i,j + 1]
                    tiles[i,j + 1] = 0
                    flag = False
                # 左のマスと番号が同じ場合マージする
                elif tiles[i,j] == tiles[i ,j + 1] and tiles[i,j + 1] != 0:
                    tiles[i,j] = tiles[i,j] * 2
                    tiles[i,j + 1] = 0
                    flag = False
        return flag

    # 1マスだけ全てのタイルを右に移動する
    # どのタイルも動かなかったらTrueを返す
    def oneRightTile(self,tiles):
        flag = True
        for i in range(4):
            for j in range(3):
                # 右のマスがblankだった場合
                if tiles[i,j + 1] == 0 and tiles[i,j] != 0:
                    tiles[i,j + 1] = tiles[i,j]
                    tiles[i,j] = 0
                    flag = False
                # 右のマスと番号が同じ場合マージする
                elif tiles[i,j + 1] == tiles[i ,j] and tiles[i,j] != 0:
                    tiles[i,j + 1] = tiles[i,j + 1] * 2
                    tiles[i,j] = 0
                    flag = False
        return flag


    # 予め設定された確率で2か4を盤面上に生成する
    def genTileRandomly(self):
         genNum = 0
         if self.P_2 > random.random():
            genNum = 2
         else:
            genNum = 4

         while(True):
            rand_i = random.randrange(0,4,1)
            rand_j = random.randrange(0,4,1)
            if self.tiles[rand_i][rand_j] == 0:
                self.tiles[rand_i,rand_j] = genNum
                break