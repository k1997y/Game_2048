class Board():
    # filenames: ファイルパスのリスト
    def __init__(self,filenames):
        pygame.sprite.Sprite.__init__(self,self.containers)

        # 画像データをロードする
        self.images = []
        for filename in filenames:
            self.images.append(pygame.image.load(filename).convert())

        self.score=0

