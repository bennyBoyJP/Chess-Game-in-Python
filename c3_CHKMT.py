def checkmate(board, turn, rule, path, future, empty, in_check, main_history, rook_history):
    """
    :param board: current board
    :param turn: current turn
    :param rule: import function from c3_RULE
    :param path: import function from c3_PATH
    :param future: import function from c3_FUTR *to test each move for moving into check*
    :param empty: empty space of square
    :param in_check: passes status of current player - in check or not
    :param main_history: from function c3_HIST passes the history of all moves
    :param rook_history: from function c3_HIST passes the history of rooks
    :return: returns TRUE if player has no movement which move out of check
    """
# ------------------------------------------------------------------------------------------------------------------
    #  creates list *allPieces* of all pieces of current player
    allPieces = []
    if turn == "WHITE":
        for whitePiece in board:
            if board[whitePiece] == "wK":
                allPieces.insert(0, whitePiece)
            elif board[whitePiece][0] == "w":
                allPieces.append(whitePiece)
    elif turn == "BLACK":
        for blackPiece in board:
            if board[blackPiece] == "bK":
                allPieces.insert(0, blackPiece)
            elif board[blackPiece][0] == "b":
                allPieces.append(blackPiece)

# ------------------------------------------------------------------------------------------------------------------
    # helper function to calculate eligibility in all directions from *night*
    def night_distances(square):
        if abs(ord(square[0]) - ord("A")) >= 2 and abs(int(square[-1]) - 8) >= 1:
            if board[chr(ord(square[0]) - 2) + str(int(square[-1]) + 1)][0] != board[square][0]:
                nightleftup = 1
            else:
                nightleftup = 0
        else:
            nightleftup = 0
        if abs(ord(square[0]) - ord("A")) >= 2 and abs(int(square[-1]) - 1) >= 1:
            if board[chr(ord(square[0]) - 2) + str(int(square[-1]) - 1)][0] != board[square][0]:
                nightleftdown = 1
            else:
                nightleftdown = 0
        else:
            nightleftdown = 0
        if abs(ord(square[0]) - ord("H")) >= 2 and abs(int(square[-1]) - 8) >= 1:
            if board[chr(ord(square[0]) + 2) + str(int(square[-1]) + 1)][0] != board[square][0]:
                nightrightup = 1
            else:
                nightrightup = 0
        else:
            nightrightup = 0
        if abs(ord(square[0]) - ord("H")) >= 2 and abs(int(square[-1]) - 1) >= 1:
            if board[chr(ord(square[0]) + 2) + str(int(square[-1]) - 1)][0] != board[square][0]:
                nightrightdown = 1
            else:
                nightrightdown = 0
        else:
            nightrightdown = 0
        if abs(ord(square[0]) - ord("A")) >= 1 and abs(int(square[-1]) - 8) >= 2:
            if board[chr(ord(square[0]) - 1) + str(int(square[-1]) + 2)][0] != board[square][0]:
                nightupleft = 1
            else:
                nightupleft = 0
        else:
            nightupleft = 0
        if abs(ord(square[0]) - ord("H")) >= 1 and abs(int(square[-1]) - 8) >= 2:
            if board[chr(ord(square[0]) + 1) + str(int(square[-1]) + 2)][0] != board[square][0]:
                nightupright = 1
            else:
                nightupright = 0
        else:
            nightupright = 0
        if abs(ord(square[0]) - ord("A")) >= 1 and abs(int(square[-1]) - 1) >= 2:
            if board[chr(ord(square[0]) - 1) + str(int(square[-1]) - 2)][0] != board[square][0]:
                nightdownleft = 1
            else:
                nightdownleft = 0
        else:
            nightdownleft = 0
        if abs(ord(square[0]) - ord("H")) >= 1 and abs(int(square[-1]) - 1) >= 2:
            if board[chr(ord(square[0]) + 1) + str(int(square[-1]) - 2)][0] != board[square][0]:
                nightdownright = 1
            else:
                nightdownright = 0
        else:
            nightdownright = 0

        return [square, [nightleftup, nightleftdown, nightrightup, nightrightdown,
                         nightupleft, nightupright, nightdownleft, nightdownright]]

