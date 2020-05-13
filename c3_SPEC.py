def special(board, origin, destination, empty, turn):
    """
    :param board:
    :param origin:
    :param destination:
    :param empty:
    :param turn:
    :return:
    """
    enPassant_move = {abs(int(origin[-1]) - int(destination[-1])) == 1 and
                      abs(ord(origin[0]) - ord(destination[0])) == 1}

    promotion_move = {destination[-1] == "8" and turn == "WHITE",
                      destination[-1] == "1" and turn == "BLACK"}

    def castle():

        if board[origin][-1] == "K":
            if origin == "E1" and destination == "C1":
                board["D1"] = board["A1"]
                board["A1"] = empty
                return True

            elif origin == "E1" and destination == "G1":
                board["F1"] = board["H1"]
                board["H1"] = empty
                return True

            elif origin == "E8" and destination == "C8":
                board["D8"] = board["A8"]
                board["A8"] = empty
                return True

            elif origin == "E8" and destination == "G8":
                board["F8"] = board["H8"]
                board["H8"] = empty
                return True
            else:
                print('invalid castle move')
                return False

    def en_passant():
        if turn == "WHITE":
            board[destination[0] + str(int(destination[-1]) - 1)] = empty
            return True
        elif turn == "BLACK":
            board[destination[0] + str(int(destination[-1]) + 1)] = empty
            return True

    def promotion():
        if turn == "WHITE":
            board[destination] = "wQ"
            return True
        elif turn == "BLACK":
            board[destination] = "bQ"
            return True

    if board[origin][-1] == "K" and abs(ord(origin[0]) - ord(destination[0])) == 2:
        return castle()
    elif all(enPassant_move) and board[destination] == empty:
        return en_passant()
    elif board[destination][-1] == "p" and any(promotion_move):
        return promotion()
    else:
        return False
