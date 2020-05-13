def check(rules, path, board, turn, empty, in_check, main_history, rook_history, future):
    """
    :param rules: function from c3_RULE to test line of attack
    :param path: function from c3_PATH to test clearance to target
    :param board: current board
    :param turn: current player turn
    :param empty: empty square ("  ")
    :param in_check: passes status of current player - in check or not
    :param main_history: from function c3_HIST passes the history of all moves
    :param rook_history: from function c3_HIST passes the history of all rook moves
    :param future function from c3_FUTR to check future board validation
    :return: returns True if current player is in Check, False if not
    """

    if turn == "WHITE":
        whiteKing = []
        allBlackPieces = []
        for k, v in board.items():
            if v[0] == "b" and v[-1] != "K":
                allBlackPieces.append(k)
            elif v == "wK":
                whiteKing.append(k)

        # print('check: searching for line of danger')
        for blackPiece in allBlackPieces:
            # print(f'check: {blackPiece}: rule ', end='')
            # print(f'blackpiece: {blackPiece}, whiteking: {whiteKing}')
            if rules(board, blackPiece, whiteKing[0], in_check, main_history, rook_history, path, future, turn, empty):
                # print(f'check: {blackPiece}: path ', end='')
                if path(board, blackPiece, whiteKing[0], in_check, empty):
                    # print(f'{turn} in Check!')
                    # print('check: completed')
                    return True
        else:
            # print('check: not in check')
            # print('check: completed')
            return False

    elif turn == "BLACK":
        blackKing = []
        allWhitePieces = []
        for k, v in board.items():
            if v[0] == "w" and v[-1] != "K":
                allWhitePieces.append(k)
            elif v == "bK":
                blackKing.append(k)

        # print('check: searching for line of danger')
        for whitePiece in allWhitePieces:
            # print(f'check: {whitePiece}: rule ', end='')
            if rules(board, whitePiece, blackKing[0], in_check, main_history, rook_history, path, future, turn, empty):
                # print(f'check: {whitePiece}: path ', end='')
                if path(board, whitePiece, blackKing[0], in_check, empty):
                    # print(f'{turn} in Check!')
                    # print('check: completed')
                    return True
        else:
            # print('check: not in check')
            # print('check: completed')
            return False
