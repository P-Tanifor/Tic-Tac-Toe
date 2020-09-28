board = [[0 for i in range(3)] for j in range(3)]
user_input = "_________"

board[0][0] = user_input[0]
board[0][1] = user_input[1]
board[0][2] = user_input[2]
board[1][0] = user_input[3]
board[1][1] = user_input[4]
board[1][2] = user_input[5]
board[2][0] = user_input[6]
board[2][1] = user_input[7]
board[2][2] = user_input[8]

print("-" * 9)
for row in board:
    print("|", *row, "|")
print("-" * 9)

x_count, o_count = 0, 0
x_win_counter = 0
o_win_counter = 0

for row in board:
    x_count += row.count("X")
    o_count += row.count("O")


while True:

    if x_count - o_count > 1 or o_count - x_count > 1:
        print("impossible")
    else:
        for row in board:
            if row[:] == ["X", "X", "X"]:
                x_win_counter += 1
                break
        for row in board:
            if row[:] == ["O", "O", "O"]:
                o_win_counter += 1
                break
        for i in range(3):
            for j in range(3):
                if board[j][i] == "X":
                    continue
                else:
                    break

            else:
                x_win_counter += 1
                break
        for i in range(3):
            for j in range(3):
                if board[j][i] == "O":
                    continue
                else:
                    break
            else:
                o_win_counter += 1
                break
        if (board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X") or \
                (board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X"):
            x_win_counter += 1
        elif (board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O") or \
                (board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O"):
            o_win_counter += 1

        if x_win_counter >= 1 and o_win_counter >= 1:
            print("Impossible")
        elif x_win_counter >= 1 and o_win_counter == 0:
            print("X wins")
            break
        elif o_win_counter >= 1 and x_win_counter == 0:
            print("O wins")
            break
        elif x_count + o_count == 9 and x_win_counter == 0 and o_win_counter == 0:
            print("Draw")
            break
        elif x_count + o_count != 9 and x_win_counter == 0 and o_win_counter == 0:
            print("Game not finished")

    user_coordinate = input("Enter the coordinates: ")
    row, col = user_coordinate.split()
    try:
        i = 3 - int(col)
        j = int(row) - 1
        index = (i * 3) + j
        if int(row) < 1 or int(row) > 3 or int(col) < 1 or int(col) > 3:
            print("Coordinates should be from 1 to 3!")
            continue
        else:
            if board[i][j] == "_":
                if x_count - o_count == 1:
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
            else:
                print("This cell is occupied! Choose another one!")
                continue
    except:
        print("You should enter numbers!")
        continue

    print("-" * 9)
    for row in board:
        print("|", *row, "|")
    print("-" * 9)
    continue
