import java.util.Arrays;
import java.util.Scanner;
import java.util.Set;
import java.util.stream.Collectors;

public class training1 {
    public static void main(String[] args) {
        String[] participants = new Scanner(System.in).nextLine().split(" ");
        String[] finishers = new Scanner(System.in).nextLine().split(" ");
        Set<String> p = Arrays.stream(participants).collect(Collectors.toSet());
        Set<String> f = Arrays.stream(finishers).collect(Collectors.toSet());
        p.removeAll(f);
        System.out.println(p.stream().sorted().collect(Collectors.joining(" ")).strip());
    }
}
