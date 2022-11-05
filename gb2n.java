
import java.util.Scanner;

public class ex_back_n {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        System.out.println("Enter the number of frames");
        int frame = in.nextInt();
        System.out.println("Enter the bits in the seq ");
        int k = in.nextInt();
        
        int send_win =(int)(Math.pow(2,k)-1);
        System.out.println(send_win);
        int arr[]=new int[frame];
        int j=0;
        for(int i=0;i<frame;i++){
            if(j<=send_win){
                arr[i] = j;
                j++;
            }
            else{
                j=0;
                arr[i]=j;
                j++;
            }
        }
        

        for(int i=0;i<frame;i++){
            System.out.print(arr[i]+" ");
        }
        System.out.println();
        int n = 0;
        int n1=0;
        int cnt = 0;
        int pos =0;
        for(int i=0;i<frame;i++){
            int random = (int)(Math.random()*10);
            // System.out.println("random "+random);
            // System.out.println("I:"+i);
            if(pos<send_win){
                if(random<8){
                    cnt++;
                    n1=arr[i];
                    System.out.println("ACK "+arr[i]);
                }
                pos++;
            }
            else{
                // System.out.println(cnt+" "+send_win);
                if(cnt == send_win ){
                    System.out.println("All packets recieved");

                    n=i;
                    i=n-1;
                    System.out.println("New value of n:"+(n));
                }
                else{
                    i=n-1;
                    System.out.println("Packet missing transfering pakcet from n:"+n+" again");

                }
                cnt = 0;
                pos = 0;
            }

            if(i == frame-1 && cnt == send_win){
                System.out.println("All packets transfered END");
            }
            if(i == frame-1 && cnt != send_win){
                i=n-1;
                System.out.println("Packet missing transfering pakcet from n:"+n+" again");
                cnt = 0;
                pos = 0;
            }
        }

    }
}
