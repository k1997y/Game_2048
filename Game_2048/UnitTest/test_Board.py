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

if __name__ == "__main__":
    unittest.main()