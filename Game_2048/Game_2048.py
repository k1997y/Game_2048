import pygame

# スクリーンサイズ
SCREEN = Rect(0,0,400,400)

def main():
    pygame.init()
    screen=pygame.display.set_mode(SCREEN.size)
    pygame.display.set_caption("2048")

    # 画像パス準備
    filenames = []
    filenames.append("2048_material/tile_2.png")
    filenames.append("2048_material/tile_4.png")
    filenames.append("2048_material/tile_8.png")
    filenames.append("2048_material/tile_16.png")
    filenames.append("2048_material/tile_32.png")
    filenames.append("2048_material/tile_64.png")
    filenames.append("2048_material/tile_128.png")
    filenames.append("2048_material/tile_256.png")
    filenames.append("2048_material/tile_512.png")
    filenames.append("2048_material/tile_1024.png")
    filenames.append("2048_material/tile_2048.png")
    filenames.append("2048_material/tile_tile_blank.png")

    # 盤面準備
    board = Board(filenames)

    # クロック準備
    clock=pygame.time.Clock()

if __name__ == "__main__":
    main()