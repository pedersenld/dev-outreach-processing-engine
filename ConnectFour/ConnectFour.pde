/*
1. switch rows and columns to get correct output
 2. gameover state was drawn so we need to add in user input ie. press r to reset
 3. gameover state for a tie needs to work
 4. counter needs fixing - reset each time that we set the board
 */



int numRows = 6;
int numCols = 7;
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
  int rowSelect = mouseY/int(height/numRows);
  int colSelect = mouseX/int(width/numCols);
  if (!gameOver) {
    while ( rowSelect+1<(numRows) &&  grid[rowSelect+1][colSelect] == 0  )
    {
      //if()
      rowSelect++;
    }

    if (grid[rowSelect][colSelect] == 0 && player == 1)
    {
      grid[rowSelect][colSelect]=1;
      player = 2;
      counter++;
    } else if (grid[rowSelect][colSelect] == 0 && player == 2)
    {
      grid[rowSelect][colSelect]=2;
      player = 1;
      counter++;
    }


    for (int i = 0; i < numCols; i++)
    {
      for (int rows = 0; rows < numRows; rows++)
      {
        for (int cols = 0; cols < numCols; cols++)
        {
          if (i+3<numRows )
          {
            if (grid[i][cols]==1 && grid[i+1][cols]==1 && grid[i+2][cols]==1 && grid[i+3][cols]==1)
              player1Wins = true;
            else if (grid[i][cols]==2 && grid[i+1][cols]==2 && grid[i+2][cols]==2 && grid[i+3][cols]==2)
              player2Wins = true;
          } else if (i+3<numCols )
          {
            if (grid[rows][i]==1 && grid[rows][i+1]==1 && grid[rows][i+2]==1 && grid[rows][i+3]==1 || grid[rows][i]==1 && grid[rows-1][i+1]==1 && grid[rows-2][i+2]==1 && grid[rows-3][i+3]==1 || grid[rows][i]==1 && grid[rows-1][i-1]==1 && grid[rows-2][i-2]==1 && grid[rows-3][i-3]==1)
              player1Wins = true;
            else if (grid[rows][i]==2 && grid[rows][i+1]==2 && grid[rows][i+2]==2 && grid[rows][i+3]==2)
              player2Wins = true;
          } else if (i-3>0)
          {
            if (grid[rows][i]==1 && grid[rows][i-1]==1 && grid[rows][i-2]==1 && grid[rows][i-3]==1)
              player1Wins = true;
            else if (grid[rows][i]==2 && grid[rows][i-1]==2 && grid[rows][i-2]==2 && grid[rows][i-3]==2)
              player2Wins = true;
          } 
          //else if (grid[i][i]==1 && grid[i+1][i+1]==1 && grid[i+2][i+2]==1 && grid[i+3][i+3]==1) //to fix //||grid[i][i+3]==1 && grid[i][i+2]==1 && grid[i+1][i+1]==1 && grid[i+2][i]==1)
          //player1Wins = true;
          //else if (grid[0][0]==2 && grid[1][1]==2 && grid[2][2]==2 ||grid[0][2]==2 && grid[1][1]==2 && grid[2][0]==2)
          //player2Wins = true;
        }
      }




      if (player1Wins)
        gameOver(1);
      else if (player2Wins)
        gameOver(2);
      else if (counter >= (numRows*numCols))
        gameOver(0);
    }
  }
}

void drawBoard()
{
  for (int rows = 0; rows < numRows; rows++)
  {
    for (int cols = 0; cols < numCols; cols++)
    {
      fill(#FFFF00);
      rect ((width/numCols)*cols, rows*(height/numRows), width/numCols, height/numRows);
      fill(0);
      ellipse((width/numCols)*cols+(width/numCols/2), rows*(height/numRows)+(height/numRows/2), width/numCols, height/numRows);
      textSize(height/numRows);
      //fill(0);

      if (grid[rows][cols]==1)
        fill(255, 0, 0);
        //text("X", (width/numCols)*cols, (rows+1)*(height/numRows));
      else if (grid[rows][cols]==2)
        fill(0, 255, 0);
        //text("O", (width/numCols)*cols, (rows+1)*(height/numRows));
      
      ellipse((width/numCols)*cols+(width/numCols/2), rows*(height/numRows)+(height/numRows/2), width/numCols, height/numRows);


      textSize(12);
      //text(new String("Row: " + rows + " Col: " + cols), (width/numCols)*cols, rows*(height/numRows)+height/numRows);
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