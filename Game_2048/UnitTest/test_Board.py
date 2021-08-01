import unittest
import Board
import numpy as np

# Boardの単体テスト
class TestBoard(unittest.TestCase):
    #board = None
    # 全体前処理
    #@classmethod
    #def setUpClass(cls):
    #    cls.board = Board.Board()
    #    cls.board.tiles = np.zeros_like(cls.board.tiles)
        #self.board = Board.Board()
        #self.board.tiles = np.zeros_like(board.tiles)
    
    # テスト前処理
    def setUp(self):
        self.board = Board.Board()
        self.board.tiles = np.zeros_like(self.board.tiles)
        self.copiedTiles = np.copy(self.board.tiles)

    ###################
    #          上移動のテスト #
    ###################
    # 1マス動く場合
    def test_keyUp_1(self):
        self.board.tiles[0,0] = 2
        self.board.tiles[1,1] = 2
        self.board.keyUp()

        self.copiedTiles[0,0] = 2
        self.copiedTiles[0,1] = 2

        self.assertTrue((self.copiedTiles == self.board.tiles).all())

    # 1マスも動かない
    def test_keyUp_2(self):
        self.board.tiles[0,0] = 2
        self.board.tiles[0,1] = 2
        self.board.keyUp()

        self.copiedTiles[0,0] = 2
        self.copiedTiles[0,1] = 2

        self.assertTrue((self.copiedTiles == self.board.tiles).all())

    # 縦に同じタイル(2)が2枚並ぶ
    def test_keyUp_3(self):
        self.board.tiles[0,0] = 2
        self.board.tiles[1,0] = 2
        self.board.keyUp()

        self.copiedTiles[0,0] = 4

        self.assertTrue((self.copiedTiles == self.board.tiles).all())

    # 縦に同じタイル(2)が3枚並ぶ
    def test_keyUp_4(self):
        self.board.tiles[0,0] = 2
        self.board.tiles[1,0] = 2
        self.board.tiles[2,0] = 2
        self.board.keyUp()

        self.copiedTiles[0,0] = 4
        self.copiedTiles[1,0] = 2

        self.assertTrue((self.copiedTiles == self.board.tiles).all())

                
    # 縦に同じタイル(2)が4枚並ぶ
    def test_keyUp_5(self):
        self.board.tiles[0,0] = 2
        self.board.tiles[1,0] = 2
        self.board.tiles[2,0] = 2
        self.board.tiles[3,0] = 2
        self.board.keyUp()

        self.copiedTiles[0,0] = 4
        self.copiedTiles[1,0] = 4

        self.assertTrue((self.copiedTiles == self.board.tiles).all())

    # 縦に(2,2,4)と並ぶ
    def test_keyUp_6(self):
        self.board.tiles[0,0] = 2
        self.board.tiles[1,0] = 2
        self.board.tiles[2,0] = 4
        self.board.keyUp()

        self.copiedTiles[0,0] = 4
        self.copiedTiles[1,0] = 4

        self.assertTrue((self.copiedTiles == self.board.tiles).all())

    # 縦に(4,2,2)と並ぶ
    def test_keyUp_7(self):
        self.board.tiles[0,0] = 4
        self.board.tiles[1,0] = 2
        self.board.tiles[2,0] = 2
        self.board.keyUp()

        self.copiedTiles[0,0] = 4
        self.copiedTiles[1,0] = 4

        self.assertTrue((self.copiedTiles == self.board.tiles).all())

     #
    def test_keyUp_8(self):
        self.board.tiles[0,0] = 2
        self.board.tiles[2,0] = 2
        self.board.tiles[3,0] = 4
        self.board.tiles[0,1] = 4
        self.board.tiles[1,1] = 4
        self.board.keyUp()

        self.copiedTiles[0,0] = 4
        self.copiedTiles[1,0] = 4
        self.copiedTiles[0,1] = 8

        self.assertTrue((self.copiedTiles == self.board.tiles).all())

     # 縦に(4,4,2,2)と並ぶ
    def test_keyUp_9(self):
        self.board.tiles[0,0] = 4
        self.board.tiles[1,0] = 4
        self.board.tiles[2,0] = 2
        self.board.tiles[3,0] = 2
        self.board.keyUp()

        self.copiedTiles[0,0] = 8
        self.copiedTiles[1,0] = 4

        self.assertTrue((self.copiedTiles == self.board.tiles).all())

         # 縦に(4,2,2,2)と並ぶ
    def test_keyUp_10(self):
        self.board.tiles[0,0] = 4
        self.board.tiles[1,0] = 2
        self.board.tiles[2,0] = 2
        self.board.tiles[3,0] = 2
        self.board.keyUp()

        self.copiedTiles[0,0] = 4
        self.copiedTiles[1,0] = 4
        self.copiedTiles[2,0] = 2

        self.assertTrue((self.copiedTiles == self.board.tiles).all())

    ###################
    #          下移動のテスト #
    ###################
      # 端までタイルに衝突せずに移動する
    def test_keyDown_1(self):
        self.board.tiles[0,0] = 2
        self.board.tiles[1,1] = 2
        self.board.keyDown()

        self.copiedTiles[3,0] = 2
        self.copiedTiles[3,1] = 2

        self.assertTrue((self.copiedTiles == self.board.tiles).all())

    # 1マスも動かない
    def test_keyDown_2(self):
        self.board.tiles[3,0] = 2
        self.board.tiles[3,1] = 2
        self.board.keyDown()

        self.copiedTiles[3,0] = 2
        self.copiedTiles[3,1] = 2

        self.assertTrue((self.copiedTiles == self.board.tiles).all())

    # 縦に同じタイル(2)が2枚並ぶ
    def test_keyDown_3(self):
        self.board.tiles[0,0] = 2
        self.board.tiles[1,0] = 2
        self.board.keyDown()

        self.copiedTiles[3,0] = 4

        self.assertTrue((self.copiedTiles == self.board.tiles).all())

    # 縦に同じタイル(2)が3枚並ぶ
    def test_keyDown_4(self):
        self.board.tiles[0,0] = 2
        self.board.tiles[1,0] = 2
        self.board.tiles[2,0] = 2
        self.board.keyDown()

        self.copiedTiles[2,0] = 2
        self.copiedTiles[3,0] = 4

        self.assertTrue((self.copiedTiles == self.board.tiles).all())

                
    # 縦に同じタイル(2)が4枚並ぶ
    def test_keyDown_5(self):
        self.board.tiles[0,0] = 2
        self.board.tiles[1,0] = 2
        self.board.tiles[2,0] = 2
        self.board.tiles[3,0] = 2
        self.board.keyDown()

        self.copiedTiles[2,0] = 4
        self.copiedTiles[3,0] = 4

        self.assertTrue((self.copiedTiles == self.board.tiles).all())

    # 縦に(2,2,4)と並ぶ
    def test_keyDown_6(self):
        self.board.tiles[0,0] = 2
        self.board.tiles[1,0] = 2
        self.board.tiles[2,0] = 4
        self.board.keyDown()

        self.copiedTiles[2,0] = 4
        self.copiedTiles[3,0] = 4

        self.assertTrue((self.copiedTiles == self.board.tiles).all())

    # 縦に(4,2,2)と並ぶ
    def test_keyDown_7(self):
        self.board.tiles[0,0] = 4
        self.board.tiles[1,0] = 2
        self.board.tiles[2,0] = 2
        self.board.keyDown()

        self.copiedTiles[2,0] = 4
        self.copiedTiles[3,0] = 4

        self.assertTrue((self.copiedTiles == self.board.tiles).all())

     # その他の例外
    def test_keyDown_8(self):
        self.board.tiles[0,0] = 2
        self.board.tiles[2,0] = 2
        self.board.tiles[3,0] = 4
        self.board.tiles[0,1] = 4
        self.board.tiles[1,1] = 4
        self.board.keyDown()

        self.copiedTiles[2,0] = 4
        self.copiedTiles[3,0] = 4
        self.copiedTiles[3,1] = 8

        self.assertTrue((self.copiedTiles == self.board.tiles).all())

     # 縦に(4,4,2,2)と並ぶ
    def test_keyDown_9(self):
        self.board.tiles[0,0] = 4
        self.board.tiles[1,0] = 4
        self.board.tiles[2,0] = 2
        self.board.tiles[3,0] = 2
        self.board.keyDown()

        self.copiedTiles[2,0] = 8
        self.copiedTiles[3,0] = 4

        self.assertTrue((self.copiedTiles == self.board.tiles).all())

     # 縦に(4,2,2,2)と並ぶ
    def test_keyDown_10(self):
        self.board.tiles[0,0] = 4
        self.board.tiles[1,0] = 2
        self.board.tiles[2,0] = 2
        self.board.tiles[3,0] = 2
        self.board.keyDown()

        self.copiedTiles[1,0] = 4
        self.copiedTiles[2,0] = 2
        self.copiedTiles[3,0] = 4

        self.assertTrue((self.copiedTiles == self.board.tiles).all())


    ###################
    #          左移動のテスト #
    ###################
    # 1マス動く場合
    def test_keyLeft_1(self):
        self.board.tiles[0,0] = 2
        self.board.tiles[1,1] = 2
        self.board.keyLeft()

        self.copiedTiles[0,0] = 2
        self.copiedTiles[1,0] = 2

        self.assertTrue((self.copiedTiles == self.board.tiles).all())

    # 1マスも動かない
    def test_keyLeft_2(self):
        self.board.tiles[0,0] = 2
        self.board.tiles[1,0] = 2
        self.board.keyLeft()

        self.copiedTiles[0,0] = 2
        self.copiedTiles[1,0] = 2

        self.assertTrue((self.copiedTiles == self.board.tiles).all())

    # 横に同じタイル(2)が2枚並ぶ
    def test_keyLeft_3(self):
        self.board.tiles[0,0] = 2
        self.board.tiles[0,1] = 2
        self.board.keyLeft()

        self.copiedTiles[0,0] = 4

        self.assertTrue((self.copiedTiles == self.board.tiles).all())

    # 横に同じタイル(2)が3枚並ぶ
    def test_keyLeft_4(self):
        self.board.tiles[0,0] = 2
        self.board.tiles[0,1] = 2
        self.board.tiles[0,2] = 2
        self.board.keyLeft()

        self.copiedTiles[0,0] = 4
        self.copiedTiles[0,1] = 2

        self.assertTrue((self.copiedTiles == self.board.tiles).all())

                
    # 横に同じタイル(2)が4枚並ぶ
    def test_keyLeft_5(self):
        self.board.tiles[0,0] = 2
        self.board.tiles[0,1] = 2
        self.board.tiles[0,2] = 2
        self.board.tiles[0,3] = 2
        self.board.keyLeft()

        self.copiedTiles[0,0] = 4
        self.copiedTiles[0,1] = 4

        self.assertTrue((self.copiedTiles == self.board.tiles).all())

    # 横に(2,2,4)と並ぶ
    def test_keyLeft_6(self):
        self.board.tiles[0,0] = 2
        self.board.tiles[0,1] = 2
        self.board.tiles[0,2] = 4
        self.board.keyLeft()

        self.copiedTiles[0,0] = 4
        self.copiedTiles[0,1] = 4

        self.assertTrue((self.copiedTiles == self.board.tiles).all())

    # 横に(4,2,2)と並ぶ
    def test_keyLeft_7(self):
        self.board.tiles[0,0] = 4
        self.board.tiles[0,1] = 2
        self.board.tiles[0,2] = 2
        self.board.keyLeft()

        self.copiedTiles[0,0] = 4
        self.copiedTiles[0,1] = 4

        self.assertTrue((self.copiedTiles == self.board.tiles).all())

     # その他例外ケース
    def test_keyLeft_8(self):
        self.board.tiles[0,0] = 2
        self.board.tiles[0,2] = 2
        self.board.tiles[0,3] = 4
        self.board.tiles[1,0] = 4
        self.board.tiles[1,1] = 4
        self.board.keyLeft()

        self.copiedTiles[0,0] = 4
        self.copiedTiles[0,1] = 4
        self.copiedTiles[1,0] = 8

        self.assertTrue((self.copiedTiles == self.board.tiles).all())

     # 横に(4,4,2,2)と並ぶ
    def test_keyLeft_9(self):
        self.board.tiles[0,0] = 4
        self.board.tiles[0,1] = 4
        self.board.tiles[0,2] = 2
        self.board.tiles[0,3] = 2
        self.board.keyLeft()

        self.copiedTiles[0,0] = 8
        self.copiedTiles[0,1] = 4

        self.assertTrue((self.copiedTiles == self.board.tiles).all())

         # 横に(4,2,2,2)と並ぶ
    def test_keyLeft_10(self):
        self.board.tiles[0,0] = 4
        self.board.tiles[0,1] = 2
        self.board.tiles[0,2] = 2
        self.board.tiles[0,3] = 2
        self.board.keyLeft()

        self.copiedTiles[0,0] = 4
        self.copiedTiles[0,1] = 4
        self.copiedTiles[0,2] = 2

        self.assertTrue((self.copiedTiles == self.board.tiles).all())


    ###################
    #          右移動のテスト             #
    ###################
    # 1マス動く場合
    def test_keyRight_1(self):
        self.board.tiles[0,0] = 2
        self.board.tiles[1,1] = 2
        self.board.keyRight()

        self.copiedTiles[0,3] = 2
        self.copiedTiles[1,3] = 2

        self.assertTrue((self.copiedTiles == self.board.tiles).all())

    # 1マスも動かない
    def test_keyRight_2(self):
        self.board.tiles[0,0] = 2
        self.board.tiles[1,0] = 2
        self.board.keyRight()

        self.copiedTiles[0,3] = 2
        self.copiedTiles[1,3] = 2

        self.assertTrue((self.copiedTiles == self.board.tiles).all())

    # 横に同じタイル(2)が2枚並ぶ
    def test_keyRight_3(self):
        self.board.tiles[0,0] = 2
        self.board.tiles[0,1] = 2
        self.board.keyRight()

        self.copiedTiles[0,3] = 4

        self.assertTrue((self.copiedTiles == self.board.tiles).all())

    # 横に同じタイル(2)が3枚並ぶ
    def test_keyRight_4(self):
        self.board.tiles[0,0] = 2
        self.board.tiles[0,1] = 2
        self.board.tiles[0,2] = 2
        self.board.keyRight()

        self.copiedTiles[0,2] = 2
        self.copiedTiles[0,3] = 4

        self.assertTrue((self.copiedTiles == self.board.tiles).all())

                
    # 横に同じタイル(2)が4枚並ぶ
    def test_keyRight_5(self):
        self.board.tiles[0,0] = 2
        self.board.tiles[0,1] = 2
        self.board.tiles[0,2] = 2
        self.board.tiles[0,3] = 2
        self.board.keyRight()

        self.copiedTiles[0,2] = 4
        self.copiedTiles[0,3] = 4

        self.assertTrue((self.copiedTiles == self.board.tiles).all())

    # 横に(2,2,4)と並ぶ
    def test_keyRight_6(self):
        self.board.tiles[0,0] = 2
        self.board.tiles[0,1] = 2
        self.board.tiles[0,2] = 4
        self.board.keyRight()

        self.copiedTiles[0,2] = 4
        self.copiedTiles[0,3] = 4

        self.assertTrue((self.copiedTiles == self.board.tiles).all())

    # 横に(4,2,2)と並ぶ
    def test_keyRight_7(self):
        self.board.tiles[0,0] = 4
        self.board.tiles[0,1] = 2
        self.board.tiles[0,2] = 2
        self.board.keyRight()

        self.copiedTiles[0,2] = 4
        self.copiedTiles[0,3] = 4

        self.assertTrue((self.copiedTiles == self.board.tiles).all())

     # その他例外ケース
    def test_keyRight_8(self):
        self.board.tiles[0,0] = 2
        self.board.tiles[0,2] = 2
        self.board.tiles[0,3] = 4
        self.board.tiles[1,0] = 4
        self.board.tiles[1,1] = 4
        self.board.keyRight()

        self.copiedTiles[0,2] = 4
        self.copiedTiles[0,3] = 4
        self.copiedTiles[1,3] = 8

        self.assertTrue((self.copiedTiles == self.board.tiles).all())

     # 横に(4,4,2,2)と並ぶ
    def test_keyRight_9(self):
        self.board.tiles[0,0] = 4
        self.board.tiles[0,1] = 4
        self.board.tiles[0,2] = 2
        self.board.tiles[0,3] = 2
        self.board.keyRight()

        self.copiedTiles[0,2] = 8
        self.copiedTiles[0,3] = 4

        self.assertTrue((self.copiedTiles == self.board.tiles).all())

         # 横に(4,2,2,2)と並ぶ
    def test_keyRight_10(self):
        self.board.tiles[0,0] = 4
        self.board.tiles[0,1] = 2
        self.board.tiles[0,2] = 2
        self.board.tiles[0,3] = 2
        self.board.keyRight()

        self.copiedTiles[0,1] = 4
        self.copiedTiles[0,2] = 2
        self.copiedTiles[0,3] = 4

        self.assertTrue((self.copiedTiles == self.board.tiles).all())
    


if __name__ == "__main__":
    unittest.main()