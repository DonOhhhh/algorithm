import java.util.*;
import java.util.stream.*;

public class exam1 {

    public static int dfs(Map<String,Set<String>> map, String start)
    {
        Stack<String> stack = new Stack<>();
        stack.push(start);
        List<String> visited = new ArrayList<>();
        String tmp;
        while(stack.size()>0)
        {
            tmp = stack.pop();
            if(!visited.contains(tmp))
            {
                visited.add(tmp);
                stack.addAll(map.get(tmp).stream().toList());
            }
        }
        return visited.size();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] input = sc.nextLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int m = Integer.parseInt(input[1]);
        String[] stations = sc.nextLine().split(" ");
        Map<String,Set<String>> map = new HashMap<>();
        for(int i = 0 ; i < m ; i++)
        {
            input = sc.nextLine().split(" ");
            if(map.containsKey(input[0])) map.get(input[0]).add(input[1]);
            else map.put(input[0], new HashSet<>(Stream.of(input[1]).collect(Collectors.toSet())));

            if(map.containsKey(input[1])) map.get(input[1]).add(input[0]);
            else map.put(input[1], new HashSet<>(Stream.of(input[0]).collect(Collectors.toSet())));
        }
        System.out.println(Arrays.stream(stations).allMatch(s->dfs(map,s)==stations.length) ? "True" : "False");
    }
}
