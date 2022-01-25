import java.util.*;
import java.util.stream.*;

public class exam4 {
    public static void main(String[] args) {
        int n = Integer.parseInt(new Scanner(System.in).nextLine());
        String[] validNums = IntStream.rangeClosed(1, n).mapToObj(j -> String.valueOf(j)).filter(i -> i.matches("(1*6*8*9*0*)*")).toArray(String[]::new);
        String[] modified = IntStream.range(0, validNums.length).mapToObj(i->new StringBuilder(validNums[i].replace("6", "2").replace("9", "6").replace("2", "9")).reverse().toString()).toArray(String[]::new);
        long cnt = IntStream.range(0, validNums.length).filter(i -> Integer.parseInt(validNums[i]) != Integer.parseInt(modified[i])).count();
        System.out.println(cnt);
    }
}
