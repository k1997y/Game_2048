# 方策勾配法による学習
import Board
import sys
import numpy as np

def main():
    # 盤面準備
    board = Board.Board()
    #print(board.tiles) 

    # パラメータθの初期値設定
    theta_0 = np.ones([16,4])
    print(board.tiles)

    # TODO: タイルの番号によってパラメータを変える必要あり
    # 0:上, 1:右, 2:下, 3:左
    for row in range(4):
        for column in range(4):
            if board.tiles[row,column] == 0:
                theta_0[row*4+column,0] = np.nan
                theta_0[row*4+column,1] = np.nan
                theta_0[row*4+column,2] = np.nan
                theta_0[row*4+column,3] = np.nan
            else:
                board.setParameter(row,column,theta_0)

    print(theta_0)
    methods_0 = board.convertParametersToMethods(theta_0)
    print(methods_0)
                


    # ゲームループ開始
    while True:
        # w:up, s: down, a: left, d: right
        key = input()

        if key == 'w':
            if board.keyUp():
                board.genTileRandomly()
        elif key == 's':
            if board.keyDown():
                board.genTileRandomly()
        elif key == 'a':
            if board.keyLeft():
                board.genTileRandomly()
        elif key == 'd':
            if board.keyRight():
                board.genTileRandomly()
        elif key == "quit":
            sys.exit()

        print(board.tiles)

if __name__ == "__main__":
    main()

