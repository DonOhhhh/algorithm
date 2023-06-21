import java.util.*;
import java.util.stream.*;

public class training1 {

    public static void name() {
        
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        int[][] edges = IntStream.range(0, n).mapToObj(i -> Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray());
        int m = Integer.parseInt(sc.nextLine());
        int[][] testCases = IntStream.range(0, m).mapToObj(i -> Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray());




    }
}
