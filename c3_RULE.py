def rules(square, origin, destination, in_check, main_history, rook_history, path, future, turn, empty):
    """
    :param square: imports square
    :param origin: starting coordinate
    :param destination: ending coordinate
    :param in_check: passes status of current player - in check or not
    :param main_history: from function c3_HIST passes the history of all moves (for special moves)
    :param rook_history: from function c3_HIST passes the history of rook moves (for castling)
    :param path: import function from c3_PATH (for castling)
    :param future: import function from c3_FUTR to test each move for moving into check (for castling)
    :param turn: current turn (for castling)
    :param empty: empty space of square (for castling)
    :return: returns True if passed piece follows movement rules
    """

    def king():

        # king's valid movements
        kingMove = {destination == origin[0] + str(int(origin[-1]) + 1),
                    destination == origin[0] + str(int(origin[-1]) - 1),
                    destination == chr(ord(origin[0]) - 1) + origin[-1],
                    destination == chr(ord(origin[0]) + 1) + origin[-1],
                    destination == chr(ord(origin[0]) - 1) + str(int(origin[-1]) + 1),
                    destination == chr(ord(origin[0]) + 1) + str(int(origin[-1]) + 1),
                    destination == chr(ord(origin[0]) - 1) + str(int(origin[-1]) - 1),
                    destination == chr(ord(origin[0]) + 1) + str(int(origin[-1]) - 1)}

        # 2 spaces from the origin (to make sure King is not approaching another King - see below)
        twoUp = destination[0] + str(int(destination[-1]) + 1)
        twoDown = destination[0] + str(int(destination[-1]) - 1)
        twoLeft = chr(ord(destination[0]) - 1) + destination[-1]
        twoRight = chr(ord(destination[0]) + 1) + destination[-1]
        twoUpLeft = chr(ord(destination[0]) - 1) + str(int(destination[-1]) + 1)
        twoUpRight = chr(ord(destination[0]) + 1) + str(int(destination[-1]) + 1)
        twoDownLeft = chr(ord(destination[0]) - 1) + str(int(destination[-1]) - 1)
        twoDownRight = chr(ord(destination[0]) + 1) + str(int(destination[-1]) - 1)

        # rules for White King is not approaching Black King in adjacent square to destination
        rivalKingBlack = {square[twoUp] != "bK",
                          square[twoDown] != "bK",
                          square[twoLeft] != "bK",
                          square[twoRight] != "bK",
                          square[twoUpLeft] != "bK",
                          square[twoUpRight] != "bK",
                          square[twoDownLeft] != "bK",
                          square[twoDownRight] != "bK"}

        # rules for Black King is not approaching White King in adjacent square to destination
        rivalKingWhite = {square[twoUp] != "wK",
                          square[twoDown] != "wK",
                          square[twoLeft] != "wK",
                          square[twoRight] != "wK",
                          square[twoUpLeft] != "wK",
                          square[twoUpRight] != "wK",
                          square[twoDownLeft] != "wK",
                          square[twoDownRight] != "wK"}

        # castling validations
        castle = {square[origin] == "wK" and origin == "E1" and destination == "C1" and square["D1"] == "  " and
                  square["C1"] == "  " and square["B1"] == "  " and "wK" not in main_history and square["A1"] == "wr"
                  and "A1" not in rook_history,
                  square[origin] == "wK" and origin == "E1" and destination == "G1" and square["F1"] == "  " and
                  square["G1"] == "  " and "wK" not in main_history and square["H1"] == "wr" and
                  "H1" not in rook_history,
                  square[origin] == "bK" and origin == "E8" and destination == "C8" and square["D8"] == "  " and
                  square["C8"] == "  " and square["B8"] == "  " and "bK" not in main_history and square["A8"] == "br"
                  and "A8" not in rook_history,
                  square[origin] == "bK" and origin == "E8" and destination == "G8" and square["F8"] == "  " and
                  square["G8"] == "  " and "bK" not in main_history and square["H8"] == "br" and
                  "H8" not in rook_history}

        if any(kingMove):
            if square[origin][0] == "w":
                if all(rivalKingBlack):
                    return True
                else:
                    pass
                    # print('rule: king move error')
            elif square[origin][0] == "b":
                if all(rivalKingWhite):
                    return True
                else:
                    pass
                    # print('rule: king move error')
        elif not in_check:
            if square[origin][0] == "w":
                if any(castle) and all(rivalKingBlack):
                    if destination == "C1":
                        pass_square = "D1"
                        if future(rules, path, square, turn, origin, pass_square, empty, in_check,
                                  main_history, rook_history):
                            return True
                        else:
                            # print('rule: white king move error')
                            return False
                    elif destination == "G1":
                        pass_square = "F1"
                        if future(rules, path, square, turn, origin, pass_square, empty, in_check,
                                  main_history, rook_history):
                            return True
                        else:
                            # print('rule: white king move error')
                            return False
                else:
                    print('rule: king move error')
                    return False

            elif square[origin][0] == "b":
                if any(castle) and all(rivalKingWhite):
                    if destination == "C8":
                        pass_square = "D8"
                        if future(rules, path, square, turn, origin, pass_square, empty, in_check,
                                  main_history, rook_history):
                            return True
                        else:
                            # print('rule: king move error')
                            return False
                    elif destination == "G8":
                        pass_square = "F8"
                        if future(rules, path, square, turn, origin, pass_square, empty, in_check,
                                  main_history, rook_history):
                            return True
                        else:
                            # print('rule: king move error')
                            return False
                else:
                    # print('rule: king move error')
                    return False

