def clearpath(board, origin, destination, in_check, empty):
    """
    :param board: current board
    :param origin: starting coordinate
    :param destination: ending coordinate
    :param empty: passes empty space ("  ")
    :return: returns true if move is ONLY not obstructed
    """

    # clearpath variables
    x = origin[0]                               # x coordinate of origin (letter)
    y = origin[-1]                              # y coordinate of origin (numeral)
    h_travel = ord(destination[0]) - ord(x)     # distance of Horizontal travel
    v_travel = int(destination[-1]) - int(y)    # distance of Vertical travel
    # print(f'h_travel: {h_travel}, v_travel: {v_travel}')
    move = 1                                    # used for while loops (passed as 'spaces')

# ------------------------------------------------------------------------------------------------------------------
    # function to test for clear passage to the right
    def right(spaces):

        while abs(h_travel) - spaces >= 0:
            if spaces == abs(h_travel):
                # print('path: right path: clear')
                return True
            elif board[chr(ord(x) + spaces) + str(y)] == empty:
                spaces += 1
                continue
            else:
                # print(f'path: right path: {origin} blocked: {spaces} spaces')
                return False
# ------------------------------------------------------------------------------------------------------------------
    def left(spaces):

        while abs(h_travel) - spaces >= 0:
            if spaces == abs(h_travel):
                # print('path: left path: clear')
                return True
            elif board[chr(ord(x) - spaces) + str(y)] == empty:
                spaces += 1
                continue
            else:
                # print(f'path: left path: {origin} blocked: {spaces} spaces')
                return False
# ------------------------------------------------------------------------------------------------------------------
    def up(spaces):

        while abs(v_travel) - spaces >= 0:
            if spaces == abs(v_travel):
                # print('path: up path: clear')
                return True
            elif board[x + str(int(y) + spaces)] == empty:
                spaces += 1
                continue
            else:
                # print(f'path: up path: {origin} blocked: {spaces} spaces')
                return False
# ------------------------------------------------------------------------------------------------------------------
    def down(spaces):

        while abs(v_travel) - spaces >= 0:
            if spaces == abs(v_travel):
                # print('path: down path: clear')
                return True
            elif board[x + str(int(y) - spaces)] == empty:
                spaces += 1
                continue
            else:
                # print(f'path: down path: {origin} blocked: {spaces} spaces')
                return False
# ------------------------------------------------------------------------------------------------------------------
    def up_right(spaces):

        while abs(v_travel) - spaces >= 0:
            if spaces == abs(v_travel):
                # print('path: up_right path: clear')
                return True
            elif board[chr(ord(x) + spaces) + str(int(y) + spaces)] == empty:
                spaces += 1
                continue
            else:
                # print(f'path: up_right path: {origin} blocked: {spaces} spaces')
                return False
# ------------------------------------------------------------------------------------------------------------------
    def up_left(spaces):

        while abs(v_travel) - spaces >= 0:
            if spaces == abs(v_travel):
                # print('path: up_left path: clear')
                return True
            elif board[chr(ord(x) - spaces) + str(int(y) + spaces)] == empty:
                spaces += 1
                continue
            else:
                # print(f'path: up_left path: {origin} blocked: {spaces} spaces')
                return False
# ------------------------------------------------------------------------------------------------------------------
    def down_left(spaces):

        while abs(v_travel) - spaces >= 0:
            if spaces == abs(v_travel):
                # print('path: down_left path: clear')
                return True
            elif board[chr(ord(x) - spaces) + str(int(y) - spaces)] == empty:
                spaces += 1
                continue
            else:
                # print(f'path: down_left path: {origin} blocked: {spaces} spaces')
                return False
# ------------------------------------------------------------------------------------------------------------------
    def down_right(spaces):

        while abs(v_travel) - spaces >= 0:
            if spaces == abs(v_travel):
                # print('path: down_right path: clear')
                return True
            elif board[chr(ord(x) + spaces) + str(int(y) - spaces)] == empty:
                spaces += 1
                continue
            else:
                # print(f'path: down_right path: {origin} blocked: {spaces} spaces')
                return False
# ------------------------------------------------------------------------------------------------------------------

    # from clearpath function - h/v travel determines direction of movement
    if board[origin][0] != board[destination][0]:  # cannot land on own piece (when performing checkmate\stalemate)
        if board[origin][-1] == "n":
            return True
        elif h_travel > 0 and v_travel == 0:
            return right(move)
        elif h_travel < 0 and v_travel == 0:
            return left(move)
        elif h_travel == 0 and v_travel > 0:
            return up(move)
        elif h_travel == 0 and v_travel < 0:
            return down(move)
        elif h_travel > 0 and v_travel > 0 and abs(h_travel) == abs(v_travel):
            return up_right(move)
        elif h_travel < 0 and v_travel > 0 and abs(h_travel) == abs(v_travel):
            return up_left(move)
        elif h_travel < 0 and v_travel < 0 and abs(h_travel) == abs(v_travel):
            return down_left(move)
        elif h_travel > 0 and v_travel < 0 and abs(h_travel) == abs(v_travel):
            return down_right(move)
        else:
            print('path: error')
    else:
        print('path: obstruction error')
