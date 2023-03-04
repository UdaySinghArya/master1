public class Pattern_2 {
    public static void main(String []args){
        for(int r=0;r<5;r++){
            int n=r+1;
            for(int c=0;c<5;c++){
                if(c<=r){
//                    n=n-1;
                    System.out.print(n);
                    n=n-1;
                }
                else{
                    System.out.print(" ");
                }
            }
//            n=n+1;
            System.out.println("");
        }
    }
}
