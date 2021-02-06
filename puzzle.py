"""
Tim Kozak, UCU IT&BA, Lab0
GitHub link: https://github.com/TimKozak/Lab0_Task2.git
"""


def validate_cell(board: list, row_idx: int, col_idx: int, visited: set) -> bool:
    """
    Check if cell is absent in a given set. 
    Add it in set and return True if yes.

    >>> validate_cell(["**** ****", "***1 ****", "**  3****", "* 4 1****", \
        "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"], 1, 1, {'0'})
    True
    """
    if board[row_idx][col_idx] in ('*', ' '):
        return True

    if board[row_idx][col_idx] in visited:
        return False

    visited.add(board[row_idx][col_idx])

    return True


def validate_row(board: list, row_idx: int) -> bool:
    """
    Check if row is valid.
    Return True if yes.

    >>> validate_row(["**** ****", "***1 ****", "**  3****", "* 4 1****", \
        "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"], 1)
    True
    """
    visited = set()

    for col_idx in range(9):

        if not validate_cell(board, row_idx, col_idx, visited):
            return False

    return True


def validate_column(board: list, col_idx: int) -> bool:
    """
    Check if column is valid.
    Retturn True if yes.

    >>> validate_column(["**** ****", "***1 ****", "**  3****", "* 4 1****", \
        "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"], 1)
    True
    """
    visited = set()

    for row_idx in range(9):

        if not validate_cell(board, row_idx, col_idx, visited):
            return False

    return True


def check_corner(board: list, diagonal_idx: int) -> bool:
    """
    Check if every corner of one color is valid.
    Return True if yes.

    >>> check_corner(["**** ****", "***1 ****", "**  3****", "* 4 1****", \
        "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"], 1)
    True
    """
    visited = set()

    for idx in range(9 - diagonal_idx):

        if not validate_cell(board, idx, diagonal_idx, visited):
            return False

    for idx in range(8 - diagonal_idx):

        if not validate_cell(board, 8 - diagonal_idx, 8 - idx, visited):
            return False

    return True


def validate_board(board: list) -> bool:
    """
    Check if every row, column and corner is valid.
    Return True if yes.

    >>> validate_board(["**** ****", "***1 ****", "**  3****", "* 4 1****", \
        "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    """
    for idx in range(9):

        if not (
            validate_row(board, idx) and
            validate_column(board, idx) and
            check_corner(board, idx)
        ):

            return False

    return True


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())

    print(validate_board([
        "**** ****",
        "***1 ****",
        "**  3****",
        "* 4 1****",
        "     9 5 ",
        " 6  83  *",
        "3   1  **",
        "  8  2***",
        "  2  ****"
    ]))
