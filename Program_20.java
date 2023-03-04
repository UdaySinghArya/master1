/* Check whether a number is divisible by 5 or 7 or not */
public class Program_20 {
    public static void main(String[]args){
        int n=99;
        if(n%5==0)
        {
            System.out.println("It is divisible by 5");
        }
        else if(n%7==0)
        {
            System.out.println("It is divisible by 7");
        }

        else
        {
            System.out.println("It is not divisible by 5 and 7");
        }
    }
}
