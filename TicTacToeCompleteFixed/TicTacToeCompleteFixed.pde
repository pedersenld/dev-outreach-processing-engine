/*
1. switch rows and columns to get correct output
 2. gameover state was drawn so we need to add in user input ie. press r to reset
 3. gameover state for a tie needs to work
 4. counter needs fixing - reset each time that we set the board
 */



int numRows = 3;
int numCols = 3;
int[][] grid = new int [numRows][numCols];
int player = 1;
int totalRow = 0;
int totalCol = 0;
int counter = 0;
boolean gameOver = false;
boolean player1Wins = false;
boolean player2Wins = false;


void resetBoard()
{
  //reset gamestate
  textSize(12);
  player = 1;
  totalRow = 0;
  totalCol = 0;
  counter = 0;
  gameOver = false;
  player1Wins = false;
  player2Wins = false;

  //reset gameBoard
  for (int rows = 0; rows < numRows; rows++)
  {
    for (int cols = 0; cols < numCols; cols++)
    {
      grid[rows][cols] = 0;
    }
  }
}


void gameOver(int player)
{

  drawBoard();
  gameOver = true;

  fill(#FAA72B);
  textSize(32);
  if (player == 1)
  {
    text("Player 1 wins!", width/3, height/5);
  } else if (player == 2)
  {
    text("Player 2 wins!", width/3, height/5);
  } else 
  {
    text("Draw", width/3, height/5);
  }
  text("Press R to Reset and play again.", width/3, height/5+32);
}

void gameTurn()
{
  if (!gameOver) {
    if (grid[mouseY/int(height/numRows)][mouseX/int(width/numCols)]==0)
    {
      if (player == 1)
      {
        grid[mouseY/int(height/numRows)][mouseX/int(width/numCols)]=1;
        player = 2;
        counter++;
      } else if (player == 2)
      {
        grid[mouseY/int(height/numRows)][mouseX/int(width/numCols)]=2;
        player = 1;
        counter++;
      }
    }

    for (int rows = 0; rows < numRows; rows++)
    {
      for (int cols = 0; cols < numCols; cols++)
      {
        if (grid[rows][0]==1 && grid[rows][1]==1 && grid[rows][2]==1 ||grid[0][cols]==1 && grid[1][cols]==1 && grid[2][cols]==1 )
          player1Wins = true;
        else if (grid[rows][0]==2 && grid[rows][1]==2 && grid[rows][2]==2 ||grid[0][cols]==2 && grid[1][cols]==2 && grid[2][cols]==2 )
          player2Wins = true;
      }
    }
    if (player1Wins)
      gameOver(1);
    else if (player2Wins)
      gameOver(2);
    else if (grid[0][0]==1 && grid[1][1]==1 && grid[2][2]==1 ||grid[0][2]==1 && grid[1][1]==1 && grid[2][0]==1)
      gameOver(1);
    else if (grid[0][0]==2 && grid[1][1]==2 && grid[2][2]==2 ||grid[0][2]==2 && grid[1][1]==2 && grid[2][0]==2)
      gameOver(2);
    else if (counter >= 9)
      gameOver(0);
  }
}

void drawBoard()
{
  for (int rows = 0; rows < numRows; rows++)
  {
    for (int cols = 0; cols < numCols; cols++)
    {
      fill(255);
      rect ((width/numCols)*cols, rows*(height/numRows), width/numCols, height/numRows);
      textSize(height/numRows);
      fill(0);

      if (grid[rows][cols]==1)
        text("X", (width/numCols)*cols+width/18, (rows+1)*(height/numRows)-height/18);
      else if (grid[rows][cols]==2)
        text("O", (width/numCols)*cols+width/18, (rows+1)*(height/numRows)-height/18);



      textSize(12);
      text(new String("Row: " + rows + " Col: " + cols), (width/numCols)*cols, rows*(height/numRows)+height/numRows);
    }
  }
}

void setup() {
  size(900, 900);
  background(204);
  resetBoard();
}

void draw()
{
  if (!gameOver)
    drawBoard();
}


void mouseClicked()
{
  gameTurn();
}

void keyPressed()
{
  if (key=='r')
    resetBoard();
}