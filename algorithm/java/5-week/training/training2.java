import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class training2 {
    public static boolean anagram2(String s1, String s2)
    {
        HashMap<String, Integer> cnt1 = new HashMap<>();
        HashMap<String, Integer> cnt2 = new HashMap<>();
        
        Arrays.stream(s1.split("")).forEach(data->{
            if(cnt1.containsKey(data)) cnt1.replace(data, cnt1.get(data)+1);
            else cnt1.put(data, 1);
        });

        Arrays.stream(s2.split("")).forEach(data->{
            if(cnt2.containsKey(data)) cnt2.replace(data, cnt2.get(data)+1);
            else cnt2.put(data, 1);
        });
        
        return cnt1.entrySet().equals(cnt2.entrySet()) ? true : false;
    }
    public static boolean anagram1(String s1, String s2)
    {
        return Stream.of(s1,s2).map(data->Arrays.stream(data.split("")).sorted().collect(Collectors.joining())).distinct().count() == 1 ? true : false;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] str = sc.nextLine().split(" ");
        System.out.println(anagram2(str[0], str[1]));
    }
}
