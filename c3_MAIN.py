from c3_BOARD import printboard as printboard, resetboard as resetboard, board as board, space as space
from c3_INPUT import main_input as inputter
from c3_RULE import rules as rule
from c3_CHK import check
from c3_PATH import clearpath
from c3_FUTR import future
from c3_CHKMT import checkmate
from c3_STLMT import stalemate
from c3_HIST import history as history, main_history as mhist, rook_history as rhist
from c3_SPEC import special as special


def chess_gamev3():

    #  MAIN VARIABLES
    turn = "WHITE"
    in_check = False
    # castle_avail = False

    #  resetting the board and place initial piece positions (and print board)
    resetboard()
    printboard(board)

    #  MAIN GAME LOOP
    while True:

        if check(rule, clearpath, board, turn, space, in_check, mhist, rhist, future):
            in_check = True
            if checkmate(board, turn, rule, clearpath, future, space, in_check, mhist, rhist):
                if turn == "WHITE":
                    print('BLACK wins! Game Over')
                else:
                    print('WhiTE wins! Game Over')
                break
        else:
            in_check = False

        if not in_check:
            if stalemate(board, turn, rule, clearpath, future, space, in_check, mhist, rhist):
                print('Draw! Game Over')
                break

        #  INPUT LOOP
        try:
            if not in_check:
                origin, destination = input(f'{turn} select origin, destination: ').split(',')
                origin, destination = origin.upper(), destination.upper()
            else:
                origin, destination = input(f'{turn} IN CHECK, select origin, destination: ').split(',')
                origin, destination = origin.upper(), destination.upper()
        except ValueError:
            printboard(board)
            print('Invalid entry - input error')
            continue

        #  INPUT AND VALIDATE MOVE
        if inputter(turn, origin, destination, board, printboard, space):
            if rule(board, origin, destination, in_check, mhist, rhist, clearpath, future, turn, space):
                if clearpath(board, origin, destination, in_check, space):
                    if future(rule, clearpath, board, turn, origin, destination, space, in_check, mhist, rhist):

                        #  UPDATE BOARD
                        board[destination] = board[origin]
                        board[origin] = space
                        special(board, origin, destination, space, turn)

                        #  UPDATE HISTORY
                        history(board, origin, destination)

                        #  TURN SWITCH
                        if turn == "WHITE":
                            turn = "BLACK"
                        else:
                            turn = "WHITE"

                    else:
                        print('main: error')
                else:
                    print('main: error')
            else:
                print('main: error')
        #  RESET BOARD
        elif origin == '1' and destination == '1':
            print('- reset board -')
            mhist[:], rhist[:] = [], []
            resetboard()
        #  MANUAL TURN SWITCH
        elif origin == '2' and destination == '2':
            print('- manual turn switch -')
            if turn == "WHITE":
                turn = "BLACK"
            else:
                turn = "WHITE"
        elif origin == '3' and destination == '3':
            print(f'{mhist}\n{rhist}')
        else:
            print('main: error')
        printboard(board)


while True:
    play = input('Play a game? (y/n): ')
    play = play.upper()

    if play == "Y":
        chess_gamev3()
    elif play == "N":
        break
    else:
        continue

