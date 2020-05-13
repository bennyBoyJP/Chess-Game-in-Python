def stalemate(board, turn, rule, path, future, empty, in_check, main_history, rook_history):
    """
    :param board: current board
    :param turn: current turn
    :param rule: import function from c3_RULE
    :param path: import function from c3_PATH
    :param future: import function from c3_FUTR *to test a possible move*
    :param empty: empty space of square
    :param in_check: passes status of current player - in check or not
    :param main_history: from function c3_HIST passes the history of all moves (for special moves)
    :param rook_history: from function c3_HIST passes the history of all rooks (for special moves)
    :return: returns TRUE if player can only move into check
    """

    # ------------------------------------------------------------------------------------------------------------------
    #  creates list *allPieces* of all pieces of current player
    allPieces = []
    if turn == "WHITE":
        for whitePiece in board:
            if board[whitePiece][0] == "w":
                allPieces.append(whitePiece)
    elif turn == "BLACK":
        for blackPiece in board:
            if board[blackPiece][0] == "b":
                allPieces.append(blackPiece)

    # ------------------------------------------------------------------------------------------------------------------
    # helper function to calculate eligibility in all directions from *night*

    def night_eligible(square):
        if abs(ord(square[0]) - ord("A")) >= 2 and abs(int(square[-1]) - 8) >= 1:
            if board[square][0] != board[chr(ord(square[0]) - 2) + str(int(square[-1]) + 1)][0]:
                nightleftup = chr(ord(square[0]) - 2) + str(int(square[-1]) + 1)
            else:
                nightleftup = False
        else:
            nightleftup = False

        if abs(ord(square[0]) - ord("A")) >= 2 and abs(int(square[-1]) - 1) >= 1:
            if board[square][0] != board[chr(ord(square[0]) - 2) + str(int(square[-1]) - 1)][0]:
                nightleftdown = chr(ord(square[0]) - 2) + str(int(square[-1]) - 1)
            else:
                nightleftdown = False
        else:
            nightleftdown = False

        if abs(ord(square[0]) - ord("H")) >= 2 and abs(int(square[-1]) - 8) >= 1:
            if board[square][0] != board[chr(ord(square[0]) + 2) + str(int(square[-1]) + 1)][0]:
                nightrightup = chr(ord(square[0]) + 2) + str(int(square[-1]) + 1)
            else:
                nightrightup = False
        else:
            nightrightup = False

        if abs(ord(square[0]) - ord("H")) >= 2 and abs(int(square[-1]) - 1) >= 1:
            if board[square][0] != board[chr(ord(square[0]) + 2) + str(int(square[-1]) - 1)][0]:
                nightrightdown = chr(ord(square[0]) + 2) + str(int(square[-1]) - 1)
            else:
                nightrightdown = False
        else:
            nightrightdown = False

        if abs(ord(square[0]) - ord("A")) >= 1 and abs(int(square[-1]) - 8) >= 2:
            if board[square][0] != board[chr(ord(square[0]) + 1) + str(int(square[-1]) + 2)][0]:
                nightupleft = chr(ord(square[0]) - 1) + str(int(square[-1]) + 2)
            else:
                nightupleft = False
        else:
            nightupleft = False

        if abs(ord(square[0]) - ord("H")) >= 1 and abs(int(square[-1]) - 8) >= 2:
            if board[square][0] != board[chr(ord(square[0]) - 1) + str(int(square[-1]) + 2)][0]:
                nightupright = chr(ord(square[0]) + 1) + str(int(square[-1]) + 2)
            else:
                nightupright = False
        else:
            nightupright = False

        if abs(ord(square[0]) - ord("A")) >= 1 and abs(int(square[-1]) - 1) >= 2:
            if board[square][0] != board[chr(ord(square[0]) - 1) + str(int(square[-1]) - 2)][0]:
                nightdownleft = chr(ord(square[0]) - 1) + str(int(square[-1]) - 2)
            else:
                nightdownleft = False
        else:
            nightdownleft = False

        if abs(ord(square[0]) - ord("H")) >= 1 and abs(int(square[-1]) - 1) >= 2:
            if board[square][0] != board[chr(ord(square[0]) + 1) + str(int(square[-1]) - 2)][0]:
                nightdownright = chr(ord(square[0]) + 1) + str(int(square[-1]) - 2)
            else:
                nightdownright = False
        else:
            nightdownright = False

        return [square, [nightleftup, nightleftdown, nightrightup, nightrightdown,
                         nightupleft, nightupright, nightdownleft, nightdownright]]

