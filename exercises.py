class Game():
  counter=0
  # board={
  #   'a1': None, 'b1': None, 'c1': None,
  #   'a2': None, 'b2': None, 'c2': None,
  #   'a3': None, 'b3': None, 'c3': None,
  #   }
      


  def __init__(self , tie=False , winner=False):

      self.turn="x"
      self.counter=0
      self.tie=False
      self.winner=False
      self.the_winner=""
      self.board=board={ 'a1': None, 'b1': None, 'c1': None,
    'a2': None, 'b2': None, 'c2': None,
    'a3': None, 'b3': None, 'c3': None,}
  



  def print_board(self):
    b = self.board
    print(f"""
          A   B   C
      1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
          ----------
      2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
          ----------
      3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
    """)

  def print_message(self):
    if self.counter==9 and self.winner==False:
      print("It's a tie!")

    if self.winner:
      print(f"{self.the_winner} wins!")
    
    if self.counter!=9 and self.winner==False:
      print(f"Player {self.turn} turn")
 
  def get_move(self):
    position = input("Enter position: ").lower()

    if self.board[position]!=None:
      print("choose available place")
      self.print_board()
      self.get_move()

    if self.board[position]==None:
      self.board[position]=self.turn
      self.counter+=1
      
      # self.next_turn()
      if self.turn=="x":
        self.turn="o"
      else:
        self.turn="x"

      self.print_board()
      self.check_winner()
      
     
      
     


  def play_game(self):
    # print("ready to play?")
    self.print_board()
    self.get_move()

  def check_winner(self):
     if self.winner==False:
        if self.board['a1'] == self.board['a2'] == self.board['a3'] != None:
          self.winner=True
          self.the_winner=self.board['a1']

        if self.board['b1'] == self.board['b2'] == self.board['b3'] != None:
          self.winner=True
          self.the_winner=self.board['b1']

        if self.board['c1'] == self.board['c2'] == self.board['c3'] != None:
          self.winner=True
          self.the_winner=self.board['c1']

        if self.board['a1'] == self.board['c1'] == self.board['b1'] != None:
          self.winner=True
          self.the_winner=self.board['c1'] 
        if self.board['a2'] == self.board['c2'] == self.board['b2'] != None:
          self.winner=True
          self.the_winner=self.board['c1'] 
        if self.board['a3'] == self.board['c3'] == self.board['b3'] != None:
          self.winner=True
          self.the_winner=self.board['c1'] 
        if self.board['a1'] == self.board['b2'] == self.board['c3'] != None:
          self.winner=True
          self.the_winner=self.board['c3']
        if self.board['a3'] == self.board['b2'] == self.board['c1'] != None:
          self.winner=True
          self.the_winner=self.board['c1']
        if self.winner==False and self.counter!=9:
          self.print_message()
          self.get_move()
     if self.winner==True or self.counter==9:
      self.print_message()
          
        

  
rick = Game()
rick.play_game()