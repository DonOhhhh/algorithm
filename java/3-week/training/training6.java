import java.util.*;
import java.util.stream.IntStream;

public class training6 {
    public static long factorial(int n) {
        return IntStream.rangeClosed(1, n).reduce((a,b)->a*b).getAsInt();
    }
    public static void main(String[] args) {
        long a = factorial(10);
        long b = factorial(8);
        System.out.println(a*b/2);
    }
}
