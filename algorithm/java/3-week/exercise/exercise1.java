import java.util.Arrays;
import java.util.Scanner;

public class exercise1 {
    public static int fibo(int n)
    {
        int[] arr = new int[n+1];
        arr[0] = 0;
        arr[1] = 1;
        for(int i = 2 ; i < arr.length ; i++)
        {
            arr[i] = arr[i-1] + arr[i-2];
        }
        return arr[n];
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println(fibo(sc.nextInt())); 
    }
}
