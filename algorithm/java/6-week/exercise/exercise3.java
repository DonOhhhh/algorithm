import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Scanner;
import java.util.stream.Collectors;

public class exercise3 {
    public static void main(String[] args) {
        String[] inputs_ori = new Scanner(System.in).nextLine().split(" ");
        String[] inputs_mod = Arrays.stream(inputs_ori).map(data -> Arrays.stream(data.split("")).sorted().collect(Collectors.joining(""))).toArray(String[]::new);
        HashMap<String,ArrayList<Integer>> result = new HashMap<>();
        for(int i = 0 ; i < inputs_mod.length ; i++)
        {
            if(result.containsKey(inputs_mod[i])) result.get(inputs_mod[i]).add(i);
            else result.put(inputs_mod[i],new ArrayList<>(Arrays.asList(Integer.valueOf(i))));
        }
        result.keySet().stream().sorted().forEach(s -> System.out.println(result.get(s).stream().map(i -> inputs_ori[i]).collect(Collectors.joining(" ")).strip()));
    }
}