# ------------------------------------------------------------------------------------------------------------------
    # helper function to calculate distances to edge of board in all directions from *queen*
    def piece_eligible(square):

        if board[square][-1] in pieces:
            if abs(ord(square[0]) - ord("A")) > 0 and \
                    board[chr(ord(square[0]) - 1) + square[-1]][0] != board[square][0]:
                left = chr(ord(square[0]) - 1) + square[-1]
            else:
                left = False

            if abs(ord(square[0]) - ord("H")) > 0 and \
                    board[chr(ord(square[0]) + 1) + square[-1]][0] != board[square][0]:
                right = chr(ord(square[0]) + 1) + square[-1]
            else:
                right = False

            if abs(int(square[-1]) - 8) > 0 and \
                    board[square[0] + str(int(square[-1]) + 1)][0] != board[square][0]:
                up = square[0] + str(int(square[-1]) + 1)
            else:
                up = False

            if abs(int(square[-1]) - 1) > 0 and \
                    board[square[0] + str(int(square[-1]) - 1)][0] != board[square][0]:
                down = square[0] + str(int(square[-1]) - 1)
            else:
                down = False

            if abs(ord(square[0]) - ord("A")) > 0 and abs(int(square[-1]) - 8) > 0 and \
                    board[chr(ord(square[0]) - 1) + str(int(square[-1]) + 1)][0] != board[square][0]:
                up_left = chr(ord(square[0]) - 1) + str(int(square[-1]) + 1)
            else:
                up_left = False

            if abs(ord(square[0]) - ord("H")) > 0 and abs(int(square[-1]) - 8) > 0 and \
                    board[chr(ord(square[0]) + 1) + str(int(square[-1]) + 1)][0] != board[square][0]:
                up_right = chr(ord(square[0]) + 1) + str(int(square[-1]) + 1)
            else:
                up_right = False

            if abs(ord(square[0]) - ord("A")) > 0 and abs(int(square[-1]) - 1) > 0 and \
                    board[chr(ord(square[0]) - 1) + str(int(square[-1]) - 1)][0] != board[square][0]:
                down_left = chr(ord(square[0]) - 1) + str(int(square[-1]) - 1)
            else:
                down_left = False

            if abs(ord(square[0]) - ord("H")) > 0 and abs(int(square[-1]) - 1) > 0 and \
                    board[chr(ord(square[0]) + 1) + str(int(square[-1]) - 1)][0] != board[square][0]:
                down_right = chr(ord(square[0]) + 1) + str(int(square[-1]) - 1)
            else:
                down_right = False

            if board[square][-1] == "r":
                up_left, up_right, down_left, down_right = False, False, False, False
            elif board[square][-1] == "b":
                left, right, up, down = False, False, False, False

            return [square, [left, right, up, down, up_left, up_right, down_left, down_right]]

