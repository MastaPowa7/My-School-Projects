import java.util.Scanner;

class Final_Project_Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        //askes user if they want to play. Waits for a valid input, then either boots the game select menu or exits the program
        System.out.print("Do you want to play? (y/n) ");
        while (true) {
            String userInput = scan.nextLine();
            if(userInput.equals("y")){
                selectGame(scan);
                break;
            }
            else if(userInput.equals("n")){
                System.out.print("Exiting...");
                System.exit(0);
            }
            else{
                System.out.print("\nEnter a valid option: ");
                continue;
            }     
        }

    }

    //menu to select game. Waits for a valid input. The second version is for if when the user chooses the same game again
    static void selectGame(Scanner scan){
        System.out.print("Select a game (Chili Pepper: 1 // Nim: 2) ");
        while(true){
            int userInput = scan.nextInt();
            switch(userInput){
                case 1:
                    chiliPepperGameMenu(scan);
                    break;
                case 2:
                    nimGameMenu(scan);
                    break;
                default:
                    System.out.print("\nSelect a game to play: ");
                    continue;
            }
        }
    }

    static void selectGame(Scanner scan, int currentGame){
        switch(currentGame){
            case 0:
                chiliPepperGameMenu(scan);
            case 1:
                nimGameMenu(scan);
        }
    }

    //main menu for Chili Pepper
    static void chiliPepperGameMenu(Scanner scan){
       System.out.print("\nCurrent game: Chili Pepper\nStart game (1) // How to play (2) ");
        while(true){
            int userInput = scan.nextInt();
            switch(userInput){
                case 1:
                    chiliPepperGame(scan);
                    break;
                case 2:
                    Final_Project.chiliTutorial();
                    System.out.print("\nStart game (1) // How to play (2) ");
                    break;
                default:
                    System.out.print("\nChoose an option: ");
                    break;
            }
        }
    }

    //logic for the Chili Pepper game is in the Final Project class. This controls the turns and status of the game
    static void chiliPepperGame(Scanner scan){
        Final_Project.chili_Initialize();
        
        while(Final_Project.activeGame){
            switch(Final_Project.currentTurn){
                case 0:
                    Final_Project.chili_cpuTurn();
                    break;
                case 1:
                    Final_Project.chili_playerTurn(scan);
                    break;
            }
        }
        playAgainScreen(scan, 0);
    }


    //main menu for Nim
    static void nimGameMenu(Scanner scan){
        System.out.print("\nCurrent game: Nim\nStart game (1) // How to play (2) ");
        while(true){
            int userInput = scan.nextInt();
            switch(userInput){
                case 1:
                    nimGame(scan);
                case 2:
                    Final_Project.nimTutorial();
                    System.out.print("\nStart game (1) // How to play (2) ");
                    break;
                default:
                    System.out.print("\nChoose an option: ");
                    break;
            }
        }
    }

    //logic for the Nim game is in the Final Project class. This controls the turns and status of the game
    static void nimGame(Scanner scan){
        Final_Project.nim_Initialize();
        
        while(Final_Project.activeGame){
            switch(Final_Project.currentTurn){
                case 0:
                    Final_Project.nim_cpuTurn();
                    break;
                case 1:
                    Final_Project.nim_playerTurn(scan);
                    break;
            }
        }
        playAgainScreen(scan, 1);
    }

    //askes user if they'd like to play again, select a different game, or exit
    static void playAgainScreen(Scanner scan, int currentGame){
        System.out.print("\n\nChoose your selection: \nPlay again (1)\nSelect a different game (2)\nExit program (3)\n");

        while(true){
            int userInput = scan.nextInt();
            switch(userInput){
                case 1:
                    selectGame(scan, currentGame);
                    break;
                case 2:
                    selectGame(scan);
                    break;
                case 3:
                    System.out.print("Exiting...\n");
                    System.exit(0);
                    break;
                default:
                    System.out.print("Select a valid option: \n");
                    continue;
            }
        }
    }

}