import java.util.Arrays;
import java.util.Scanner;
import java.util.TreeSet;
import java.util.stream.Collectors;

public class exercise3 {
    public static void main(String[] args) {
        TreeSet<Integer> weights = new TreeSet<>(Arrays.stream(new Scanner(System.in).nextLine().split(" ")).mapToInt(Integer::parseInt).boxed().collect(Collectors.toSet()));
        int diff;
        while(weights.size()>1)
        {
            diff = weights.pollLast() - weights.pollLast();
            if(weights.contains(diff))
            {
                weights.remove(diff);
                weights.add(0);
            }
            else weights.add(diff);
        }
        System.out.println(weights.first());
    }
}
