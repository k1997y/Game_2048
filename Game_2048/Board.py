import pygame
import numpy as np

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
        flag = False    # タイルが1つも動かないままならFalseとなる
        for column in range(4):
            # 縦に4つ同じ数字が並んでいる場合上半分、下半分でそれぞれマージを行う
            if self.tiles[0,column] == self.tiles[1,column] and self.tiles[1,column] == self.tiles[2,column] and self.tiles[2,column] == self.tiles[3,column] and self.tiles[0,column] != 0:
                self.tiles[0,column] = self.tiles[0,column] * 2
                self.tiles[1,column] = self.tiles[2,column] * 2
                self.tiles[2,column] = 0
                self.tiles[3,column] = 0
                flag = True
            # 上半分に同じ数字、下半分に同じ数字が並んでいる場合、上半分、下半分でそれぞれマージを行う
            elif self.tiles[0,column] == self.tiles[1,column] and self.tiles[2,column] == self.tiles[3,column]:
                self.tiles[0,column] = self.tiles[0,column] * 2
                self.tiles[1,column] = self.tiles[2,column] * 2
                self.tiles[2,column] = 0
                self.tiles[3,column] = 0
                flag= True
            elif self.moveTilesUp(self.tiles,column):
                flag = True
        return flag

    # downキーを押したときの挙動を定義
    def keyDown(self):
        flag = False    # タイルが1つも動かないままならFalseとなる
        for column in range(4):
            # 縦に4つ同じ数字が並んでいる場合上半分、下半分でそれぞれマージを行う
            if self.tiles[0,column] == self.tiles[1,column] and self.tiles[1,column] == self.tiles[2,column] and self.tiles[2,column] == self.tiles[3,column] and self.tiles[0,column] != 0:
                self.tiles[3,column] = self.tiles[3,column] * 2
                self.tiles[2,column] = self.tiles[1,column] * 2
                self.tiles[1,column] = 0
                self.tiles[0,column] = 0
                flag = True
            # 上半分に同じ数字、下半分に同じ数字が並んでいる場合、上半分、下半分でそれぞれマージを行う
            elif self.tiles[0,column] == self.tiles[1,column] and self.tiles[2,column] == self.tiles[3,column]:
                self.tiles[3,column] = self.tiles[3,column] * 2
                self.tiles[2,column] = self.tiles[1,column] * 2
                self.tiles[1,column] = 0
                self.tiles[0,column] = 0
                flag= True
            elif self.moveTilesDown(self.tiles,column):
                flag = True
        return flag

    # leftキーを押したときの挙動を定義
    def keyLeft(self):
        flag = False    # タイルが1つも動かないままならFalseとなる
        for row in range(4):
            # 横に4つ同じ数字が並んでいる場合左半分、右半分でそれぞれマージを行う
            if self.tiles[row,0] == self.tiles[row,1] and self.tiles[row,1] == self.tiles[row,2] and self.tiles[row,2] == self.tiles[row,3] and self.tiles[row,0] != 0:
                self.tiles[row,0] = self.tiles[row,0] * 2
                self.tiles[row,1] = self.tiles[row,2] * 2
                self.tiles[row,2] = 0
                self.tiles[row,3] = 0
                flag = True
                # 上半分に同じ数字、下半分に同じ数字が並んでいる場合、上半分、下半分でそれぞれマージを行う
            elif self.tiles[row,0] == self.tiles[row,1] and self.tiles[row,2] == self.tiles[row,3]:
                self.tiles[row,0] = self.tiles[row,0] * 2
                self.tiles[row,1] = self.tiles[row,2] * 2
                self.tiles[row,2] = 0
                self.tiles[row,3] = 0
                flag= True
            elif self.moveTilesLeft(self.tiles,row):
                flag = True
        return flag

    # rightキーを押したときの挙動を定義
    def keyRight(self):
        flag = False    # タイルが1つも動かないままならFalseとなる
        for row in range(4):
            # 横に4つ同じ数字が並んでいる場合左半分、右半分でそれぞれマージを行う
            if self.tiles[row,0] == self.tiles[row,1] and self.tiles[row,1] == self.tiles[row,2] and self.tiles[row,2] == self.tiles[row,3] and self.tiles[row,0] != 0:
                self.tiles[row,3] = self.tiles[row,3] * 2
                self.tiles[row,2] = self.tiles[row,1] * 2
                self.tiles[row,1] = 0
                self.tiles[row,0] = 0
                flag = True
            # 上半分に同じ数字、下半分に同じ数字が並んでいる場合、上半分、下半分でそれぞれマージを行う
            elif self.tiles[row,0] == self.tiles[row,1] and self.tiles[row,2] == self.tiles[row,3]:
                self.tiles[row,3] = self.tiles[row,3] * 2
                self.tiles[row,2] = self.tiles[row,1] * 2
                self.tiles[row,1] = 0
                self.tiles[row,0] = 0
                flag= True
            elif self.moveTilesRight(self.tiles,row):
                flag = True
        return flag

    # TODO: フラグ変数が多く可読性が低いため、関数で分割するなど工夫できないか
    # 指定された列のタイルを上に移動させる
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

     # 指定された列のタイルを下に移動させる
    def moveTilesDown(self,tiles,column):
        isMovedInThisLoop = True # その周で1度でも動いたらTrueにする
        isNotMerged = True  # マージ済みならFalse
        isMoved = False # この関数内で1度も動かなかったらFalse

        # タイルが動かなくなるまでループする
        while isMovedInThisLoop:
            isMovedInThisLoop = False
            for row in range(3):
                # 下のマスが空ならタイルを移動
                if tiles[3 - row,column] == 0 and tiles[2 - row,column] != 0:
                    tiles[3 - row,column] = tiles[2 - row,column]
                    tiles[2 - row,column] = 0
                    isMovedInThisLoop = True
                    isMoved = True
                # 上のマスと下のマスの数字が同じ場合マージする(既にこの列でマージがあった場合はマージしない)
                elif tiles[3 - row,column] == tiles[2 - row,column] and tiles[3 - row,column] != 0 and isNotMerged:
                        tiles[3 - row,column] = tiles[3 - row,column] * 2
                        tiles[2 - row,column] = 0
                        isNotMerged = False
                        isMovedInThisLoop = True
                        isMoved = True
        return isMoved

     # 指定された行のタイルを左に移動させる
    def moveTilesLeft(self,tiles,row):
        isMovedInThisLoop = True # その周で1度でも動いたらTrueにする
        isNotMerged = True  # マージ済みならFalse
        isMoved = False # この関数内で1度も動かなかったらFalse

        # タイルが動かなくなるまでループする
        while isMovedInThisLoop:
            isMovedInThisLoop = False
            for column in range(3):
                # 左のマスが空ならタイルを移動
                if tiles[row,column] == 0 and tiles[row,column + 1] != 0:
                    tiles[row,column] = tiles[row,column + 1]
                    tiles[row ,column + 1] = 0
                    isMovedInThisLoop = True
                    isMoved = True
                # 上のマスと下のマスの数字が同じ場合マージする(既にこの行でマージがあった場合はマージしない)
                elif tiles[row,column] == tiles[row,column + 1] and tiles[row,column] != 0 and isNotMerged:
                        tiles[row,column] = tiles[row,column] * 2
                        tiles[row ,column + 1] = 0
                        isNotMerged = False
                        isMovedInThisLoop = True
                        isMoved = True
        return isMoved

      # 指定された行のタイルを右に移動させる
    def moveTilesRight(self,tiles,row):
        isMovedInThisLoop = True # その周で1度でも動いたらTrueにする
        isNotMerged = True  # マージ済みならFalse
        isMoved = False # この関数内で1度も動かなかったらFalse

        # タイルが動かなくなるまでループする
        while isMovedInThisLoop:
            isMovedInThisLoop = False
            for column in range(3):
                # 右のマスが空ならタイルを移動
                if tiles[row,3 - column] == 0 and tiles[row,2 - column] != 0:
                    tiles[row,3 - column] = tiles[row,2 - column]
                    tiles[row ,2 - column] = 0
                    isMovedInThisLoop = True
                    isMoved = True
                # 右のマスと左のマスの数字が同じ場合マージする(既にこの行でマージがあった場合はマージしない)
                elif tiles[row,3 - column] == tiles[row,2 - column] and tiles[row,3 - column] != 0 and isNotMerged:
                        tiles[row,3 - column] = tiles[row,3 - column] * 2
                        tiles[row ,2 - column] = 0
                        isNotMerged = False
                        isMovedInThisLoop = True
                        isMoved = True
        return isMoved

    # 予め設定された確率で2か4を盤面上に生成する
    def genTileRandomly(self):
         genNum = 0
         if self.P_2 > np.random.random():
            genNum = 2
         else:
            genNum = 4

         while(True):
            rand_i = np.random.randint(0,4)
            rand_j = np.random.randint(0,4)
            if self.tiles[rand_i][rand_j] == 0:
                self.tiles[rand_i,rand_j] = genNum
                break