main_history = []
rook_history = []


def history(board, start, end):
    """
    :param board: current board
    :param start: start point of piece move
    :param end: end point of piece move
    :return: none
    """

    piece = board[end]
    rooks = {"wr", "br"}

    main_history.append(piece)
    main_history.append([start, end])

    if piece in rooks:
        if piece not in rook_history:
            if start == "A1":
                rook_history.append("A1")
            elif start == "H1":
                rook_history.append("H1")
            elif start == "A8":
                rook_history.append("A8")
            elif start == "H8":
                rook_history.append("H8")

    return True

