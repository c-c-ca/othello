def in_bounds(board, row, col):
  return 0 <= row < len(board) and 0 <= col < len(board[0])


def is_empty_cell(board, row, col):
  return board[row][col] == ''


def is_adjacent(x1, y1, x2, y2):
  return abs(x2 - x1) <= 1 and abs(y2 - y1) <= 1


def is_same_turn(board, turn, row, col):
  return board[row][col] == turn


def contains_match(board, turn, row, col, dx, dy):
  def find_match(curr_row, curr_col):
    if not in_bounds(board, curr_row, curr_col) or \
      is_empty_cell(board, curr_row, curr_col):
      return False

    if not is_adjacent(row, col, curr_row, curr_col) and \
      is_same_turn(board, turn, curr_row, curr_col): 
      return True

    return find_match(curr_row + dy, curr_col + dx)

  return find_match(row + dy, col + dx)


def othello(board, turn, row, col):
  """
  Returns a `bool` indicating whether adding a piece for the given `turn` at the
  specified `row` and `col` represents a legal move on the `board`.
  """
  if not is_empty_cell(board, row, col):
    return False

  for dx in range(-1, 2):
    for dy in range(-1, 2):
      if dx == 0 and dy == 0:
        continue
      if contains_match(board, turn, row, col, dx, dy):
        return True
        
  return False


board = [[ '',  '',  '',  '',  '',  '',  '',  ''],
         [ '',  '',  '',  '',  '',  '',  '',  ''],
         [ '',  '', 'B', 'B', 'B',  '',  '',  ''],
         [ '', 'W', 'B', 'W', 'W',  '', 'B',  ''],
         [ '', 'W', 'B', 'W', 'W', 'W', 'W',  ''],
         [ '',  '', 'W', 'W', 'W',  '',  '',  ''],
         [ '',  '',  '', 'W',  '',  '',  '',  ''],
         [ '',  '',  '',  '',  '',  '',  '',  '']]
         
board2 = [[ 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
          [ 'B', 'W', 'B', 'W', 'B', 'B', 'W', 'B'],
          [ 'B', 'B', 'W', 'W', 'B', 'B', 'B', 'B'],
          [ 'B', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
          [ 'W', 'W', 'W', 'W', 'W', 'W', 'B', 'B'],
          [ 'B', 'B', 'W', 'W', 'W', 'B', 'B', 'W'],
          [ 'B', 'B', 'W', 'B', 'B', 'B', 'W', 'W'],
          [ 'B', 'B', 'W', 'B', 'B', 'B', 'W', 'W']]
          
print(othello(board, 'W', 1, 1))