import pygame
from pygame.locals import K_LEFT, K_RIGHT, K_UP, K_DOWN, Rect

# Ｃ－１７最初）ヘビクラス
class Snake:
    # Ｃ－１８）ヘビの色
    SNAKE_COLOUR = (0, 255, 255)
    # Ｃ－１９）コンストラクタ
    def __init__(self, body):
        # Ｃ－２０）ヘビの体を表すインスタンス変数
        # 「(x, y)の位置を表すタプル」のリスト
        self.body = body
    
    # Ｃ－２１）ヘビ描画処理
    def draw(self, surface,width, height):
        # Ｃ－２１）ヘビの体の数だけ繰り返す
        for pos in self.body:
            # Ｃ－２２mainへ）体の１マスごとに、四角を描画する
            pygame.draw.rect(surface, Snake.SNAKE_COLOUR,
                             Rect(pos[0] * width, pos[1] * height,width,height))
            
    # Ｆ－６４foodsから）引数にエサインスタンス、横マス数、縦マス数を追加
    # Ｄ－２９最初）ヘビ移動処理
    def move(self, key, foods, col_cnt, row_cnt):
    
        # Ｄ－３０）ヘビの先頭位置を取得[x, y]
        x, y = self.body[0]
        # Ｄ－３１）押されているキーに対応して、先頭の位置を移動させる
        if key == K_LEFT:
            x -= 1
        elif key == K_RIGHT:
            x += 1
        elif key == K_UP:
            y -= 1
        elif key == K_DOWN:
            y += 1          
        # Ｄ－３２）移動後の位置を新しい頭の位置にする
        new_head = (x, y)
        # Ｇ－７０最初）ゲームオーバー判定フラグ（初期値はFalse）
        is_gameover =False
        # Ｇ－７１）ヘビの先頭がヘビの体と重なったらゲームオーバー
        if new_head in self.body:
            is_gameover = True
        # Ｇ－７２）ヘビの先頭が画面外に行ってしまったらゲームオーバー
        # ※Python では、下記のような書き方で複数の比較判定を同時に行える
        if not ((0 <= new_head[0]< col_cnt)and (0 <= new_head[1]< row_cnt)):
            is_gameover = True

        # Ｄ－３３）ヘビの体に、移動後の先頭位置を挿入する
        self.body.insert(0,new_head)
        # Ｆ－６５）ヘビの先頭がエサの位置だったら
        if new_head in foods.food_list: 
            # Ｆ－６６）エサの位置を動かす
            foods.move(self, new_head, col_cnt, row_cnt)
            # Ｆ－６７）デバッグ用に出力
            print('GET Food!')
        # Ｆ－６８mainへ）エサの位置でない場合に最後を削除するようにする
        else:
            # Ｄ－３４mainへ）ヘビの体の最後を削除する
            self.body.pop()
        
        # Ｇ－７３mainへ）ゲームオーバー判定を戻り値にする
        return is_gameover
