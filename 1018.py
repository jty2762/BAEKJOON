N,M = map(int, input().split())
global chess_board
chess_board = [input() for _ in range(N)]
tmp = chess_board
min_cnt = 5000

def change_color(i, j):
    if chess_board[i][j] == 'B':
        chess_board[i] = chess_board[i][:j] + 'W' + chess_board[i][j+1:]
    else:
        chess_board[i] = chess_board[i][:j] + 'B' + chess_board[i][j+1:]
    
for i in range(0, N-7):
    for j in range(0, M-8):
        cnt = 0
        chess_board = tmp
        first_point = chess_board[i][j]
        if first_point == 'B':
            for k in range(i, i+8, 2):
                for l in range(j, j+7):
                    if chess_board[k][l] == chess_board[k][l+1]:
                        change_color(k, l+1)
                        cnt += 1
            
            for k in range(i+1, i+8, 2):
                for l in range(j, j+7):
                    if chess_board[k][l] != 'W':
                        change_color(k,l)
                        cnt += 1
                    if chess_board[k][l] == chess_board[k][l+1]:
                        change_color(k, l+1)
                        cnt += 1
        else:
            for k in range(i, i+8, 2):
                for l in range(j, j+7):
                    if chess_board[k][l] == chess_board[k][l+1]:
                        change_color(k, l+1)
                        cnt += 1
            for k in range(i+1, i+8, 2):
                for l in range(j, j+7):
                    if chess_board[k][l] != 'B':
                        change_color(k,l)
                        cnt += 1
                    if chess_board[k][l] == chess_board[k][l+1]:
                        change_color(k, l+1)
                        cnt += 1
            
        min_cnt = min(min_cnt, cnt)
print(chess_board)
print(min_cnt)
