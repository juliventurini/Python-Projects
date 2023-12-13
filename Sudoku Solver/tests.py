from sudoku_solver import valid, BoardInvalidError
import pytest

b = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

b_null = None
b_non_regulation_size = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
]


# Value Invalid
def test_value_lower_than_1():
    assert valid(b,0,(0,2)) == False

def test_value_higher_than_9():
    assert valid(b,10,(0,2)) == False

def test_value_is_negative():
    assert valid(b,-1,(0,2)) == False


# Position Out Of Bounds
def test_position_out_of_bounds_left():
    assert valid(b,3,(0,-1)) == False

def test_position_out_of_bounds_right():
    assert valid(b,3,(0,9)) == False

def test_position_out_of_bounds_top():
    assert valid(b,3,(-1,0)) == False

def test_position_out_of_bounds_bottom():
    assert valid(b,3,(9,0)) == False


# Invalid Board
def test_board_null():
    with pytest.raises(BoardInvalidError):
        valid(b_null,3,(0,2))

def test_board_not_regulation_sized():
    with pytest.raises(BoardInvalidError):
        valid(b_non_regulation_size,3,(0,2))


# Valid Value And Position Within Bounds
def test_value_not_repeated():
    assert valid(b,3,(0,2)) == True

def test_value_already_in_subsquare_only():
    assert valid(b,4,(4,5)) == False

def test_value_already_in_row_only():
    assert valid(b,1,(7,3)) == False

def test_value_already_in_column_only():
    assert valid(b,1,(5,6)) == False

