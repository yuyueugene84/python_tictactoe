def print_board(board):
    print("_____")
    print("|{}|{}|{}|".format(board[0], board[1], board[2]))
    print("_____")
    print("|{}|{}|{}|".format(board[3], board[4], board[5]))
    print("_____")
    print("|{}|{}|{}|".format(board[6], board[7], board[8]))
    print("_____")

def board_not_full(board):
    return (board.count("O") + board.count("X")) != 9

# 代表九宮格的一維陣列
board = list(range(1,10))
# 玩家選項
user_choices = ["O", "X"]

print("歡迎光臨井字游戲!!!")

user_choice = input("請選擇 'O' 或 'X'")

print("你選擇了： {}".format(user_choice))

while not board_full():
    user_move = int(input("請選擇你的下一步："))
