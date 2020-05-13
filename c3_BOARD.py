#  empty space
space = "  "
#  white space (if needed)
wspace = "\u2593"*2  # ▓▓

white_pieces = {'wking': 'wK','wqueen': 'wQ','wrook0': 'wr','wrook1': 'wr','wbishop0': 'wb',
                'wbishop1': 'wb','wnight0': 'wn','wnight1': 'wn','wpawn0': 'wp','wpawn1': 'wp',
                'wpawn2': 'wp','wpawn3': 'wp','wpawn4': 'wp','wpawn5': 'wp','wpawn6': 'wp','wpawn7': 'wp'}

black_pieces = {'bking': 'bK','bqueen': 'bQ','brook0': 'br','brook1': 'br','bbishop0': 'bb',
                'bbishop1': 'bb','bnight0': 'bn','bnight1': 'bn','bpawn0': 'bp','bpawn1': 'bp',
                'bpawn2': 'bp','bpawn3': 'bp','bpawn4': 'bp','bpawn5': 'bp','bpawn6': 'bp','bpawn7': 'bp'}

#  array of 64 ranging from A-H from 1-8 - emptyboard
emptyBoard = {'A8': space,'B8': space,'C8': space,'D8': space,'E8': space,'F8': space,'G8': space,'H8': space,
              'A7': space,'B7': space,'C7': space,'D7': space,'E7': space,'F7': space,'G7': space,'H7': space,
              'A6': space,'B6': space,'C6': space,'D6': space,'E6': space,'F6': space,'G6': space,'H6': space,
              'A5': space,'B5': space,'C5': space,'D5': space,'E5': space,'F5': space,'G5': space,'H5': space,
              'A4': space,'B4': space,'C4': space,'D4': space,'E4': space,'F4': space,'G4': space,'H4': space,
              'A3': space,'B3': space,'C3': space,'D3': space,'E3': space,'F3': space,'G3': space,'H3': space,
              'A2': space,'B2': space,'C2': space,'D2': space,'E2': space,'F2': space,'G2': space,'H2': space,
              'A1': space,'B1': space,'C1': space,'D1': space,'E1': space,'F1': space,'G1': space,'H1': space}

#  board assigned new Values (with extra rows (0,9) and columns (@,I) for supporting check scanning if needed)
board = {'@9': space, 'A9': space,'B9': space,'C9': space,'D9': space,'E9': space,'F9': space,'G9': space,'H9': space,
         'I9': space,
         '@8': space, 'A8': space,'B8': space,'C8': space,'D8': space,'E8': space,'F8': space,'G8': space,'H8': space,
         'I8': space,
         '@7': space, 'A7': space,'B7': space,'C7': space,'D7': space,'E7': space,'F7': space,'G7': space,'H7': space,
         'I7': space,
         '@6': space, 'A6': space,'B6': space,'C6': space,'D6': space,'E6': space,'F6': space,'G6': space,'H6': space,
         'I6': space,
         '@5': space, 'A5': space,'B5': space,'C5': space,'D5': space,'E5': space,'F5': space,'G5': space,'H5': space,
         'I5': space,
         '@4': space, 'A4': space,'B4': space,'C4': space,'D4': space,'E4': space,'F4': space,'G4': space,'H4': space,
         'I4': space,
         '@3': space, 'A3': space,'B3': space,'C3': space,'D3': space,'E3': space,'F3': space,'G3': space,'H3': space,
         'I3': space,
         '@2': space, 'A2': space,'B2': space,'C2': space,'D2': space,'E2': space,'F2': space,'G2': space,'H2': space,
         'I2': space,
         '@1': space, 'A1': space,'B1': space,'C1': space,'D1': space,'E1': space,'F1': space,'G1': space,'H1': space,
         'I1': space,
         '@0': space, 'A0': space,'B0': space,'C0': space,'D0': space,'E0': space,'F0': space,'G0': space,'H0': space,
         'I0': space}


