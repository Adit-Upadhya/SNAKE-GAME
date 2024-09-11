import random
import pygame
from pygame.locals import Rect

# Ｅ－４２最初）エサクラス
# ※エサ全部で１つのインスタンスとして使用します
class Foods:
    # Ｅ－４３）エサの色
    FOOD_COLOUR =(0, 255,0)
    # Ｅ－４４）コンストラクタ
    def __init__(self):
        # Ｅ－４５）エサを空のリストとして用意
        self.food_list = []

    # Ｅ－４６）画面上にエサを配置
    def add(self, snake, col_cnt, row_cnt):
        # Ｅ－４７）エサを配置できるまでずっと繰り返す
        while True:
            # Ｅ－４８）エサの位置をランダムに決定する
            col = random.randint(0, col_cnt - 1)
            row = random.randint(0, row_cnt - 1)
            pos =(col, row)
            # Ｅ－４９）エサが、すでにエサのある位置ならやり直し
            if pos in self.food_list:
                continue
            # Ｅ－５０）エサが、ヘビの体のある位置ならやり直し
            if pos in snake.body:
                continue
            # Ｅ－５１）空の位置ならエサを配置して、繰り返しを終了する
            self.food_list.append(pos)
            break

    # Ｅ－５２）エサ描画処理
    def draw(self, surface, width, height):
        # Ｅ－５３mainへ）エサの数だけ、丸を描画する
        for  pos in self.food_list:
            pygame.draw.ellipse(surface, Foods.FOOD_COLOUR,
                                Rect(pos[0] * width, pos[1] * height, width, height))
        
    # Ｆ－６０最初）画面上のエサを別の場所に移動
    def move(self, snake, pos, col_cnt, row_cnt):
        # Ｆ－６１）画面上にエサを配置
        self.add(snake, col_cnt, row_cnt)
        # Ｆ－６２）引数の位置のエサの、配列の添字（何番目か）を取得
        idx = self.food_list.index(pos)
        # Ｆ－６３snakeへ）引数のエサをリストから取り除く
        del self.food_list[idx]
