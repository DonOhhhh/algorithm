import java.util.Arrays;
import java.util.Scanner;
import java.util.stream.Collectors;

public class training1 {
    public static void main(String[] args) {
        System.out.println(Arrays.stream(new Scanner(System.in).nextLine().split(" ")).sorted().collect(Collectors.joining(" ")).strip());
    }
}
