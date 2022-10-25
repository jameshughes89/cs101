# NAME:
# ST-NUMBER:
# StFX EMAIL:

def setup_game(size: int) -> list:
    """
    Create a new nXn tic-tac-toe game board, where n is the provided size. The game board is a list of n lists, with
    each of the n list having n characters representing the state of the cell. The n lists represent the n rows of the
    game board, and the n characters in each list represent the state of the cell in the column. The state of the cells
    is either ' ' (blank) meaning empty, 'X' meaning player X holds the position, and 'O' means player O holds the
    position.

    For example 3x3, a game board with player X holding the cell in the bottom left corner and player O holding the top
    right cell, can be seen below.

        [[' ', ' ', 'O'],
         [' ', ' ', ' '],
         ['X', ' ', ' ']]

    :param size: Size of the game board to be returned.
    :type size: Integer
    :return: An empty tic-tac-toe game board with all cells set blank.
    :rtype: A list of three lists containing three characters (strings) each.
    """



#assert [[" "]] == setup_game(1)
#assert [[" ", " "], [" ", " "]] == setup_game(2)
#assert [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]] == setup_game(3)
#assert [[" ", " ", " ", " "], [" ", " ", " ", " "], [" ", " ", " ", " "], [" ", " ", " ", " "]] == setup_game(4)
#test_board = setup_game(3)
#assert not (test_board[0] is test_board[1])
#assert not (test_board[0] is test_board[2])
#assert not (test_board[1] is test_board[2])

def parse_move(string: str) -> tuple:
    """
    Parse a move from the string provided as a parameter and return it as a tuple of integers of size 2. First index is
    the column (x), second index is the row (y). Input is expected to be in the form of as "x, y" --- the comma is
    necessary.

        x --- the x/column of the move
        y --- the y/row of the move

    The top left corner of the game board is (0, 0).

    If more than two comma separated values are provided, only the first 2 are returned.

    :param string: String of a move to be parsed.
    :type string: String
    :return: The move, as specified as a column, row pair.
    :rtype: A tuple of integers of size 2 (int(x), int(y))
    """



#assert (0, 0) == parse_move("0, 0")
#assert (2, 1) == parse_move("2,1")
#assert (10, 11) == parse_move("10, 11, 12, 13")

def is_move_valid(move: tuple, board: list) -> bool:
    """
    Checks if the provided move is valid for the current game board. A move is valid if (a) the cell it refers to is
    unoccupied, and (b) it is within the game board.

    :param move: A tuple with the player's move's x and y location.
    :type move: A tuple of integers of size 2 (int(x), int(y)).
    :param board: The current game board.
    :type board: A list of n lists containing n characters (strings) each.
    :return: True if the move is considered valid, False otherwise.
    :rtype: Boolean.
    """



#test_board_3 = [[" ", " ", " "], ["O", "X", " "], [" ", " ", " "]]
#assert True == is_move_valid((0, 0), test_board_3)
#assert True == is_move_valid((2, 2), test_board_3)
#assert False == is_move_valid((-1, 0), test_board_3)
#assert False == is_move_valid((0, -1), test_board_3)
#assert False == is_move_valid((-1, -1), test_board_3)
#assert False == is_move_valid((3, 0), test_board_3)
#assert False == is_move_valid((0, 3), test_board_3)
#assert False == is_move_valid((3, 3), test_board_3)
#assert False == is_move_valid((1, 1), test_board_3)
#assert False == is_move_valid((0, 1), test_board_3)

def apply_move(move: tuple, board: list, player: str) -> list:
    """
    Apply a move to the game board by making a copy of the board and placing the player symbol ('X', or 'O') in the
    move's corresponding location in the new board. This function does not have any side effect.

    The move is provided as a tuple of the form (x, y):
        x --- the x/column of the move
        y --- the y/row of the move

    The top left corner of the game board is (0, 0).

    :param move: A tuple with the player's move's x and y location.
    :type move: A tuple of integers of size 2 (int(x), int(y)).
    :param board: The current game board.
    :type board: A list of n lists containing n characters (strings) each.
    :param player: The current player's symbol ('X' or 'O').
    :type player: A string, either 'X' or 'O'.
    :return: A new board with the current state.
    :rtype: list of lists
    """



