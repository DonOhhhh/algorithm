import java.util.Scanner;
import java.util.stream.IntStream;

public class exercise3 {
    public static int pyramid(int n)
    {
        return IntStream.range(0, n).map(i -> (int)Math.pow(2,i)).boxed().reduce(Integer::sum).get();
    }
    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        System.out.println(pyramid(n));
    }
}
