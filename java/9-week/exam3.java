import java.util.*;
import java.util.stream.*;

public class exam3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<String[]> inputs = new ArrayList<>();
        while(sc.hasNextLine())
            inputs.add(sc.nextLine().strip().split("[:|\\-|.]"));
        for(String[] input : inputs)
        {
            if(input.length==6 && Arrays.stream(input).allMatch(i->i.matches("(\\d*[A-F]*){2}")))
            {
                System.out.println("MAC");
            }
            else if(input.length==4 && Arrays.stream(input).allMatch(i->Integer.parseInt(i) <= 255 && Integer.parseInt(i) >= 0))
            {
                System.out.println("IP");
            }
            else System.out.println(0);
        }
    }
}