#test_board_2 = [[" ", " "], [" ", " "]]
#test_board_2_applied = apply_move((0, 0), test_board_2, "X")
#assert [["X", " "], [" ", " "]] == test_board_2_applied
#assert test_board_2 is not test_board_2_applied
#test_board_2_applied_twice = apply_move((1, 1), test_board_2_applied, "O")
#assert [["X", " "], [" ", "O"]] == test_board_2_applied_twice
#assert test_board_2_applied is not test_board_2_applied_twice
#test_board_3 = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
#test_board_3_applied = apply_move((0, 2), test_board_3, "X")
#assert [[" ", " ", " "], [" ", " ", " "], ["X", " ", " "]] == test_board_3_applied
#assert test_board_3 is not test_board_3_applied
#test_board_3_applied_twice = apply_move((2, 0), test_board_3_applied, "O")
#assert [[" ", " ", "O"], [" ", " ", " "], ["X", " ", " "]] == test_board_3_applied_twice
#assert test_board_3_applied is not test_board_3_applied_twice

def check_row(board: list, row: int, player: str) -> bool:
    """
    Check a specified row on the game board to see if the player has won. This function returns True if the player
    occupies all cells in the row on the game board, otherwise it returns False.

    :param board: The current game board.
    :type board: A list of n lists containing n characters (strings) each.
    :param row: The row on the game board to check (0 being top row).
    :type row: Integer
    :param player: The current player's symbol ('X' or 'O').
    :type player: A string, either 'X' or 'O'.
    :return: True if the player occupies all cells in the specified row.
    :rtype: Boolean.
    """



#test_cases = [["O", "O"], ["X", "X"], ["X", " "], ["O", "X"], [" ", " "]]
#assert True == check_row(test_cases, 0, "O")
#assert False == check_row(test_cases, 0, "X")
#assert False == check_row(test_cases, 1, "O")
#assert True == check_row(test_cases, 1, "X")
#assert False == check_row(test_cases, 2, "O")
#assert False == check_row(test_cases, 2, "X")
#assert False == check_row(test_cases, 3, "O")
#assert False == check_row(test_cases, 3, "X")
#assert False == check_row(test_cases, 4, "O")
#assert False == check_row(test_cases, 4, "X")

def check_column(board: list, column: int, player: str) -> bool:
    """
    Check a specified column on the game board to see if the player has won. This function returns True if the player
    occupies all cells in the column on the game board, otherwise it returns False.

    :param board: The current game board.
    :type board: A list of n lists containing n characters (strings) each.
    :param column: The column on the game board to check (0 being left most).
    :type column: Integer
    :param player: The current player's symbol ('X' or 'O').
    :type player: A string, either 'X' or 'O'.
    :return: True if the player occupies all cells in the specified column.
    :rtype: Boolean.
    """



#test_cases = [["O", "X", "X", "O", " "], ["O", "X", " ", "X", " "], ["O", "X", " ", "O", " "]]
#assert True == check_column(test_cases, 0, "O")
#assert False == check_column(test_cases, 0, "X")
#assert False == check_column(test_cases, 1, "O")
#assert True == check_column(test_cases, 1, "X")
#assert False == check_column(test_cases, 2, "O")
#assert False == check_column(test_cases, 2, "X")
#assert False == check_column(test_cases, 3, "O")
#assert False == check_column(test_cases, 3, "X")
#assert False == check_column(test_cases, 4, "O")
#assert False == check_column(test_cases, 4, "X")

def check_down_diagonal(board: list, player: str) -> bool:
    """
    Check the down right diagonal (start top left, ends bottom right) on the game board to see if the player has won.
    This function returns True if the player occupies all cells within the diagonal, otherwise it returns False.

    :param board: The current game board.
    :type board: A list of n lists containing n characters (strings) each.
    :param player: The current player's symbol ('X' or 'O').
    :type player: A string, either 'X' or 'O'.
    :return: True if the player occupies all cells in the diagonal.
    :rtype: Boolean.
    """



