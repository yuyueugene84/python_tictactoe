def print_board(board):
    print("_____")
    print("|{}|{}|{}|".format(board[0], board[1], board[2]))
    print("_____")
    print("|{}|{}|{}|".format(board[3], board[4], board[5]))
    print("_____")
    print("|{}|{}|{}|".format(board[6], board[7], board[8]))
    print("_____")

def board_full(board):
    return (board.count("O") + board.count("X")) != 9

def user_move(board, user_choice):
    # 截取玩家選擇的格子，更新 board 這個 list 的資料
    # 先確保玩家的選項是在 1 到 9 之間的數字
    while True:
        user_move = int(input("請選擇你的下一步："))
        if user_move in range(1, 10):
            # 確保玩家選擇的儲存格是空的
            if board[int(user_move)-1] in list(range(1,10)):
                # 若該儲存格是空的，就將該儲存格填上使用者的選項
                board[int(user_move)-1] = user_choice
                # 跳出 while loop
                break
            else:
                print("格子已被佔領！")
        else:
            print("請確認你輸入的數字是在 1 到 9 之間！")
    # 回傳九宮格陣列
    return board

def check_win(board, choice):
    return ((board[0] == choice and board[1] == choice and board[2] == choice) or
           (board[3] == choice and board[4] == choice and board[5] == choice) or
           (board[6] == choice and board[7] == choice and board[8] == choice) or
           (board[0] == choice and board[3] == choice and board[6] == choice) or
           (board[1] == choice and board[4] == choice and board[7] == choice) or
           (board[2] == choice and board[5] == choice and board[8] == choice) or
           (board[0] == choice and board[4] == choice and board[8] == choice) or
           (board[2] == choice and board[4] == choice and board[6] == choice))

def determine_winner(board, user_choice):
    # 判斷目前的九宮格是否其中一人勝利或是平手
    if check_win(board, user_choice):
        print('恭喜你贏了！')
        return True
    elif check_win(board, computer_choice):
        print('你輸了...')
        return True
    elif board_full(board) == True:
        print('平手...')
        return True
    else:
        return False


# 代表九宮格的一維陣列
board = list(range(1,10))
# 玩家選項
user_choices = ["O", "X"]

print("歡迎光臨井字游戲!!!")
# 讓使用者選擇棋子
while True:
    user_choice = input("請選擇 'O' 或 'X'")
    if user_choice in ["O", "X"]：
        user_choices.remove(user_choice)
        computer_choice = user_choice.pop()
        break

print("你選擇了： {} 做棋子".format(user_choice))
# 九宮格還沒被佔滿，就繼續執行游戲
while not board_full(board):
    # 讓使用者走下一步，回傳九宮格的狀態
    board = user_move(board, user_choice)

    if determine_winner(board, user_choice)
        break

