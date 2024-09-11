import sys
import pygame
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN
# Ｃ－２３）ヘビクラスのインポート
from snake import Snake
# Ｅ－５４）エサクラスのインポート
from foods import Foods

BLOCK_ROWS = 20     # マスの縦の数
BLOCK_COLS = 20     # マスの横の数
BLOCK_HEIGHT = 30   # マスの高さ
BLOCK_WIDTH = 30    # マスの幅
WINDOW_HEIGHT = BLOCK_ROWS * BLOCK_HEIGHT   # 画面の高さ
WINDOW_WIDTH = BLOCK_COLS * BLOCK_WIDTH     # 画面の幅

FOOD_COUNT = 10                             # エサの数
LINE_COLOR = (64, 64, 64)                   # 区切り線の色
MSG_COLOR = (255, 0, 0)                     # メッセージの色

# Ａ－１最初）Pygameの初期化
pygame.init()
# Ａ－２）ウィンドウの設定
surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# Ａ－３）クロックの作成
clock = pygame.time.Clock()
# Ａ－４）ウィンドウ名の設定
pygame.display.set_caption('SNAKE GAME')
# Ｇ－７４）フォントを作成
msg_font = pygame.font.SysFont('Arial', 100)

# Ｇ－７５）引数にメッセージとその位置を追加
# Ｅ－５５）引数に foods インスタンスを追加
# Ｃ－２４）引数に snake インスタンスを追加
# Ｂ－１１最初）画面の描画処理関数
def paint(snake, foods, disp_msg, disp_msg_pos):

    # Ｂ－１２）画面を黒で塗りつぶす
    surface.fill((0,0,0))
    # Ｃ－２５）ヘビ描画処理
    snake.draw(surface, BLOCK_WIDTH, BLOCK_HEIGHT)
    # Ｅ－５６）エサ描画処理
    foods.draw(surface, BLOCK_WIDTH, BLOCK_HEIGHT)
    # Ｂ－１３）縦の線を引く
    for index in range(BLOCK_COLS):
        pygame.draw.line(surface,LINE_COLOR,
                         (index * BLOCK_WIDTH, 0),
                         (index * BLOCK_WIDTH, WINDOW_HEIGHT))
    # Ｂ－１４）横の線を引く
    for index in range(BLOCK_ROWS):
        pygame.draw.line(surface,LINE_COLOR,
                         (0, index * BLOCK_HEIGHT),
                        (WINDOW_WIDTH, index * BLOCK_HEIGHT))    
    # Ｇ－７６）メッセージが空でない場合
    if disp_msg != '':
        # Ｇ－７７）メッセージを表示する
        msg = msg_font.render(disp_msg, True, MSG_COLOR)
        surface.blit(msg, disp_msg_pos)
    # Ｂ－１５）画面を更新する
    pygame.display.update()

# Ａ－５）メイン関数
def main():
    # Ｄ－３５snakeから）初期状態は、下キーが押されているものとする
    key = K_DOWN
    # Ｄ－３６）ゲームオーバーフラグ
    is_gameover = False
    # Ｇ－７８）画面に表示するメッセージとその位置
    disp_msg = ''
    disp_msg_pos = (0, 0)
    # Ｃ－２６）ヘビの初期位置
    # （※仮に長さ３で作成、隣り合った位置にしてください）
    f_body = [(10, 10), (10, 9), (10,8)]
    # Ｃ－２７）ヘビクラスのインスタンスを作成
    snake = Snake(f_body)
    # Ｅ－５７）エサクラスのインスタンスを作成
    foods = Foods()
    # Ｅ－５８）エサの数だけ、エサを初期配置する
    for fd in range(FOOD_COUNT):
        foods.add(snake, BLOCK_COLS, BLOCK_ROWS)
    # Ａ－６）メイン繰り返し処理
    while True:
        # Ａ－７）イベント取得
        for event in pygame.event.get():
            # Ａ－８）終了イベントの場合、ゲームを終了する
            if event.type == QUIT:
                pygame.quit()
                sys.exit()            
            # Ｄ－３７）キーが押された場合、
            elif event.type == KEYDOWN:
                # Ｄ－３８）そのキーが上下左右だったら保持する
                if event.key in [K_LEFT, K_RIGHT, K_UP, K_DOWN]:
                    key = event.key

        # Ｄ－３９）ゲームオーバーの場合（一旦処理はpassのみ）
        if is_gameover:
            pass
            # Ｇ－７９）メッセージを設定する
            disp_msg = 'Game Over'
            disp_msg_pos = (85, 120)
            
        # Ｄ－４０）ゲームオーバーでない場合
        else:
            # Ｇ－８０）戻り値の判定を追加
            # Ｆ－６９最後）引数を追加
            # Ｄ－４１最後）ヘビを移動（キーを引数にする）
             is_gameover = snake.move(key, foods, BLOCK_COLS, BLOCK_ROWS)
            
            
        
        # Ｇ－８１最後）引数の追加
        # Ｅ－５９最後）引数に foods インスタンスを追加
        # Ｃ－２８最後）引数に snake インスタンスを追加
        # Ｂ－１６最後）画面の描画処理
        paint(snake, foods, disp_msg, disp_msg_pos)
        # Ａ－９）クロック（時間間隔）の設定
        clock.tick(10)

# Ａ－１０最後）メインモジュール判定
if __name__ == '__main__':
    main()
