import java.util.Scanner;

public class Final_Project {
     //global variables
     static public int currentTurn = 0; //0 = CPU, 1 = Player
     static int userAmount = 0;
     static boolean activeGame = false;

     //chili variables
     static int chocolate = 0;

     //nim variables
     static int[] lane = new int[5];
     static int userRow = 0;		



     //tutorial for how to play Chili Pepper
     static public void chiliTutorial(){
     System.out.print("====\nHow to play:\n- There is a bucket containing 13 chocolates and a chili pepper. Players can take 1-3 chocolates each turn.\n- The player left with the chili pepper loses!\n");
     }

    //tutorial for how to play Nim 
    static public void nimTutorial(){
     System.out.print("====\nHow to play:\n- There are 5 lanes of pieces, and each lane has that number of pieces on it (i.e. lane 5 = 5 pieces, lane 4 = 4 pieces, etc). \"O\" means the piece is available and \"X\" means the piece is taken.\n- Players will take turns taking pieces, each having to take at least 1 piece.\n- The player forced to take the last piece loses!\n");
    }


    //used to display whos turn it is
    static public void turnDisplay(){
     String playerName = (currentTurn == 0) ? "CPU" : "PLAYER";
     System.out.print("\nCurrent turn: " + playerName + "\n");
    }







    //starts up the Chili Pepper game
    static public void chili_Initialize(){
     chocolate = 13;
     currentTurn = 0;
     activeGame = true;
    }

    //simply askes the player how many chocolates they want to take. If there are no more chocolates left, the game ends
    static public void chili_playerTurn(Scanner scan){
     turnDisplay();
     System.out.print("Current number of chocolates: " + chocolate + "\n");
     if (chocolate == 0){
          System.out.print("Game over. The CPU has won!");
          activeGame = false;
          return;
     }

     System.out.print("How many do you want to take: ");
     while(true){
          userAmount = scan.nextInt();
          if (userAmount > 0 && userAmount < 4 && userAmount < chocolate){
               chocolate -= userAmount;
               break;
          }
          else{
               System.out.print("Invalid amount. Select a new amount: ");
               continue;
          }
     }
     currentTurn = 0;
    }

    //the CPU uses modulos math to figure out how many pieces to take
    static public void chili_cpuTurn(){
     turnDisplay();
     System.out.print("Current number of chocolates: " + chocolate + "\n");
     String amount = (chocolate % 4 != 1) ? "s" : "";
     System.out.print("The CPU has taken " + (chocolate % 4) + " chocolate" + amount + "\n");
     chocolate -= chocolate % 4;
     currentTurn = 1;
    }










     //Starts up the Nim game
     static public void nim_Initialize(){
          for (int i = 0; i < lane.length; i++){
               lane[i] = i + 1;
          }
          currentTurn = 0;
          activeGame = true;
     }


     static public void nim_updateBoard(){
          //prints and updates the game board to the console
		for(int i = 0; i < lane.length; i++){
			System.out.print("\nLane " + (i + 1) + ": ");
			
			for(int j = 0; j < lane[i]; j++){
				System.out.print("O ");
			}
			
			for(int j = 0; j < (i + 1) - lane[i]; j++){
				System.out.print("X ");
			}
		}
          turnDisplay();

          //keeps track of how many total pieces there are on the board. If exactly one is left, the game ends
          int pieces = 0;
          for (int i : lane){
               pieces += i;
          }
          if (pieces <= 1){
               System.out.print("Game over. The CPU wins!");
               activeGame = false;
          }

     }


     static public void nim_playerTurn(Scanner scan){
          nim_updateBoard();
          if (!activeGame){
               return;
          }

		//asks user to choose a valid row
		while(true){
			System.out.print("\nChoose a row: ");
			userRow = scan.nextInt();
			if (userRow > 0 && userRow < 6 && lane[userRow - 1] != 0){
				break;
			}
			else{
				System.out.println("Invalid");
				continue;
			}
		}

		//asks user to choose how many pieces to take from that row. At least 1 must be taken
		while(true){
			System.out.print("\nHow many pieces do you want to take: ");	
			userAmount = scan.nextInt();
			if (userAmount > 0 && userAmount <= lane[userRow - 1]){
				lane[userRow - 1] -= userAmount;
				break;
			}
			else{
				System.out.println("Invalid");
				continue;
			}
		}
          currentTurn = 0;
	}


     static public void nim_cpuTurn(){
		int[] rowA = {0,0,0,0,0}; //binary 4s
		int[] rowB = {0,0,0,0,0}; //binary 2s
		int[] rowC = {0,0,0,0,0}; //binary 1s
		
          //converts the values in the lane array into 3 digit binary
		for(int i = 0; i < lane.length; i++){
			int temp = lane[i];
			
			rowC[i] = temp % 2;
			temp /= 2;
			
			rowB[i] = temp % 2;
			temp /= 2;
			
			rowA[i] = temp % 2;
		}


          //gets the sum of each row
          int totalA = 0;
          int totalB = 0;
          int totalC = 0;

          for (int i : rowA){
               totalA += i;
          }
          for (int i : rowB){
               totalB += i;
          }
          for (int i : rowC){
               totalC += i;
          }
          

          //checks to see which row is broken by checking if the sum of the row is odd
          boolean[] brokenRow = {false,false,false};
          brokenRow[0] = (totalA % 2 != 0) ? true : false;
          brokenRow[1] = (totalB % 2 != 0) ? true : false;
          brokenRow[2] = (totalC % 2 != 0) ? true : false;


          //starting from the highest broken digit, the for loops looks for the first instance of a "1." It will then lock into that specific column
          int targetColumn = 0;
          for(int i = 0; i < lane.length; i++){
               if (brokenRow[0] && rowA[i] == 1){
                    targetColumn = i;
                    break;
               }
               else if (brokenRow[1] && rowB[i] == 1){
                    targetColumn = i;
                    break;
               }
               else if (brokenRow[2] && rowC[i] == 1){
                    targetColumn = i;
                    break;
               }

          }


          //fixes the targeted column by swapping the values of the broken rows and increases binarySum if the digit is a "1"
          int binarySum = 0;
          if(brokenRow[0]){
               if (rowA[targetColumn] == 1){
                    rowA[targetColumn] = 0;
               }
          }
          if(brokenRow[1]){
               if (rowB[targetColumn] == 1){
                    rowB[targetColumn] = 0;
               }
               else{
                    rowB[targetColumn] = 1;
               }
          }
          if(brokenRow[2]){
               if (rowC[targetColumn] == 1){
                    rowC[targetColumn] = 0;
               }
               else{
                    rowC[targetColumn] = 1;
               }
          }

          if(rowA[targetColumn] == 1){
               binarySum += 4;
          }
          if(rowB[targetColumn] == 1){
               binarySum += 2;
          }
          if(rowC[targetColumn] == 1){
               binarySum += 1;
          }


          //updates lane to reflect how many pieces were taken
          lane[targetColumn] = binarySum;
          currentTurn = 1;
	}
}