# ------------------------------------------------------------------------------------------------------------------
    # helper function to calculate distances to edge of board in all directions from *queen*
    def queen_distances(square):

        left = abs(ord(square[0]) - ord("A"))
        right = abs(ord(square[0]) - ord("H"))
        up = abs(int(square[-1]) - 8)
        down = abs(int(square[-1]) - 1)
        if abs(ord(square[0]) - ord("A")) <= abs(int(square[-1]) - 8):
            up_left = abs(ord(square[0]) - ord("A"))
        else:
            up_left = abs(int(square[-1]) - 8)
        if abs(ord(square[0]) - ord("H")) <= abs(int(square[-1]) - 8):
            up_right = abs(ord(square[0]) - ord("H"))
        else:
            up_right = abs(int(square[-1]) - 8)
        if abs(ord(square[0]) - ord("A")) <= abs(int(square[-1]) - 1):
            down_left = abs(ord(square[0]) - ord("A"))
        else:
            down_left = abs(int(square[-1]) - 1)
        if abs(ord(square[0]) - ord("H")) <= abs(int(square[-1]) - 1):
            down_right = abs(ord(square[0]) - ord("H"))
        else:
            down_right = abs(int(square[-1]) - 1)

        return [square, [left, right, up, down, up_left, up_right, down_left, down_right]]

# ------------------------------------------------------------------------------------------------------------------
    # helper function to calculate available move or not in all directions from *king*
    def king_distances(square):

        if chr(ord(square[0]) - 1) >= "A" and board[chr(ord(square[0]) - 1) + square[-1]][0] != board[square][0]:
            left = 1
        else:
            left = 0
        if chr(ord(square[0]) + 1) <= "H" and board[chr(ord(square[0]) + 1) + square[-1]][0] != board[square][0]:
            right = 1
        else:
            right = 0
        if int(square[-1]) + 1 <= 8 and board[square[0] + str(int(square[-1]) + 1)][0] != board[square][0]:
            up = 1
        else:
            up = 0
        if int(square[-1]) - 1 >= 1 and board[square[0] + str(int(square[-1]) - 1)][0] != board[square][0]:
            down = 1
        else:
            down = 0
        if chr(ord(square[0]) - 1) >= "A" and int(square[-1]) + 1 <= 8 and \
                board[chr(ord(square[0]) - 1) + str(int(square[-1]) + 1)][0] != board[square][0]:
            up_left = 1
        else:
            up_left = 0
        if chr(ord(square[0]) + 1) <= "H" and int(square[-1]) + 1 <= 8 and \
                board[chr(ord(square[0]) + 1) + str(int(square[-1]) + 1)][0] != board[square][0]:
            up_right = 1
        else:
            up_right = 0
        if chr(ord(square[0]) - 1) >= "A" and int(square[-1]) - 1 >= 1 and \
                board[chr(ord(square[0]) - 1) + str(int(square[-1]) - 1)][0] != board[square][0]:
            down_left = 1
        else:
            down_left = 0
        if chr(ord(square[0]) + 1) <= "H" and int(square[-1]) - 1 >= 1 and \
                board[chr(ord(square[0]) + 1) + str(int(square[-1]) - 1)][0] != board[square][0]:
            down_right = 1
        else:
            down_right = 0

        return [square, [left, right, up, down, up_left, up_right, down_left, down_right]]
# ------------------------------------------------------------------------------------------------------------------
    # helper function to calculate available move or not in all directions from *bishop*
    def bishop_distances(square):

        left = 0
        right = 0
        up = 0
        down = 0
        if abs(ord(square[0]) - ord("A")) <= abs(int(square[-1]) - 8):
            up_left = abs(ord(square[0]) - ord("A"))
        else:
            up_left = abs(int(square[-1]) - 8)
        if abs(ord(square[0]) - ord("H")) <= abs(int(square[-1]) - 8):
            up_right = abs(ord(square[0]) - ord("H"))
        else:
            up_right = abs(int(square[-1]) - 8)
        if abs(ord(square[0]) - ord("A")) <= abs(int(square[-1]) - 1):
            down_left = abs(ord(square[0]) - ord("A"))
        else:
            down_left = abs(int(square[-1]) - 1)
        if abs(ord(square[0]) - ord("H")) <= abs(int(square[-1]) - 1):
            down_right = abs(ord(square[0]) - ord("H"))
        else:
            down_right = abs(int(square[-1]) - 1)

        return [square, [left, right, up, down, up_left, up_right, down_left, down_right]]

# ------------------------------------------------------------------------------------------------------------------
    # helper function to calculate available move or not in all directions from *rook*
    def rook_distances(square):

        left = abs(ord(square[0]) - ord("A"))
        right = abs(ord(square[0]) - ord("H"))
        up = abs(int(square[-1]) - 8)
        down = abs(int(square[-1]) - 1)
        up_left = 0
        up_right = 0
        down_left = 0
        down_right = 0

        return [square, [left, right, up, down, up_left, up_right, down_left, down_right]]

