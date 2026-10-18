import java.io.*;

class classArray {
    public static void main(String[] args) {
        //creates an empty array of 100 and uses a method to fill the indexes with ranodm numbers
        int[] array = new int[100];
        array = fillArray(array);
        
        //declares a variable whos value is given from meanArray method
        double mean = meanArray(array);
        
        //prints what the mean is, then uses a for loop to figure out which values (and their index) are above the mean
        System.out.println("The mean of the array is " + mean + ". The following numbers from the array are above the mean:");
        int total = 0;
        
        for (int i = 0; i < array.length; i++){
         if (array[i] > mean){
            System.out.print("[" + i + "]" + array[i] + " ");
            total += 1;
         }
        }
        System.out.println("\nTotal values: " + total);
        

    }
    
    //fills the loop up with random numbers from 0-100, then returns the array
    static int[] fillArray(int[] array){
      for (int i = 0; i < array.length; i++){
         array[i] = (int)(Math.random() * 101);
      }
 
      return array;
    }
    
    //used to obtain the mean of an array, then returns the result
    static double meanArray(int[] array){
      double mean = 0;
      for (int i = 0; i < array.length; i++){
         mean += array[i];
      }
      
      return mean/array.length;
    
    }
}