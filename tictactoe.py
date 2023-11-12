"""
    @author Álvaro Menacho Rodríguez

    Tic Tac Toe
"""
import random


def draw_board(board):
    """
    Draw in the console the curretn board, displaying rows (1, 2, 3) and
    columns (a, b, c).

    :param: board: list of lists displaying a 3x3 board. Symbols available: x, o, ' '
    :return:
    """

    line = '     +---+---+---+'

    # Head
    print('\n')
    print('       a   b   c  ')

    # Rows
    print(line)
    for i, c in enumerate(board):
        print('   {0} | {1[0]} | {1[1]} | {1[2]} |'.format(1 + i, c))
        print(line)

    print('\n')


def check_board(board):
    """
    Check if the game is over
    :param board: 3x3 play board
    :return: tuple indicating if the game is over (True,False) and the result [(1,2,0), -1]
    """

    # Checking diagonals
    def check_diag(board_diag):
        win_x = True
        win_o = True

        # Check main diag
        for i in range(3):
            if board_diag[i][i] != 'x':
                win_x = False
            if board_diag[i][i] != 'o':
                win_o = False
            # Exit condition
            if not win_x and not win_o:
                break
        # If one yes one of them have won
        if win_x:
            return 1
        elif win_o:
            return 2

        # Reset to check the other diag
        win_x = True
        win_o = True

        # Same index for the other diag
        for i in range(3):
            if board_diag[i][3 - 1 - i] != 'x':
                win_x = False
            if board_diag[i][3 - 1 - i] != 'o':
                win_o = False
            if not win_x and not win_o:
                break

        # Final result
        if win_x:
            return 1
        elif win_o:
            return 2
        else:
            return 0

    # Check columns
    def check_columns(board_columns):
        win_x = True
        win_o = True

        # Iterate the columns changing the indexes
        for i in range(3):
            win_x = True
            win_o = True
            for k in range(3):
                if board_columns[k][i] != 'x':
                    win_x = False
                if board_columns[k][i] != 'o':
                    win_o = False

            # Exit condition when it finds a winner column
            if win_x or win_o:
                break

        # Final result
        if win_x:
            return 1
        elif win_o:
            return 2
        else:
            return 0

    # Check rows
    def check_rows(board_rows):

        # Check rows
        for i in range(3):
            win_x = True
            win_o = True

            # Iterating using index for each row
            for k in range(3):
                if board_rows[i][k] != 'x':
                    win_x = False
                if board_rows[i][k] != 'o':
                    win_o = False

            # Final result
            if win_x:
                return 1
            elif win_o:
                return 2
        return 0

    # Full flag
    full_board = True

    # Check if the board is fulfilled
    for x in range(3):
        for j in range(3):
            if board[x][j] == ' ':
                full_board = False
                break
    # Control variables
    diag_result = -1
    rows_result = -1
    columns_result = -1

    # Retrieve checkings
    diag_result = check_diag(board)
    rows_result = check_rows(board)
    columns_result = check_columns(board)

    # Show match result
    if diag_result == 1 or rows_result == 1 or columns_result == 1:
        return True, 1

    elif diag_result == 2 or rows_result == 2 or columns_result == 2:
        return True, 2

    elif diag_result == 0 and rows_result == 0 and columns_result == 0 and full_board:
        return True, 0

    return False, -1


def move_player(board, symbol):
    """
    Player movement
    :param board: 3x3 play board
    :param symbol: user chosen symbol (x,o)
    :return:
    """
    check = False

    # Movement request after format check
    while not check:
        user_input = input('Enter your next movement "numberletter":')
        check = len(user_input) == 2 and user_input[0] in ['1', '2', '3'] and user_input[1] in ['a', 'b', 'c']

        # If format is right we do the movement
        if check:
            # Do the movement
            if user_input[1] == 'a':
                board[int(user_input[0]) - 1][ord('a') - 97] = symbol
            elif user_input[1] == 'b':
                board[int(user_input[0]) - 1][ord('b') - 97] = symbol
            elif user_input[1] == 'c':
                board[int(user_input[0]) - 1][ord('c') - 97] = symbol


def move_ia(board, symbol):
    """
    Do IA movement
    :param board: 3x3 play board
    :param symbol: ia chosen symbol (x,o)
    :return:
    """
    empty_positions = []

    # Look for empty positions
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                empty_positions.append((i, j))

    # Random movement chosen
    random_position = empty_positions[random.randint(0, len(empty_positions) - 1)]

    # Do the movement
    board[random_position[0]][random_position[1]] = symbol