# ------------------------------------------------------------------------------------------------------------------
    # helper function to calculate available move or not in all directions from *pawn*
    def pawn_distances(square):

        pawn_limits = {int(square[-1]) - 1 >= 1,
                       int(square[-1]) + 1 <= 8}

        if all(pawn_limits):
            if board[square][0] == "w" and board[square[0] + str(int(square[-1]) + 2)] == empty and \
                    board[square[0] + str(int(square[-1]) + 1)] == empty and int(square[-1]) == 2:
                up = 2
                down = 0
            elif board[square][0] == "w" and board[square[0] + str(int(square[-1]) + 1)] == empty:
                up = 1
                down = 0
            elif board[square][0] == "b" and board[square[0] + str(int(square[-1]) - 2)] == empty and \
                    board[square[0] + str(int(square[-1]) - 1)] == empty and int(square[-1]) == 7:
                up = 0
                down = 2
            elif board[square][0] == "b" and board[square[0] + str(int(square[-1]) - 1)] == empty:
                up = 0
                down = 1
            else:
                up = 0
                down = 0
        else:
            up = 0
            down = 0

        pawn_rival_limits = {chr(ord(square[0]) - 1) >= "A",
                             chr(ord(square[0]) + 1) <= "H",
                             int(square[-1]) - 1 >= 1,
                             int(square[-1]) + 1 <= 8}

        if all(pawn_rival_limits):
            if board[square][0] == "w":
                down_left = 0
                down_right = 0
                if board[chr(ord(square[0]) - 1) + str(int(square[-1]) + 1)][0] == "b":
                    up_left = 1
                    up_right = 0
                elif board[chr(ord(square[0]) + 1) + str(int(square[-1]) + 1)][0] == "b":
                    up_right = 1
                    up_left = 0
                elif board[chr(ord(square[0]) + 1) + str(int(square[-1]) + 1)][0] == "b" and \
                        board[chr(ord(square[0]) - 1) + str(int(square[-1]) + 1)][0] == "b":
                    up_right = 1
                    up_left = 1
                elif board[chr(ord(square[0]) + 1) + str(int(square[-1]) + 1)][0] != "b" and \
                        board[chr(ord(square[0]) - 1) + str(int(square[-1]) + 1)][0] != "b":
                    up_left = 0
                    up_right = 0
                else:
                    up_left = 0
                    up_right = 0

            elif board[square][0] == "b":
                up_left = 0
                up_right = 0
                if board[chr(ord(square[0]) - 1) + str(int(square[-1]) - 1)][0] == "w":
                    down_left = 1
                    down_right = 0
                elif board[chr(ord(square[0]) + 1) + str(int(square[-1]) - 1)][0] == "w":
                    down_right = 1
                    down_left = 0
                elif board[chr(ord(square[0]) + 1) + str(int(square[-1]) - 1)][0] == "w" and \
                        board[chr(ord(square[0]) - 1) + str(int(square[-1]) - 1)][0] == "w":
                    down_right = 1
                    down_left = 1
                elif board[chr(ord(square[0]) + 1) + str(int(square[-1]) - 1)][0] != "w" and \
                        board[chr(ord(square[0]) - 1) + str(int(square[-1]) - 1)][0] != "w":
                    down_left = 0
                    down_right = 0
                else:
                    down_left = 0
                    down_right = 0
            else:
                up_left = 0
                up_right = 0
                down_left = 0
                down_right = 0
        else:
            up_left = 0
            up_right = 0
            down_left = 0
            down_right = 0

        left = 0
        right = 0

        return [square, [left, right, up, down, up_left, up_right, down_left, down_right]]

# ------------------------------------------------------------------------------------------------------------------
    #  appends all piece movement lists into 'allPiecesDistance'
    allPiecesDistance = []
    for coordinate in allPieces:
        if board[coordinate][-1] == "K":
            allPiecesDistance.append(king_distances(coordinate))
        elif board[coordinate][-1] == "Q":
            allPiecesDistance.append(queen_distances(coordinate))
        elif board[coordinate][-1] == "n":
            allPiecesDistance.append(night_distances(coordinate))
        elif board[coordinate][-1] == "b":
            allPiecesDistance.append(bishop_distances(coordinate))
        elif board[coordinate][-1] == "r":
            allPiecesDistance.append(rook_distances(coordinate))
        elif board[coordinate][-1] == "p":
            allPiecesDistance.append(pawn_distances(coordinate))