#assert True == check_down_diagonal([["X", " ", " "], [" ", "X", " "], [" ", " ", "X"]], "X")
#assert False == check_down_diagonal([["X", " ", " "], [" ", "X", " "], [" ", " ", "X"]], "O")
#assert False == check_down_diagonal([["X", " ", " "], [" ", " ", " "], [" ", " ", "X"]], "X")
#assert False == check_down_diagonal([["X", " ", " "], [" ", " ", " "], [" ", " ", "X"]], "O")
#assert False == check_down_diagonal([["X", " ", " "], [" ", "X", " "], [" ", " ", "O"]], "X")
#assert False == check_down_diagonal([["X", " ", " "], [" ", "X", " "], [" ", " ", "O"]], "O")
#assert False == check_down_diagonal([[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]], "X")
#assert False == check_down_diagonal([[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]], "O")
#assert True == check_down_diagonal(
#    [["X", " ", " ", " "], [" ", "X", " ", " "], [" ", " ", "X", " "], [" ", " ", " ", "X"]], "X"
#)
#assert False == check_down_diagonal(
#    [["X", " ", " ", " "], [" ", "X", " ", " "], [" ", " ", "X", " "], [" ", " ", " ", "X"]], "O"
#)
#assert False == check_down_diagonal(
#    [["X", " ", " ", " "], [" ", "X", " ", " "], [" ", " ", "X", " "], [" ", " ", " ", "O"]], "X"
#)
#assert False == check_down_diagonal(
#    [["X", " ", " ", " "], [" ", "X", " ", " "], [" ", " ", "X", " "], [" ", " ", " ", "O"]], "O"
#)

def check_up_diagonal(board: list, player: str) -> bool:
    """
    Check the up right diagonal (start bottom left, ends top right) on the game board to see if the player has won.
    This function returns True if the player occupies all cells within the diagonal, otherwise it returns False.

    :param board: The current game board.
    :type board: A list of n lists containing n characters (strings) each.
    :param player: The current player's symbol ('X' or 'O').
    :type player: A string, either 'X' or 'O'.
    :return: True if the player occupies all cells in the diagonal.
    :rtype: Boolean.
    """



#assert True == check_up_diagonal([[" ", " ", "X"], [" ", "X", " "], ["X", " ", " "]], "X")
#assert False == check_up_diagonal([[" ", " ", "X"], [" ", "X", " "], ["X", " ", " "]], "O")
#assert False == check_up_diagonal([[" ", " ", "X"], [" ", " ", " "], ["X", " ", " "]], "X")
#assert False == check_up_diagonal([[" ", " ", "X"], [" ", " ", " "], ["X", " ", " "]], "O")
#assert False == check_up_diagonal([[" ", " ", "X"], [" ", "X", " "], ["O", " ", " "]], "X")
#assert False == check_up_diagonal([[" ", " ", "X"], [" ", "X", " "], ["O", " ", ""]], "O")
#assert False == check_up_diagonal([[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]], "X")
#assert False == check_up_diagonal([[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]], "O")
#assert True == check_up_diagonal(
#    [[" ", " ", " ", "X"], [" ", " ", "X", " "], [" ", "X", " ", " "], ["X", " ", " ", " "]], "X"
#)
#assert False == check_up_diagonal(
#    [[" ", " ", " ", "X"], [" ", " ", "X", " "], [" ", "X", " ", " "], ["X", " ", " ", " "]], "O"
#)
#assert False == check_up_diagonal(
#    [[" ", " ", " ", "X"], [" ", " ", "X", " "], [" ", "X", " ", " "], ["O", " ", " ", " "]], "X"
#)
#assert False == check_up_diagonal(
#    [[" ", " ", " ", "X"], [" ", " ", "X", " "], [" ", "X", " ", " "], ["O", " ", " ", " "]], "O"
#)

def check_for_winner(board: list, player: str) -> bool:
    """
    Check the current game board to see if the specified player has won the game. If the specified player has won,
    return True, otherwise return False. This function simply calls the other check functions: `check_row`,
    `check_column`, `check_up_diagonal`, `check_down_diagonal`.

    :param board: The current game board.
    :type board: A list of n lists containing n characters (strings) each.
    :param player: The current player's symbol ('X' or 'O').
    :type player: A string, either 'X' or 'O'.
    :return: True if the player occupies all cells in the diagonal.
    :rtype: Boolean.
    """


