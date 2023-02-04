import random
import sys

kanji_board = ['土', '士', '万', '方', '低', '抵', '作', '昨', '州', '川', '千', '干', '日', '曰', '未', '末', '毛', '手', '人', '入', '力', '刀', '石', '右', '牛', '午', '友', '反', '名', '各', '木', '本', '白', '自', '王', '玉', '大', '犬', '水', '氷', '考', '老', '比', '北', '知', '和', '従', '徒', '験', '検', '感', '惑', '拾', '捨'] * 2
random.shuffle(kanji_board)

board = [['' for x in range(15)] for y in range(15)]
for i in range(15):
    for j in range(15):
        if len(kanji_board) == 0:
            break
        board[i][j] = kanji_board.pop()

japanese_num = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '十一', '十二', '十三', '十四', '十五']
japanese_alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']

def display_board(board):
    print(' ', end='')
    for i in japanese_alphabets:
        print(f'  {i} ', end='')
    print('\n' + '+---' * 15 + '+')
    for i in range(15):
        print(japanese_num[i], end='|')
        for j in range(15):
            print(f' {board[i][j]} ', end='|')
        print('\n' + '+---' * 15 + '+')

while True:
    display_board(board)
    row, col = input('Enter the row and column: ').split()
    row = int(row) - 1
    col = japanese_alphabets.index(col)
    if board[row][col] == board[row][col]:
        board[row][col] = ''
    else:
        print('Wrong selection! Try again.')
    if not kanji_board:
        print('All kanjis have been found!')
        sys.exit()
