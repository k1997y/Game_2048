import pygame
import Board

# スクリーンサイズ
#SCREEN = pygame.Rect(0,0,400,400)

def main():
    pygame.init()
    screen=pygame.display.set_mode((400,400))
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

    # 盤面準備
    board = Board.Board()

    # クロック準備
    clock=pygame.time.Clock()

    # ゲームループ開始
    while True:
        clock.tick(60)  #60fps

        # 塗りつぶす範囲のRectを作成
        r = pygame.Rect(0,0,board.WIDTH,board.HEIGHT)
        color = pygame.Color(169,169,169)
        screen.fill(color,rect=r)    # 灰色で塗りつぶす
        

if __name__ == "__main__":
    main()