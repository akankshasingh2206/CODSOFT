import random

#BOARD 
board = [" " for _ in range(9)]
move_history = []

#DISPLAY BOARD
def print_board(board):
    print("\n")
    for i in range(0, 9, 3):
        print(" " + board[i] + " | " + board[i+1] + " | " + board[i+2])
        if i < 6:
            print("---+---+---")
    print("\n")

#WIN CHECK
def check_winner(board, player):
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for pos in win_positions:
        if all(board[i] == player for i in pos):
            return True
    return False

#DRAW CHECK
def is_draw(board):
    return " " not in board

#AVAILABLE MOVES
def available_moves(board):
    return [i for i in range(9) if board[i] == " "]

#MINIMAX
def minimax(board, is_maximizing, ai, human):

    if check_winner(board, ai):
        return 1
    if check_winner(board, human):
        return -1
    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = -1000
        for move in available_moves(board):
            board[move] = ai
            score = minimax(board, False, ai, human)
            board[move] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = 1000
        for move in available_moves(board):
            board[move] = human
            score = minimax(board, True, ai, human)
            board[move] = " "
            best_score = min(score, best_score)
        return best_score
#BEST MOVE
def best_move(board, ai, human):
    best_score = -1000
    move = None

    for i in available_moves(board):
        board[i] = ai
        score = minimax(board, False, ai, human)
        board[i] = " "

        if score > best_score:
            best_score = score
            move = i

    return move

#EASY MODE
def easy_move(board):
    return random.choice(available_moves(board))

#GAME START
print(" Welcome to Tic-Tac-Toe AI")

player_name = input("Enter your name: ")

choice = input("Choose X or O: ").upper()

if choice == "O":
    human = "O"
    ai = "X"
else:
    human = "X"
    ai = "O"

level = input("Choose difficulty (easy/hard): ").lower()

player_score = 0
ai_score = 0

#GAME LOOP
while True:

    board = [" " for _ in range(9)]
    move_history = []

    print("\nNew Game Started!\n")

    while True:

        print_board(board)

        #HUMAN MOVE
        try:
            move = int(input(f"{player_name}, enter position (0-8): "))
        except:
            print("Invalid input!")
            continue

        if move < 0 or move > 8 or board[move] != " ":
            print("Invalid move!")
            continue

        board[move] = human
        move_history.append((player_name, move))

        if check_winner(board, human):
            print_board(board)
            print("🎉", player_name, "Wins!")
            player_score += 1
            break

        if is_draw(board):
            print_board(board)
            print("Draw!")
            break

        #AI MOVE
        print("AI is thinking... 🤖")

        if level == "easy":
            ai_move = easy_move(board)
        else:
            ai_move = best_move(board, ai, human)

        board[ai_move] = ai
        move_history.append(("AI", ai_move))

        print("AI chooses position:", ai_move)

        if check_winner(board, ai):
            print_board(board)
            print("🤖 AI Wins!")
            ai_score += 1
            break

        if is_draw(board):
            print_board(board)
            print("Draw!")
            break

    #GAME STATS
    print("\nSCOREBOARD")
    print(player_name, ":", player_score)
    print("AI :", ai_score)

    print("\n📜 Move History:", move_history)

    #REPLAY
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break