def draw_initial_board():
    """
    Draw initial board
    :return: 3x3 play board
    """
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    return board


def new_game(difficulty):
    """
    New game tic-tac-toe
    :return: 1-User wins 2-AI wins 3-Tie
    """
    print("Welcome to Tic Tac Toe")
    flag_symbol = False
    user_symbol = ''
    ai_symbol = ''

    # Check valid input
    while not flag_symbol:
        symbol_chosen = input("Choose your symbol 'x' or 'o':")

        # Symbol decision
        if symbol_chosen == 'x' or symbol_chosen == 'o':
            user_symbol = user_symbol.join(symbol_chosen)
            flag_symbol = True

            if user_symbol == 'x':
                ai_symbol = 'o'
            else:
                ai_symbol = 'x'

            # Init board
            board = draw_initial_board()

            # Draw initial board
            print('Welcome to the play board\n')
            print('-' * 50)
            draw_board(board)
            print('-' * 50)

            game_over = False
            result = -1

            # While play is not over we continue doing movements
            while not game_over:
                # Check the board
                game_over, result = check_board(board)

                # AI movement
                if not game_over:
                    # AI starts game
                    if difficulty == 'Easy':
                        move_ia(board, ai_symbol)
                        move_ai_2(board, ai_symbol)
                    elif difficulty == 'Difficult':
                        move_ai_2(board, ai_symbol, 'difícil')
                    draw_board(board)
                    print('-' * 50)

                # Check the board
                game_over, result = check_board(board)

                # User movement
                if not game_over:
                    move_player(board, user_symbol)
                    draw_board(board)
                    print('-' * 50)

            # Show play result
            if result == 1:
                if user_symbol == 'x':
                    print('Congratulations, you won the game!')
                    return 1
                else:
                    print('AI won the match!')
                    return 2
            elif result == 2:
                if user_symbol == 'o':
                    print('Congratulations, you won the game!')
                    return 1
                else:
                    print('AI won the match!')
                    return 2
            elif result == 0:
                print('The result of the game is a tie')
                return 3


def new_tournament():
    """
    New best of 3 games tournament
    :return:
    """
    # Counters
    won_games_needed = 3
    user_won_games = 0
    ai_won_games = 0
    tie_games = 0

    # Check if tournament finished
    while user_won_games != won_games_needed or ai_won_games != won_games_needed:

        game_result = new_game()

        if game_result == 1:
            user_won_games = user_won_games + 1
        elif game_result == 2:
            ai_won_games = ai_won_games + 1
        elif game_result == 3:
            tie_games = tie_games + 1

    # Show tournament result
    if user_won_games == won_games_needed:
        print('Congratulations, you are the winner of the tournament!')
    elif ai_won_games == won_games_needed:
        print('AI has won the tournament')

    print('A total of {0} games were played'.format(
        user_won_games + ai_won_games + tie_games))


def move_ai_2(board, symbol, difficulty='easy'):
    """
    Do AI movement
    :param board: 3x3 play board
    :param symbol: symbol (x,o)
    :param difficulty: easy o difficult
    :return:
    """
    empty_positions = []

    # Find empty positions
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                empty_positions.append((i, j))

    # Difficulty
    if difficulty == 'easy':
        # Choose random position
        random_position = empty_positions[random.randint(0, len(empty_positions) - 1)]

        # Do the movement
        board[random_position[0]][random_position[1]] = symbol

    elif difficulty == 'difficult':
        # Make a copy of the board to try movements
        tablero_sandbox = board.copy()
        optimized_movement = ()

        # Try empty positions
        for movement in empty_positions:
            tablero_sandbox[movement[0]][movement[1]] = symbol

            # Check
            if symbol == 'x':
                if check_board(tablero_sandbox) == (True, 1):
                    optimized_movement = movement

                    board[optimized_movement[0]][optimized_movement[1]] = symbol
                    break
                else:
                    # Choose random position
                    random_position = empty_positions[random.randint(0, len(empty_positions) - 1)]

                    # Do the movement
                    board[random_position[0]][random_position[1]] = symbol

            elif symbol == 'o':
                if check_board(tablero_sandbox) == (True, 2):
                    optimized_movement = movement

                    board[optimized_movement[0]][optimized_movement[1]] = symbol
                    break
                else:
                    # Choose random position
                    random_position = empty_positions[random.randint(0, len(empty_positions) - 1)]

                    # Do the movement
                    board[random_position[0]][random_position[1]] = symbol


new_tournament()
