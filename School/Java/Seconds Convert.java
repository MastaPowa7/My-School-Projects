import java.util.Scanner;

class SecondsConv {
  
    //converts the seconds into HH:MM:SS and prints the result
     public static void realTime(int secs){
       int hours = secs / 3600;
       int minutes = (secs % 3600) / 60;
       int seconds = secs % 60;
       
       System.out.print("Hours: " + hours + "\nMinutes: " + (minutes) + "\nSeconds: " + seconds);
     }
    
    //accept the number of seconds from a user and pass that data to the realTime method
    public static void main(String[] args) {
    
      Scanner scan = new Scanner(System.in);
      
      System.out.print("Enter the number of seconds: ");
         int seconds = scan.nextInt();
         
      realTime(seconds);
    }
}