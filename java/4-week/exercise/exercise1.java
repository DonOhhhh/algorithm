import java.util.Scanner;
import java.util.stream.IntStream;

public class exercise1 {
    public static void main(String[] args) {
        String[] str = new Scanner(System.in).nextLine().split("-");
        IntStream.range(0, str.length).forEach(i -> {
            if(i==str.length-1) System.out.println(str[i]);
            else System.out.print("*".repeat(str[i].length()));
        });
    }
}
