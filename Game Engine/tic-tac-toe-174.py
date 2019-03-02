"""
Example Tic tac toe from cmput 174
Has cursors and drawing
"""

# Tic Tac Toe Version 3
# This program allows two players to play Tic Tac Toe.
# The X and Y player's take turns selecting empty tiles
# to fill on a 3x3 board. If a player selects three tiles
# in a row, a column or a diagonal, that player wins.
# If all the tiles are filled without a win, the game is
# a draw.
# This program requires two data files: cursorx.txt and
# cursoro.txt that contain string represenations of  two
# custom cursors used in the game.
#
# V1 implements only a single player 'X' who can select 
# tiles using a regular cursor. A tile flashes when an 
# occupied tile is selected, but there is no win or draw
# indication at the end. The game runs until the player 
# closes the window.


from uagame import Window
import pygame, time
from pygame.locals import *
import math, random

# User-defined functions

def main():

   window = Window('Tic Tac Toe', 500, 400)
   window.set_auto_update(False)   
   game = Game(window)
   game.play()
   window.close()

# User-defined classes

class Game:
   # An object in this class represents a complete game.

   def __init__(self, window):
      # Initialize a Game.
      # - self is the Game to initialize
      # - window is the uagame window object
      
      self.window = window
      Tile.set_window(window)
      self.bg_color = pygame.Color('black')
      self.pause_time = 0.01 # smaller is faster game
      self.close_clicked = False
      self.continue_game = True
      self.board_size = 3
      self.player_1 = 'X'
      self.player_2 = 'O'
      self.active_player = self.player_1
      self.number_of_occupied_tiles  = 0 
      self.flashers = []
      self.flasher_index = 0
      self.cursor_x = Cursor('cursorx.txt')
      self.cursor_o = Cursor('cursoro.txt')
      self.cursor_x.activate()
      self.board = []
      self.create_board()
      
   def create_board(self):
      # Create the game board.
      # - self is the Game whose board is created

      for row_index in range(0,  self.board_size):
         row = self.create_row(row_index) 
         self.board.append(row)
         
   def create_row(self, row_index):
      # Create one row of the board
      # - self is the Game whose board row is being created
      # - row_index is the int index of the row starting at 0

      row = []
      width = self.window.get_width() // self.board_size
      height = self.window.get_height() // self.board_size
      y = row_index * height
      for col_index in range(0,  self.board_size):
         x = col_index * width
         tile = Tile(x, y, width, height)
         row.append(tile)
      return row
      
   def play(self):
      # Play the game until the player presses the close box.
      # - self is the Game that should be continued or not.

      while not self.close_clicked:  # until player clicks close box
         # play frame
         self.handle_event()
         self.draw()            
         if self.continue_game:
            self.update()
            self.decide_continue()
         time.sleep(self.pause_time) # set game velocity by pausing

   def handle_event(self):
      # Handle each user event by changing the game state
      # appropriately.
      # - self is the Game whose events will be handled

      event = pygame.event.poll()
      if event.type == QUIT:
         self.close_clicked = True
      elif event.type == MOUSEBUTTONUP and self.continue_game:
         self.handle_mouse_up_event(event)
         
   def handle_mouse_up_event(self, event):
      # Respond to the player releasing the mouse button by
      # taking appropriate actions.
      # - self is the Game where the mouse up occurred.
      # - event is the pygame.event.Event object to handle

      for row in self.board: 
         for tile in row:
            valid_selection = tile.select(event.pos, self.active_player)
            if valid_selection:
               self.change_turn()
               self.number_of_occupied_tiles = self.number_of_occupied_tiles + 1
      
   def change_turn(self):
      if self.active_player == self.player_1:
         self.active_player = self.player_2
         self.cursor_o.activate()
      else:
         self.active_player = self.player_1
         self.cursor_o.activate()
      

   def draw(self):
      # Draw all game objects.
      # - self is the Game to draw
      
      self.window.clear()
      self.select_flasher()
      for row in self.board: 
         for tile in row:
            tile.draw()
      self.window.update()

   def update(self):
      # Update the game objects.
      # - self is the Game to update
      pass

         
   def decide_continue(self):
      # Check and remember if the game should continue
      # - self is the Game to check

      if self.is_win() or self.is_tie():
         self.continue_game = False
         self.pause_time = 0.03
     
   def is_tie(self):
      is_tie = self.number_of_occupied_tiles == self.board_size ** 2 #and not self.is_win() #<= not needed because of lazy evaluation of self.is_win() or self.is_tie() in decide_continue
      if is_tie:
         for row in self.board:
            for tile in row:
               self.flashers.append(tile)
      return is_tie
   
   def is_win(self):
      is_row_win = self.is_row_win() 
      is_column_win = self.is_column_win()
      is_diagonal_win = self.is_diagonal_win()
      return is_row_win or is_column_win or is_diagonal_win
   
   def is_row_win(self):
      row_win = False
      for row in self.board:
         if self.is_list_win(row):
            row_win = True
      return row_win
   
   def is_column_win(self):
      column_win = False
      for column_index in range(0, self.board_size):
         # collect tiles of this column as list
         column = []
         for row_index in range(0, self.board_size):
            tile = self.board[row_index][column_index]
            column.append(tile)
         if self.is_list_win(column):
            column_win = True
      return column_win
   
   def is_diagonal_win(self):
      diag_1 = []
      diag_2 = []
      for index in range(0, self.board_size):
            diag_1.append(self.board[index][index])
            diag_2.append(self.board[index][self.board_size - (index + 1)])
      diag_1_win = self.is_list_win(diag_1) 
      diag_2_win = self.is_list_win(diag_2)
      return diag_1_win or diag_2_win
            
   def is_list_win(self, tile_list):
      is_list_win = True
      tile_0 = tile_list[0]
      for tile in tile_list:
