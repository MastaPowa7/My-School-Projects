//append your last name to the class name, and saveAs the file as the same thing
class MethodProj {
    
   //reverse the order of the elements
   public static void reverse(int x[]){
      for(int i = 0; i < (x.length / 2); ++i){
         int temp = x[i];
         x[i] = x[(x.length - 1) - i];
         x[(x.length - 1) - i] = temp;
      }
   }
    
   //print the array
   public static void printit(int x[], String s){
      System.out.print("Here are the numbers in the array");
      if (!s.equals("")){
         System.out.print(" (" + s + "):\n");
      }
      else{
         System.out.print(":\n");
      }
      
      for (int i = 0; i < x.length; i++){
         System.out.print(x[i]);
         if (i + 1 < x.length){
            System.out.print(", ");
         }
      }
      System.out.print("\n");
   }
    
    //randomize() method will fill in elements with random numbers from 10 - 99
   public static void randomize(int x[]){
    for (int i = 0; i < x.length; i++){
         x[i] = (int)(Math.random() * (99 - 10 + 1) + 10);
      }   
   }
   
   //returns the sum of all numbers in the array
   static int sum(int x[]){
      int t = 0;
      for (int i = 0; i < x.length; i++){
         t += x[i];
         }
      return t;
   }
   
   //returns the average of all numbers in the array
   static double average(int x[]){
      double t = 0;
      for (int i = 0; i < x.length; i++){
         t += x[i];
      }
      return t / x.length;
   }
   
   //finds the largest number in the array
   static int findMax(int x[]){
      int m = 0;
      for (int i = 0; i < x.length; i++){
         if (x[i] > m){
            m = x[i];
         }
      }
      return m;
   }
   
   //finds the lowest number in the array
   static int findMin(int x[]){
      int m = 100;
      for (int i = 0; i < x.length; i++){
         if (x[i] < m){
            m = x[i];
         }
      }
      return m;
   }
   
   //obtains the average of all even numbers in the array
   static double avgEvens(int x[]){
      double t = 0;
      int e = 0;
      for (int i = 0; i < x.length; i++){
         if (x[i] % 2 == 0){
            t += x[i];
            e += 1;
         }
      }
      return t / e;
   }

   public static void main(String[] args) {
      int [] mainArray = new int [10];
     
     //populate with random numbers by calling the method
      randomize(mainArray);
     
     //display the random numbers by calling the method
      printit(mainArray, "");
     
     //reverse the array element order
      reverse(mainArray);
     
     //display the random numbers by calling the method
      printit(mainArray, "reversed");
               
     //display the final result
      printit(mainArray, "final result");
      
      //you need to create each of the below methods called from the print statement, outside of the main
      System.out.println("\nSum: " + sum(mainArray));
      
      System.out.println("Average: " + average(mainArray));
      
      System.out.println("Largest: " + findMax(mainArray));
      
      System.out.println("Smallest: " + findMin(mainArray));
      
      System.out.println("Average of Evens: " + avgEvens(mainArray));
   }
}