# ------------------------------------------------------------------------------------------------------------------
    # helper function to calculate available move or not in all directions from *pawn*
    def pawn_eligible(square):

        pawn_limits = {int(square[-1]) - 1 >= 1,
                       int(square[-1]) + 1 <= 8}

        left = False
        right = False
        if all(pawn_limits):
            if board[square][0] == "w" and board[square[0] + str(int(square[-1]) + 1)] == empty:
                down = False
                up = square[0] + str(int(square[-1]) + 1)

            elif board[square][0] == "b" and board[square[0] + str(int(square[-1]) - 1)] == empty:
                up = False
                down = square[0] + str(int(square[-1]) - 1)

            else:
                up = False
                down = False
        else:
            up = False
            down = False

        pawn_rival_limits = {chr(ord(square[0]) - 1) >= "A",
                             chr(ord(square[0]) + 1) <= "H",
                             int(square[-1]) - 1 >= 1,
                             int(square[-1]) + 1 <= 8}

        if all(pawn_rival_limits):
            if board[square][0] == "w":
                down_left = False
                down_right = False
                if board[chr(ord(square[0]) - 1) + str(int(square[-1]) + 1)][0] == "b":
                    up_left = chr(ord(square[0]) - 1) + str(int(square[-1]) + 1)
                    up_right = False
                elif board[chr(ord(square[0]) + 1) + str(int(square[-1]) + 1)][0] == "b":
                    up_right = chr(ord(square[0]) + 1) + str(int(square[-1]) + 1)
                    up_left = False
                elif board[chr(ord(square[0]) + 1) + str(int(square[-1]) + 1)][0] == "b" and \
                        board[chr(ord(square[0]) - 1) + str(int(square[-1]) + 1)][0] == "b":
                    up_right = chr(ord(square[0]) + 1) + str(int(square[-1]) + 1)
                    up_left = chr(ord(square[0]) - 1) + str(int(square[-1]) + 1)
                elif board[chr(ord(square[0]) + 1) + str(int(square[-1]) + 1)][0] != "b" and \
                        board[chr(ord(square[0]) - 1) + str(int(square[-1]) + 1)][0] != "b":
                    up_left = False
                    up_right = False
                else:
                    up_left = False
                    up_right = False

            elif board[square][0] == "b":
                up_left = False
                up_right = False
                if board[chr(ord(square[0]) - 1) + str(int(square[-1]) - 1)][0] == "w":
                    down_left = chr(ord(square[0]) - 1) + str(int(square[-1]) - 1)
                    down_right = False
                elif board[chr(ord(square[0]) + 1) + str(int(square[-1]) - 1)][0] == "w":
                    down_right = chr(ord(square[0]) + 1) + str(int(square[-1]) - 1)
                    down_left = False
                elif board[chr(ord(square[0]) + 1) + str(int(square[-1]) - 1)][0] == "w" and \
                        board[chr(ord(square[0]) - 1) + str(int(square[-1]) - 1)][0] == "w":
                    down_right = chr(ord(square[0]) + 1) + str(int(square[-1]) - 1)
                    down_left = chr(ord(square[0]) - 1) + str(int(square[-1]) - 1)
                elif board[chr(ord(square[0]) + 1) + str(int(square[-1]) - 1)][0] != "w" and \
                        board[chr(ord(square[0]) - 1) + str(int(square[-1]) - 1)][0] != "w":
                    down_left = False
                    down_right = False
                else:
                    down_left = False
                    down_right = False
            else:
                up_left = False
                up_right = False
                down_left = False
                down_right = False
        else:
            up_left = False
            up_right = False
            down_left = False
            down_right = False

        return [square, [left, right, up, down, up_left, up_right, down_left, down_right]]

# ------------------------------------------------------------------------------------------------------------------
    #  appends all piece movement lists into 'allPiecesDistance'
    pieces = {"K", "Q", "b", "r"}
    allPiecesEligible = []
    for coordinate in allPieces:
        if board[coordinate][-1] in pieces:
            allPiecesEligible.append(piece_eligible(coordinate))
        elif board[coordinate][-1] == "n":
            allPiecesEligible.append(night_eligible(coordinate))
        elif board[coordinate][-1] == "p":
            allPiecesEligible.append(pawn_eligible(coordinate))

# ------------------------------------------------------------------------------------------------------------------
#     for piece in allPiecesEligible:  # temp for testing
#         print(piece)

    # directions = ['left','right','up','down','upleft','upright','downleft','downright']

    #   iterates through indices (spaces in each direction) of each item in allPiecesDistance
    #   ref: 0 = left, 1 = right, 2 = up, 3 = down, 4 = up_left, 5 = up_right, 6 = down_left, 7 = down_right

    director = range(8)

    for piece in allPiecesEligible:  # iterates through each piece of allPiecesDistance
        for direction in director:  # iterates from (0 - 7)
            if piece[1][direction] is not False:  # skips any item with False
                # print('stalemate: ', end='')
                # testing rule of movement
                if rule(board, piece[0], piece[1][direction], in_check, main_history,
                        rook_history, path, future, turn, empty):
                    # print(f'stalemate: valid rule for: {piece[0]}: ')
                    # print('stalemate: ', end='')
                    if path(board, piece[0], piece[1][direction], in_check, empty):  # testing path of movement
                        # print(f'stalemate: path for: {piece[0]}: {piece[1][direction]}')
                        # print('stalemate: ', end='')
                        # testing future board
                        if not future(rule, path, board, turn, piece[0], piece[1][direction],
                                      empty, in_check, main_history, rook_history):
                            continue
                        else:
                            # print('FOUND: not stalemate')
                            return False
                    else:
                        # print(f'stalemate: blocked: {piece[0]}: {piece[1][direction]}')
                        break
                else:
                    # print(f'stalemate: invalid rule for: '
                    #       f'{piece[0]} to {piece[1][direction]}')
                    break
            else:
                continue
    else:
        print('Stalemate!')
        return True
