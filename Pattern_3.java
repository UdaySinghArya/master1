public class Pattern_3 {
    public static void main(String []args){
        for(int r=0;r<5;r++){
            char ch='A';
            for(int c=0;c<5;c++){
                if(c>=r){
                    System.out.print(ch);
                    ch++;
                }
                else{
                    System.out.print(" ");
                }
            }
            System.out.println("");
        }
    }
}
