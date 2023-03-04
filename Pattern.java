public class Pattern {
    public static void main(String []args){
        for(int r=0;r<5;r++){
            int n=1;
            for(int c=0;c<5;c++){
                if(c<=r){

                    System.out.print(n);
                    n=n+1;
                }
                else{
                    System.out.print(" ");
                }
            }
            System.out.println("");
        }
    }
}
