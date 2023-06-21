import java.util.Arrays;
import java.util.Scanner;
import java.util.stream.IntStream;

public class exercise4 {
    public static int stairs(int n, int m)
    {
        if(n<=1) return 1;
        return IntStream.range(n-m,n).map(x -> stairs(x, m > x ? x : m)).reduce(Integer::sum).getAsInt();
    }
    public static void main(String[] args) {
        int[] nm = Arrays.stream(new Scanner(System.in).nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        System.out.println(stairs(nm[0], nm[1]));
    }
}
