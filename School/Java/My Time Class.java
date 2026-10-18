public class MyTime{
   private int hour;
   private int minute;
   private int second;
   
   //constructors that build different times based on the arugments received
   MyTime(){
      this(System.currentTimeMillis());
   }
   
   MyTime(long ms){
      setTime(ms);
   }
   
   MyTime(int hour, int minute, int second){
      this.hour = hour;
      this.minute = minute;
      this.second = second;
   }
   
   //getters that return the object's hour, minute, and second
   int getHour(){
      return this.hour;
   }
   
   int getMinute(){
      return this.minute;
   }
   
   int getSecond(){
      return this.second;
   }
   
   //sets the hour, minutes, and seconds from an elasped time
   void setTime(long elaspedTime){
      long seconds = elaspedTime / 1000;
      long minutes = seconds / 60;
      long hours = minutes / 60;
      
      this.second = (int)(seconds % 60);
      this.minute = (int)(minutes % 60);
      this.hour = (int)(hours % 24);
   }

}