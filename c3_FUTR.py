def future(rules, path, current_board, turn, origin, destination, empty, in_check, main_history, rook_history):
    """
     :param rules: function from c3_RULE to test line of attack
     :param path: function from c3_PATH to test clear path of movement
     :param current_board: current board
     :param turn: current player turn
     :param origin: starting coordinate
     :param destination: ending coordinate
     :param empty: passes empty space ("  ")
     :param in_check: passes status of current player - in check or not
     :param main_history: from function c3_HIST passes the history of all moves (for special moves)
     :param rook_history: from function c3_HIST passes the history of rook moves (for special moves)
     :return: returns True if current player is in Check, False if not
     """
    # making a copy of current board called 'futureboard' and pseudo moving piece to test moving into check
    futureBoard = current_board.copy()
    futureBoard[destination] = futureBoard[origin]
    futureBoard[origin] = empty

    # creating list of all opponent piece coordinates and another list of only the current player's king coordinates
    if turn == "WHITE":
        whiteKing = []
        allBlackPieces = []
        for k, v in futureBoard.items():
            if v[0] == "b" and v[-1] != "K":
                allBlackPieces.append(k)
            elif v == "wK":
                whiteKing.append(k)

        # checking all opponent pieces against current players King position, if successfully moving into check,
        # returns *False*
        # print('future: start search')
        for blackPiece in allBlackPieces:
            # print('future: rules: ', end='')
            # print(f'blackpiece: {blackPiece}')
            if rules(futureBoard, blackPiece, whiteKing[0], in_check, main_history,
                     rook_history, path, future, turn, empty):
                # print('future: ', end='')
                if path(futureBoard, blackPiece, whiteKing[0], in_check, empty):
                    # print(f'future: {turn} cannot move into check!')
                    # print('future: end search')
                    return False
                else:
                    pass
                    # print(f'future: invalid path for: {blackPiece}')
            else:
                pass
                # print(f'future: invalid rule for: {blackPiece}')
        else:
            # print('future: not moving into check')
            # print('future: end search')
            return True

    elif turn == "BLACK":
        blackKing = []
        allWhitePieces = []
        for k, v in futureBoard.items():
            if v[0] == "w" and v[-1] != "K":
                allWhitePieces.append(k)
            elif v == "bK":
                blackKing.append(k)

        # print('future: start search')
        for whitePiece in allWhitePieces:
            # print('future: ', end='')
            # print(f'whitepiece: {whitePiece}')
            # print(f'whitePiece:{whitePiece}, blackKing:{blackKing[0]}')
            if rules(futureBoard, whitePiece, blackKing[0], in_check, main_history,
                     rook_history, path, future, turn, empty):
                # print('future: ', end='')
                if path(futureBoard, whitePiece, blackKing[0], in_check, empty):
                    # print(f'future: {turn} cannot move into check!')
                    # print('future: end search')
                    return False
                else:
                    pass
                    # print(f'future: invalid path for: {whitePiece}')
            else:
                pass
                # print(f'future: invalid rule for: {whitePiece}')
        else:
            # print('future: not moving in check')
            # print('future: end search')
            return True