#no_winner = [["O", "X", " "], ["X", "O", "X"], ["O", "X", " "]]
#row_winner = [["X", "X"], [" ", " "]]
#column_winner = [["O", " ", " "], ["O", " ", " "], ["O", " ", " "]]
#down_diagonal_winner = [["X", " ", " ", " "], [" ", "X", " ", " "], [" ", " ", "X", " "], [" ", " ", " ", "X"]]
#up_diagonal_winner = [[" ", " ", " ", "O"], [" ", " ", "O", " "], [" ", "O", " ", " "], ["O", " ", " ", " "]]
#assert False == check_for_winner(no_winner, "X")
#assert False == check_for_winner(no_winner, "O")
#assert True == check_for_winner(row_winner, "X")
#assert True == check_for_winner(column_winner, "O")
#assert True == check_for_winner(down_diagonal_winner, "X")
#assert True == check_for_winner(up_diagonal_winner, "O")

def render_cell(board: list, x: int, y: int) -> str:
    """
    Render the specified cell from the game board as a string and return the string. The possible return values are 'X',
    'Y', or ' ' (empty). The origin of the board (0, 0) is the top left corner of the game board.

    :param board: The current game board.
    :type board: A list of n lists containing n characters (strings) each.
    :param x: x coordinate of the cell to render, with 0 being left-hand side of board.
    :type x: integer.
    :param y: y coordinate of the cell to render, with 0 being the top of the board.
    :type y: integer.
    :return: String representation of the contents of the cell ('X', 'O', or ' ').
    :rtype: String.
    """


#test_board_2 = [[" ", "X"], ["O", " "]]
#assert " " == render_cell(test_board_2, 0, 0)
#assert "X" == render_cell(test_board_2, 1, 0)
#assert "O" == render_cell(test_board_2, 0, 1)
#test_board_3 = [["X", " ", "O"], [" ", "O", " "], ["O", " ", "X"]]
#assert " " == render_cell(test_board_3, 0, 1)
#assert "X" == render_cell(test_board_3, 2, 2)
#assert "O" == render_cell(test_board_3, 1, 1)

def render_row(board: list, y: int) -> str:
    """
    Render the specified row from the game board as a string and return the string. The row is specified by the y
    coordinate, where 0 is the top row. Cells are separated with pipes `|`. Each row ends with a new line.

    :param board: The current game board.
    :type board: A list of n lists containing n characters (strings) each.
    :param y: y coordinate/row number of the row to render.
    :type y: integer.
    :return: String representation of the contents of the row.
    :rtype: String.
    """



#test_board_2 = [[" ", "X"], ["O", " "]]
#assert " |X\n" == render_row(test_board_2, 0)
#assert "O| \n" == render_row(test_board_2, 1)
#test_board_3 = [["X", " ", "O"], [" ", "O", " "], ["O", " ", "X"]]
#assert "X| |O\n" == render_row(test_board_3, 0)
#assert " |O| \n" == render_row(test_board_3, 1)
#assert "O| |X\n" == render_row(test_board_3, 2)

def render_board(board: list) -> str:
    """
    Render the current game board as a string and return the string. The board will always be a square, and each cell
    is 3x3 characters. The cell, of occupied by a player, will have the player's symbol ('X' or 'O') in the centre of
    the 3x3 cell. Vertical lines are represented as pipe characters '|', horizontal lines are hyphen-minus '-', and
    intersections of vertical and horizontal lines are represented as addition signs '+'. An example 3x3 game board
    populated with player moves is presented below:

                X|O|X
                -+-+-
                O|X|O
                -+-+-
                X|O|X

    :param board: The current game board.
    :type board: A list of n lists containing n characters (strings) each.
    :return: String representation of the current game board state.
    :rtype: String.
    """



#one_one = "O\n"
#two_two = "X| \n" "-+-\n" " |X\n"
#three_three = "O| | \n" "-+-+-\n" " |O| \n" "-+-+-\n" " | |O\n"
#four_four = " | | |X\n" "-+-+-+-\n" " | |X| \n" "-+-+-+-\n" " |X| | \n" "-+-+-+-\n" "X| | | \n"
#assert one_one == render_board([["O"]])
#assert two_two == render_board([["X", " "], [" ", "X"]])
#assert three_three == render_board([["O", " ", " "], [" ", "O", " "], [" ", " ", "O"]])
#assert four_four == render_board(
#    [[" ", " ", " ", "X"], [" ", " ", "X", " "], [" ", "X", " ", " "], ["X", " ", " ", " "]]
#)

# Makes it so the import from the unit tests do not break things
if __name__ == "__main__":
    # Execution of Game
