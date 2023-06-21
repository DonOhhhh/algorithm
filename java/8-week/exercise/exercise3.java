import java.util.*;
import java.util.stream.*;

public class exercise3 {

    public static int dfs(Map<Integer,Set<Integer>> map, int start) {
        Stack<Integer> stack = new Stack<>();
        stack.push(start);
        List<Integer> visited = new ArrayList<>();
        int tmp;
        while(stack.size()>0)
        {
            tmp = stack.pop();
            if(!visited.contains(tmp))
            {
                if(!map.containsKey(tmp)) continue;
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
        int[][] connection = new int[m][];
        IntStream.range(0, m).forEach(i -> connection[i] = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray());
        List<int[]> result = new ArrayList<>();

        Map<Integer,Set<Integer>> map;
        for(int i = 0 ; i < m ; i++)
        {
            map = new HashMap<>();
            int[] removed = connection[i];
            for(int[] road : connection)
            {
                if(Arrays.equals(road, removed)) continue;
                
                if(map.containsKey(road[0])) map.get(road[0]).add(road[1]);
                else map.put(road[0], new TreeSet<>(Stream.of(road[1]).collect(Collectors.toSet())));

                if(map.containsKey(road[1])) map.get(road[1]).add(road[0]);
                else map.put(road[1], new TreeSet<>(Stream.of(road[0]).collect(Collectors.toSet())));
            }
            if(dfs(map, 0) < n) result.add(removed);
        }

        result.stream().sorted((a,b)->Arrays.compare(a, b)).forEach(i->System.out.println(i[0] + " " + i[1]));
    }
}
