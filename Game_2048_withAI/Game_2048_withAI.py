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
            board.keyUp()
        elif key == 's':
            board.keyDown()
        elif key == 'a':
            board.keyLeft()
        elif key == 'd':
            board.keyRight()
        elif key == "quit":
            sys.exit()

        print(board.tiles)

if __name__ == "__main__":
    main()
