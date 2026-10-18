class MyTime{

   public static void main(String[] args) {
      //creates 3 different time variables using the created class, then prints the hours, minutes, and seconds to create an HH:MM:SS format
       MyTime time1 = new MyTime();
       System.out.println(time1.getHour() + ":" +
         time1.getMinute() + ":" + time1.getSecond());
   
       MyTime time2 = new MyTime(555550000);
       System.out.println(time2.getHour() + ":" +
         time2.getMinute() + ":" + time2.getSecond());
   
       MyTime time3 = new MyTime(5, 23, 55);
       System.out.println(time3.getHour() + ":" +
         time3.getMinute() + ":" + time3.getSecond());
   }

}