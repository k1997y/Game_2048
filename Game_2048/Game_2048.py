import pygame
import Board

# スクリーンサイズ
#SCREEN = pygame.Rect(0,0,400,400)
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 1024
# フォントサイズ
FONT_SIZE = 50

def main():
    pygame.init()
    screen = pygame.display.set_mode((1024,1024))
    pygame.display.set_caption("2048")

    # 画像パス準備
    #filenames = []
    #filenames.append("2048_material/tile_2.png")
    #filenames.append("2048_material/tile_4.png")
    #filenames.append("2048_material/tile_8.png")
    #filenames.append("2048_material/tile_16.png")
    #filenames.append("2048_material/tile_32.png")
    #filenames.append("2048_material/tile_64.png")
    #filenames.append("2048_material/tile_128.png")
    #filenames.append("2048_material/tile_256.png")
    #filenames.append("2048_material/tile_512.png")
    #filenames.append("2048_material/tile_1024.png")
    #filenames.append("2048_material/tile_2048.png")
    #filenames.append("2048_material/tile_tile_blank.png")

    #フォントの設定
    font = pygame.font.Font(None,FONT_SIZE)
    

    # 盤面準備
    board = Board.Board()
    screen.fill("#92877d")
    pygame.display.flip()

    # 盤面描画
    for i in range(4):
        for j in range(4):
            tile = pygame.Rect((j + 1) * board.INTERVAL + j * board.TILE_WIDTH,(i+1)*board.INTERVAL+i*board.TILE_HEIGHT,board.TILE_WIDTH,board.TILE_HEIGHT)
            color = getColorFromNum(board.tiles[i,j])
            screen.fill(color,rect=tile)
            # 数字の色を決める
            if board.tiles[i,j] == 2 or board.tiles[i,j] == 4 :
                color= pygame.Color("#000000")
            else:
                color = pygame.Color("#FFFFFF")
            # 数字をタイル上に出力する
            if board.tiles[i,j] != 0:
                text = font.render(str(board.tiles[i,j]),True,color)
                screen.blit(text,tile)



    pygame.display.flip()
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)

    # クロック準備
    #clock=pygame.time.Clock()

    # ゲームループ開始
    #while True:
    #    #clock.tick(60) #60fps

    #    # 塗りつぶす範囲のRectを作成
    #    r = pygame.Rect(0,0,board.BOARD_WIDTH,board.BOARD_HEIGHT)
    #    color = pygame.Color(169,169,169)
    #    screen.fill(color,rect=r) # 灰色で塗りつぶす
    #    pygame.display.flip()
      
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



if __name__ == "__main__":
    main()