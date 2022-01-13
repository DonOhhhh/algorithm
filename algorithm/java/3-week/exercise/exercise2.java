import java.util.Arrays;
import java.util.Scanner;

public class exercise2 {
    public static int euclid(int dividend, int divisor)
    {
        if(divisor==0) return dividend;
        return euclid(divisor, dividend%divisor);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] inputs = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        System.out.println(euclid(inputs[0], inputs[1]));
    }
}