#         if not tile_0.is_equal(tile): #alternative without overloading ==
         if tile_0 != tile:         
            is_list_win = False
            
      if is_list_win:
            self.flashers.extend(tile_list)
         
      return is_list_win
   
   def select_flasher(self):
      if self.flashers != []:
         tile = self.flashers[self.flasher_index]
         tile.flash()
         self.flasher_index = (self.flasher_index + 1) % len(self.flashers)

class Tile:
   # An object in this class represents a Rectangular tile
   # that contains a string. A new tile contains an empty
   # string. A tile can be selected if the tile contains a
   # position. If an empty tile is selected its string can
   # be changed. If a non-empty tile is selected it will flash
   # the next time it is drawn. A tile can also be set to
   # flash forever. Two tiles are equal if they contain the
   # same non-empty string.


   # initialize the class attributes that are common to all tiles.
   fg_color = pygame.Color('white')
   border_width = 3
   font_size = 144
   window = None

   @classmethod
   def set_window(cls, window):
      # remember the window

      cls.window = window

   def __init__(self, x, y, width, height):
      # Initialize a tile to contain a ' '
      # - x is the int x coord of the upper left corner
      # - y is the int y coord of the upper left corner
      # - width is the int width of the tile
      # - height is the int height of the tile

      self.content = ''
      self.rectangle = pygame.Rect(x, y, width, height)
      self.flashing = False
      
#   def is_equal(self, other_tile):
#      return self.content == other_tile.content and self.content != ''

   def __eq__(self, other_tile):
      return self.content == other_tile.content and self.content != ''

      
   def select(self, mouse_position, player_symbol):
      # A position was selected. If the position is in the Tile
      # and the Tile is empty, then update the Tile content
      # - self is the Tile
      # - position is the selected location (tuple)
      # - new_content is the new str contents of the tile
      
      selected = False
      if self.rectangle.collidepoint(mouse_position):
         if self.content == '':
            self.content = player_symbol
            selected = True
         else:
            self.flashing = True
      return selected
      
            
   def draw(self):
      # Draw the Tile' content, and a rectangle border or flash it.
      # - self is the Tile

      if self.flashing:
         pygame.draw.rect(self.window.get_surface(), Tile.fg_color, self.rectangle)
         self.flashing = False
      else:
         self.draw_content()
         
   def draw_content(self):
         pygame.draw.rect(self.window.get_surface(), Tile.fg_color, self.rectangle, Tile.border_width)
         Tile.window.set_font_size(Tile.font_size)
         content_width = Tile.window.get_string_width(self.content)
         content_height = Tile.window.get_font_height()
         content_x = self.rectangle.left + (self.rectangle.width - content_width) // 2
         content_y = self.rectangle.top + (self.rectangle.height - content_height) // 2
         Tile.window.draw_string(self.content, content_x, content_y) 
      
   def flash(self):
      self.flashing = True


class Cursor:
   
   def __init__(self, filename):
      
         string_list = self.read_cursor_data(filename)
         self.size = (len(string_list[0]),len(string_list))
         self.hotspot = (self.size[0] // 2, self.size[1] // 2)
         compiled = pygame.cursors.compile(string_list, black='X', white='*', xor='o')
         self.xormasks = compiled[0]
         self.andmasks = compiled[1]
       

   def activate(self):
      pygame.mouse.set_cursor(self.size, self.hotspot, self.xormasks, self.andmasks)

   def read_cursor_data(self, filename):
      file = open(filename, 'r')
      string_list = []
      for line in file:
         string_list.append(line.strip('\n'))
      file.close()
      return string_list 
   
   ''' 
   Alternative implementations of the read_cursor_data method:
   ===========================================================
   
   def read_cursor_data(self, filename):
      file = open(filename, 'r')
      strings = file.read().splitlines()
      file.close()
      return strings
      
   def read_cursor_data(self, filename):
      file = open(filename, 'r')
      strings = file.readlines()
      for i in range(len(strings)):
         strings[i] = strings[i].strip('\n')
      file.close()
      return strings

   '''
   
main()
