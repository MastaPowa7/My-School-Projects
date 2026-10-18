import java.io.*;
import java.util.Scanner;

class Methods {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        //asks the user for 2 numbers
        System.out.print("Enter the first number: ");
        int valueA = scan.nextInt();
        
        System.out.print("Enter the second number: ");
        int valueB = scan.nextInt();
        
        //calls the max function
        max(valueA, valueB);
        
        //calls the single argument rndIncrease function and compares its value with the original number
        rndIncrease(valueA);
        System.out.println("Original number: " + valueA);
        
        //creates a variable which stores the result from the double argument rndIncrease function and compares its value with the combined value of the original numbers
        int valueC = rndIncrease(valueA, valueB);
        System.out.println("\nCombined number: " + valueC + "\nOriginal number: " + (valueA + valueB));
    }
  
    static void max(int a, int b){
      String result = (a > b) ? "1st" : "2nd";
      
      //if the 2 values are equal, prints both are equal and exits the function, otherwise it prints which's bigger
      if (a == b){
         System.out.println("\nBoth numbers are equal.");
         return;
      }
      System.out.println("\nThe " + result + " number is greater.");
    }
    
    static void rndIncrease(int a){
      //uses a single print statement to print the random number    
      System.out.println("\nRandom number: " + (a += (int)(Math.random() * a)));
    }
    
    static int rndIncrease(int a, int b){
    //simply returns the combined values of a and b
    return a + b;
    }
}