# ------------------------------------------------------------------------------------------------------------------
    for piece in allPiecesDistance:  # temp for testing
        print(piece)

    # helper function to calculate coordinate of destination from provided start point and amount of squares
    # in a given direction
    def end_coord(route, start, amount):
        if route == 0:  # left
            return chr(ord(start[0]) - amount) + start[-1]
        elif route == 1:  # right
            return chr(ord(start[0]) + amount) + start[-1]
        elif route == 2:  # up
            return start[0] + str(int(start[-1]) + amount)
        elif route == 3:  # down
            return start[0] + str(int(start[-1]) - amount)
        elif route == 4:  # up_left
            return chr(ord(start[0]) - amount) + str(int(start[-1]) + amount)
        elif route == 5:  # up_right
            return chr(ord(start[0]) + amount) + str(int(start[-1]) + amount)
        elif route == 6:  # down_left
            return chr(ord(start[0]) - amount) + str(int(start[-1]) - amount)
        elif route == 7:  # down_right
            return chr(ord(start[0]) + amount) + str(int(start[-1]) - amount)

    #   iterates through indices (spaces in each direction) of each item in allPiecesDistance
    #   ref: 0 = left, 1 = right, 2 = up, 3 = down, 4 = up_left, 5 = up_right, 6 = down_left, 7 = down_right

    def night_end_coord(route, start):
        if route == 0:  # night_left_up
            return chr(ord(start[0]) - 2) + str(int(start[-1]) + 1)
        elif route == 1:  # night_left_down
            return chr(ord(start[0]) - 2) + str(int(start[-1]) - 1)
        elif route == 2:  # night_right_up
            return chr(ord(start[0]) + 2) + str(int(start[-1]) + 1)
        elif route == 3:  # night_right_down
            return chr(ord(start[0]) + 2) + str(int(start[-1]) - 1)
        elif route == 4:  # night_up_left
            return chr(ord(start[0]) - 1) + str(int(start[-1]) + 2)
        elif route == 5:  # night_up_right
            return chr(ord(start[0]) + 1) + str(int(start[-1]) + 2)
        elif route == 6:  # night_down_left
            return chr(ord(start[0]) - 1) + str(int(start[-1]) - 2)
        elif route == 7:  # night_down_right
            return chr(ord(start[0]) + 1) + str(int(start[-1]) - 2)

# ------------------------------------------------------------------------------------------------------------------
    directions = ['left', 'right', 'up', 'down', 'upleft', 'upright', 'downleft', 'downright']
    night_directions = ['nightleftup', 'nightleftdown', 'nightrightup', 'nightrightdown',
                        'nightupleft', 'nightupright', 'nightdownleft', 'nightdownright']
    director = range(8)

    for piece in allPiecesDistance:                             # iterates through each piece of allPiecesDistance
        for direction in director:                              # iterates from (0 - 7)
            if piece[1][direction] > 0:                         # skips any item with a distance of zero
                distance = range(1, piece[1][direction] + 1)    # creates distance of current direction iterable
                for spaces in distance:                         # iterate each space to max distance
                    if board[piece[0]][-1] != "n":              # does not include night piece
                        # end variable from end_coord function(s) (above)
                        end_square = end_coord(direction, piece[0], spaces)
                        # print('checkmate: ', end='')
                        # testing rule of movement
                        if rule(board, piece[0], end_square, in_check, main_history,
                                rook_history, path, future, turn, empty):
                            # print(f'checkmate: valid rule for: {piece[0]}: '
                            #       f'{directions[direction]} by {spaces} space(s)')
                            # print('checkmate: ', end='')
                            if path(board, piece[0], end_square, in_check, empty):                    # testing path of movement
                                # print(f'checkmate: path for: {piece[0]}: {directions[direction]} by {spaces} spaces')
                                # print('checkmate: ', end='')
                                # testing future board
                                if not future(rule, path, board, turn, piece[0], end_square,
                                              empty, in_check, main_history, rook_history):
                                    continue
                                else:
                                    # print('FOUND: not checkmate')
                                    return False
                            else:
                                # print(f'checkmate: blocked: {piece[0]}: {directions[direction]} by {spaces} space(s)')
                                break
                        else:
                            # print(f'checkmate: invalid rule for: '
                            #       f'{piece[0]} to {directions[direction]} by {spaces} spaces')
                            break
                    elif board[piece[0]][-1] == "n":                                        # night movement testing
                        end_square = night_end_coord(direction, piece[0])
                        # print('checkmate: ', end='')
                        if rule(board, piece[0], end_square, in_check, main_history,
                                rook_history, path, future, turn, empty):
                            # print(f'checkmate: valid rule for: {piece[0]}: '
                            #       f'{night_directions[direction]}')
                            # print('checkmate: ', end='')
                            if path(board, piece[0], end_square, in_check, empty):                    # testing path of movement
                                # print(f'checkmate: path for: {piece[0]}: {night_directions[direction]}')
                                # print('checkmate: ', end='')
                                # testing future board
                                if not future(rule, path, board, turn, piece[0], end_square,
                                              empty, in_check, main_history, rook_history):
                                    continue
                                else:
                                    # not checkmate
                                    # print('FOUND: not checkmate')
                                    return False
                    else:
                        # print(piece)
                        # print('ERROR: no pieces found in allPiecesDistance')
                        continue
            else:
                continue
    else:
        print('Checkmate!')
        return True