def printboard(square):
    """
    :param square: board array as the argument
    :return: image of chessboard with assigned pieces
    """
    print('    a    b    c    d    e    f    g    h   ')
    print('  +----+----+----+----+----+----+----+----+')
    print("8 | " + square['A8'] + " | " + square['B8'] + " | " + square['C8'] + " | " + square['D8'] + " | " + square[
        'E8'] + " | " + square['F8'] + " | " + square['G8'] + " | " + square['H8'] + " | 8")
    print('  +----+----+----+----+----+----+----+----+')
    print("7 | " + square['A7'] + " | " + square['B7'] + " | " + square['C7'] + " | " + square['D7'] + " | " + square[
        'E7'] + " | " + square['F7'] + " | " + square['G7'] + " | " + square['H7'] + " | 7")
    print('  +----+----+----+----+----+----+----+----+')
    print("6 | " + square['A6'] + " | " + square['B6'] + " | " + square['C6'] + " | " + square['D6'] + " | " + square[
        'E6'] + " | " + square['F6'] + " | " + square['G6'] + " | " + square['H6'] + " | 6")
    print('  +----+----+----+----+----+----+----+----+')
    print("5 | " + square['A5'] + " | " + square['B5'] + " | " + square['C5'] + " | " + square['D5'] + " | " + square[
        'E5'] + " | " + square['F5'] + " | " + square['G5'] + " | " + square['H5'] + " | 5")
    print('  +----+----+----+----+----+----+----+----+')
    print("4 | " + square['A4'] + " | " + square['B4'] + " | " + square['C4'] + " | " + square['D4'] + " | " + square[
        'E4'] + " | " + square['F4'] + " | " + square['G4'] + " | " + square['H4'] + " | 4")
    print('  +----+----+----+----+----+----+----+----+')
    print("3 | " + square['A3'] + " | " + square['B3'] + " | " + square['C3'] + " | " + square['D3'] + " | " + square[
        'E3'] + " | " + square['F3'] + " | " + square['G3'] + " | " + square['H3'] + " | 3")
    print('  +----+----+----+----+----+----+----+----+')
    print("2 | " + square['A2'] + " | " + square['B2'] + " | " + square['C2'] + " | " + square['D2'] + " | " + square[
        'E2'] + " | " + square['F2'] + " | " + square['G2'] + " | " + square['H2'] + " | 2")
    print('  +----+----+----+----+----+----+----+----+')
    print("1 | " + square['A1'] + " | " + square['B1'] + " | " + square['C1'] + " | " + square['D1'] + " | " + square[
        'E1'] + " | " + square['F1'] + " | " + square['G1'] + " | " + square['H1'] + " | 1")
    print('  +----+----+----+----+----+----+----+----+')
    print('    a    b    c    d    e    f    g    h   ')


def resetboard():
    """
    :return: returns assigned locations of pieces (can be adjusted for testing)
    """
    # print('- set pieces - ')
    board['A8'] = space
    board['B8'] = space
    board['C8'] = space
    board['D8'] = space
    board['E8'] = space
    board['F8'] = space
    board['G8'] = space
    board['H8'] = space
    board['A7'] = space
    board['B7'] = space
    board['C7'] = space
    board['D7'] = space
    board['E7'] = space
    board['F7'] = space
    board['G7'] = space
    board['H7'] = space
    board['A6'] = space
    board['B6'] = space
    board['C6'] = space
    board['D6'] = space
    board['E6'] = space
    board['F6'] = space
    board['G6'] = space
    board['H6'] = space
    board['A5'] = space
    board['B5'] = space
    board['C5'] = space
    board['D5'] = space
    board['E5'] = space
    board['F5'] = space
    board['G5'] = space
    board['H5'] = space
    board['A4'] = space
    board['B4'] = space
    board['C4'] = space
    board['D4'] = space
    board['E4'] = space
    board['F4'] = space
    board['G4'] = space
    board['H4'] = space
    board['A3'] = space
    board['B3'] = space
    board['C3'] = space
    board['D3'] = space
    board['E3'] = space
    board['F3'] = space
    board['G3'] = space
    board['H3'] = space
    board['A2'] = space
    board['B2'] = space
    board['C2'] = space
    board['D2'] = space
    board['E2'] = space
    board['F2'] = space
    board['G2'] = space
    board['H2'] = space
    board['A1'] = space
    board['B1'] = space
    board['C1'] = space
    board['D1'] = space
    board['E1'] = space
    board['F1'] = space
    board['G1'] = space
    board['H1'] = space

    # black pieces
    board['A7'] = black_pieces['bpawn0']
    board['B7'] = black_pieces['bpawn1']
    board['C7'] = black_pieces['bpawn2']
    board['D7'] = black_pieces['bpawn3']
    board['E7'] = black_pieces['bpawn4']
    board['F7'] = black_pieces['bpawn5']
    board['G7'] = black_pieces['bpawn6']
    board['H7'] = black_pieces['bpawn7']
    board['A8'] = black_pieces['brook0']
    board['B8'] = black_pieces['bnight0']
    board['C8'] = black_pieces['bbishop0']
    board['D8'] = black_pieces['bqueen']
    board['E8'] = black_pieces['bking']
    board['F8'] = black_pieces['bbishop1']
    board['G8'] = black_pieces['bnight1']
    board['H8'] = black_pieces['brook1']

    # white pieces
    board['A2'] = white_pieces['wpawn0']
    board['B2'] = white_pieces['wpawn1']
    board['C2'] = white_pieces['wpawn2']
    board['D2'] = white_pieces['wpawn3']
    board['E2'] = white_pieces['wpawn4']
    board['F2'] = white_pieces['wpawn5']
    board['G2'] = white_pieces['wpawn6']
    board['H2'] = white_pieces['wpawn7']
    board['A1'] = white_pieces['wrook0']
    board['B1'] = white_pieces['wnight0']
    board['C1'] = white_pieces['wbishop0']
    board['D1'] = white_pieces['wqueen']
    board['E1'] = white_pieces['wking']
    board['F1'] = white_pieces['wbishop1']
    board['G1'] = white_pieces['wnight1']
    board['H1'] = white_pieces['wrook1']

    # board['D1'] = white_pieces['wpawn0']
    # board['D2'] = white_pieces['wpawn0']
    # board['D3'] = black_pieces['brook0']
    # board['F1'] = white_pieces['wpawn0']
    # board['F2'] = white_pieces['wpawn0']
    # board['F3'] = black_pieces['brook0']
    # board['E1'] = white_pieces['wking']
    # board['E8'] = black_pieces['bking']
    # board['E4'] = black_pieces['bqueen']