import pygame
from pygame.locals import *
import Board
import sys

# スクリーンサイズ
#SCREEN = pygame.Rect(0,0,400,400)
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 1024
# フォントサイズ
FONT_SIZE = 70

def main():
    pygame.init()
    screen = pygame.display.set_mode((1024,1024))
    pygame.display.set_caption("2048")

    #フォントの設定
    font = pygame.font.Font(None,FONT_SIZE)
    
    # 盤面準備
    board = Board.Board()
    screen.fill("#92877d")
    pygame.display.flip()

    # 盤面描画
    drawBoard(font,screen,board)       

    pygame.display.flip()
    clock = pygame.time.Clock()

    # ゲームループ開始
    while True:
        pygame.time.wait(30)

        # イベントの処理
        for event in pygame.event.get():
             # ESCが押されたらプログラムを終了する
            if event.type == QUIT:
                sys.exit()

            # キーを押下したとき
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
                elif event.key == K_UP:
                    if board.keyUp():
                        board.genTileRandomly()
                elif event.key == K_DOWN:
                    board.keyDown()
                elif event.key == K_LEFT:
                    board.keyLeft()
                elif event.key == K_RIGHT:
                    board.keyRight()

        # 画面更新
        drawBoard(font,screen,board)
        pygame.display.flip()
                
      
# 数字によって違った色を返す
def getColorFromNum(number):
    if number == 0:
        return pygame.Color("#9e948a")
    elif number == 2:
        return pygame.Color("#eee4da")
    elif number == 4:
        return pygame.Color("#ede0c8")
    elif number == 8:
        return pygame.Color("#f2b179")
    elif number == 16:
        return pygame.Color("#f59563")
    elif number == 32:
        return pygame.Color("#f67c5f")
    elif number == 64:
        return pygame.Color("#f65e3b")
    elif number == 128:
        return pygame.Color("#edcf72")
    elif number == 256:
        return pygame.Color("#edcc61")
    elif number == 512:
        return pygame.Color("#edc850")
    elif number == 1024:
        return pygame.Color("#edc53f")
    elif number == 2048:
        return pygame.Color("#edc22e")

# 盤面の描画
def drawBoard(font,screen,board):
      for i in range(4):
        for j in range(4):
            tile = pygame.Rect((j + 1) * board.INTERVAL + j * board.TILE_WIDTH,(i + 1) * board.INTERVAL + i * board.TILE_HEIGHT,board.TILE_WIDTH,board.TILE_HEIGHT)
            color = getColorFromNum(board.tiles[i,j])
            screen.fill(color,rect=tile)
            # 数字の色を決める
            if board.tiles[i,j] == 2 or board.tiles[i,j] == 4 :
                color = pygame.Color("#000000")
            else:
                color = pygame.Color("#FFFFFF")
            # 数字をタイル上に出力する
            if board.tiles[i,j] != 0:
                text = font.render(str(board.tiles[i,j]),True,color)
                # TODO: 文字の位置が適切でないため修正必要
                screen.blit(text,[(j + 1) * board.INTERVAL + j * board.TILE_WIDTH + (board.TILE_WIDTH / 3),(i + 1) * board.INTERVAL + i * board.TILE_HEIGHT + (board.TILE_HEIGHT / 3)])
               

if __name__ == "__main__":
    main()