# ------------------------------------------------------------------------------------------------------------------
    def queen():

        # queen's valid movements
        queenMove = {abs(int(origin[-1]) - int(destination[-1])) <= 7 and
                     abs(ord(origin[0]) - ord(destination[0])) == 0,
                     abs(ord(origin[0]) - ord(destination[0])) <= 7 and
                     abs(int(origin[-1]) - int(destination[-1])) == 0,
                     abs(int(origin[-1]) - int(destination[-1])) ==
                     abs(ord(origin[0]) - ord(destination[0]))}

        if any(queenMove):
            return True
        else:
            # print('rule: queen move error')
            return False

# ------------------------------------------------------------------------------------------------------------------
    def bishop():

        # bishop's valid movements
        bishopMove = {abs(int(origin[-1]) - int(destination[-1])) ==
                      abs(ord(origin[0]) - ord(destination[0]))}

        if any(bishopMove):
            return True
        else:
            # print('rule: bishop move error')
            return False

# ------------------------------------------------------------------------------------------------------------------
    def night():

        # night's valid movements (yes, night not, knight ;) this misspell was to avoid conflict with 'k' in King
        nightMove = {destination == chr(ord(origin[0]) - 1) + str(int(origin[-1]) + 2),
                     destination == chr(ord(origin[0]) + 1) + str(int(origin[-1]) + 2),
                     destination == chr(ord(origin[0]) - 1) + str(int(origin[-1]) - 2),
                     destination == chr(ord(origin[0]) + 1) + str(int(origin[-1]) - 2),
                     destination == chr(ord(origin[0]) - 2) + str(int(origin[-1]) + 1),
                     destination == chr(ord(origin[0]) + 2) + str(int(origin[-1]) + 1),
                     destination == chr(ord(origin[0]) - 2) + str(int(origin[-1]) - 1),
                     destination == chr(ord(origin[0]) + 2) + str(int(origin[-1]) - 1)}
        if any(nightMove):
            return True
        else:
            # print('rule: night move error')
            return False

# ------------------------------------------------------------------------------------------------------------------
    def rook():

        # rook's valid movements
        rookMove = {abs(int(origin[-1]) - int(destination[-1])) <= 7 and
                    abs(ord(origin[0]) - ord(destination[0])) == 0,
                    abs(ord(origin[0]) - ord(destination[0])) <= 7 and
                    abs(int(origin[-1]) - int(destination[-1])) == 0}

        if any(rookMove):
            return True
        else:
            # print('rule: rook move error')
            return False

# ------------------------------------------------------------------------------------------------------------------
    def pawn():

        # pawn's valid movements

        pawnTwoSpace = {abs(int(origin[-1]) - int(destination[-1])) == 1,
                        abs(int(origin[-1]) - int(destination[-1])) == 2}

        pawnOneSpace = {abs(int(origin[-1]) - int(destination[-1])) == 1}

        pawnTakeRival = {abs(int(origin[-1]) - int(destination[-1])) == 1 and
                         abs(ord(origin[0]) - ord(destination[0])) == 1}

        if int(origin[-1]) == 2 or int(origin[-1]) == 7 and origin[0] == destination[0]:
            if (square[origin][0] == "w" and int(origin[-1]) < int(destination[-1])) or \
                    (square[origin][0] == "b" and int(origin[-1]) > int(destination[-1])):
                if any(pawnTwoSpace):
                    return True
                else:
                    # print('rule: pawn move error - 2 spaces')
                    return False
            else:
                return False

        elif origin[0] == destination[0]:
            if (square[origin][0] == "w" and int(origin[-1]) < int(destination[-1])) or \
                    (square[origin][0] == "b" and int(origin[-1]) > int(destination[-1])):
                if any(pawnOneSpace):
                    return True
            else:
                # print('rule: pawn move error - 1 space')
                return False

        elif square[destination] != "  " and square[origin][0] != square[destination][0]:
            if any(pawnTakeRival):
                return True
            else:
                # print('rule: pawn move error - take rival')
                return False

        elif turn == "WHITE":
            if len(main_history):
                en_passantWhite = {main_history[-2] == "bp",
                                   main_history[-1][0][-1] == "7",
                                   main_history[-1][-1][-1] == "5",
                                   origin[-1] == "5",
                                   destination[-1] == "6",
                                   square[destination] == empty,
                                   ord(destination[0]) == ord(main_history[-1][-1][0])}

                if all(en_passantWhite):
                    future_square = square.copy()
                    future_square[main_history[-1][-1]] = empty
                    if future(rules, path, future_square, turn, origin, destination, empty, in_check,
                              main_history, rook_history):
                        print('En Passant!')
                        return True
                    else:
                        # print('en passant into check')
                        return False
                else:
                    # print('NOT en passant rules')
                    return False
        elif turn == "BLACK":
            if len(main_history):
                en_passantBlack = {main_history[-2] == "wp",
                                   main_history[-1][0][-1] == "2",
                                   main_history[-1][-1][-1] == "4",
                                   origin[-1] == "4",
                                   destination[-1] == "3",
                                   square[destination] == empty,
                                   ord(destination[0]) == ord(main_history[-1][-1][0])}
                if all(en_passantBlack):
                    future_square = square.copy()
                    future_square[main_history[-1][-1]] = empty
                    if future(rules, path, future_square, turn, origin, destination, empty, in_check,
                              main_history, rook_history):
                        print('En Passant!')
                        return True
                    else:
                        return False
                else:
                    return False

        else:
            print('rule: pawn move error')
            return False

# ------------------------------------------------------------------------------------------------------------------
    if square[origin][-1] == "K":
        return king()
    elif square[origin][-1] == "Q":
        return queen()
    elif square[origin][-1] == "b":
        return bishop()
    elif square[origin][-1] == "n":
        return night()
    elif square[origin][-1] == "r":
        return rook()
    elif square[origin][-1] == "p":
        return pawn()
    else:
        print('rule: error')
    return False
