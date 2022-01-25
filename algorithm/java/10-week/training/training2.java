import java.util.*;
import java.util.stream.*;

public class training2 {

    public static int prim(Map<String,List<String[]>> graph)
    {
        PriorityQueue<String[]> priorityQueue = new PriorityQueue<>(1,(String[] s1, String[] s2)->Integer.parseInt(s1[2]) > Integer.parseInt(s2[2]) ? 1 : -1);
        priorityQueue.add(new String[]{"A","A","0"});
        String[] tmp;
        Set<String> visited = new HashSet<>();
        int sum = 0;
        List<String[]> answer = new ArrayList<>();

        while(priorityQueue.size()>0)
        {
            tmp = priorityQueue.poll();
            if(visited.contains(tmp[1]) && visited.contains(tmp[0])) continue;
            visited.add(tmp[1]);
            visited.add(tmp[0]);
            sum += Integer.parseInt(tmp[2]);
            answer.add(tmp);
            for(String[] edge : graph.get(tmp[1]))
            {
                if(!visited.contains(edge[1]) || !visited.contains(edge[0]))
                    priorityQueue.add(edge);
            }
        }
        return sum;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] input = sc.nextLine().split(" ");
        String[] vertices = sc.nextLine().split(" ");
        String[] tmp;
        Map<String,List<String[]>> graph = new HashMap<>();
        for(int i = 0 ; i < Integer.parseInt(input[1]) ; i++)
        {
            tmp = sc.nextLine().split(" ");
            if(!graph.containsKey(tmp[0])) graph.put(tmp[0],new ArrayList<>());
            graph.get(tmp[0]).add(tmp);
            if(!graph.containsKey(tmp[1])) graph.put(tmp[1],new ArrayList<>());
            graph.get(tmp[1]).add(tmp);
        }
        System.out.println(prim(graph));
    }
}
