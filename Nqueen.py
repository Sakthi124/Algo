class QueenChessBoard: 

 def init(self, size): 

 self.size = size 

 self.columns = [] 

 def place_in_next_row(self, column): 

 self.columns.append(column) 

 def remove_in_current_row(self): 

 return self.columns.pop() 

 def is_this_column_safe_in_next_row(self, column): 

 row = len(self.columns) 

 for queen_column in self.columns: 

 if column == queen_column: 

 return False 

 for queen_row, queen_column in enumerate(self.columns): 

 if queen_column - queen_row == column - row: 

 return False 

 for queen_row, queen_column in enumerate(self.columns): 

 if (self.size - queen_column) - queen_row == (self.size - column) - row: 

 return False 

 return True 

 def display(self): 

 for row in range(self.size): 

 for column in range(self.size): 

 if column == self.columns[row]: 

 print('Q', end='') 

 else: 

 print('.', end=' ') 
 print() 

def solve_queen(size): 

 board = QueenChessBoard(size) 

 number_of_solutions = 0 

 row = 0 

 column = 0 

 while True: 

 while column < size: 

 if board.is_this_column_safe_in_next_row(column): 

 board.place_in_next_row(column) 

 row += 1 

 column = 0 

 break 

 else: 

 column += 1 

 if column == size or row == size: 

 if row == size: 

 board.display() 

 print() 

 number_of_solutions += 1 

 try: 

 prev_column = board.remove_in_current_row() # remove last placed queen

 row -= 1 

 column = prev_column + 1 # try next column in this row

 except IndexError: 

 break # done, no more rows to backtrack

 return number_of_solutions 
n = int(input('Enter n: ')) 

print('Number of solutions:', solve_queen(n))
