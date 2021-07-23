import Board
import sys

def main():
    # 盤面準備
    board = Board.Board()
    print(board.tiles)  

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
