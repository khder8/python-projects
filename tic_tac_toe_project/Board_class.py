class Board_class :

    def __init__(self):
     self.board=[f'{x}' for x in range(1,10)]



    def display_board(self):
     board_status=f"""
    {self.board[0]}-{self.board[1]}-{self.board[2]}
    {self.board[3]}-{self.board[4]}-{self.board[5]}
    {self.board[6]}-{self.board[7]}-{self.board[8]}
 """
     print(board_status)

    def reset_board(self):
      self.board=[f'{x}' for x in range(1,10)]

    def update_board(self,index,symbol):
      
      if self.board[int(index)-1].isdigit():
         self.board[int(index)-1]=symbol
         return True
      return False



      