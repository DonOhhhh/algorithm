import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class exercise1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<String> participants = new ArrayList<>(Arrays.stream(sc.nextLine().split(" ")).toList());
        String[] finisher = sc.nextLine().split(" ");
        for(String f : finisher) participants.remove(f);
        System.out.println(participants.stream().collect(Collectors.joining(" ")));
    }
}
