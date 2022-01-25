import java.util.*;
import java.util.stream.*;

public class exercise2 {

    public static Integer prim(Map<String,List<String[]>> graph)
    {
        PriorityQueue<String[]> q = new PriorityQueue<>((String[] s1, String[] s2)->Integer.parseInt(s1[2]) > Integer.parseInt(s2[2]) ? 1 : -1);
        q.add(new String[]{"A","A","0"});
        Set<String> visited = new HashSet<>();
        Integer sum = 0;
        List<String[]> path = new ArrayList<>();

        while(q.size()>0)
        {
            String[] tmp = q.poll();
            if(visited.contains(tmp[0]) && visited.contains(tmp[1])) continue;
            visited.add(tmp[0]);
            visited.add(tmp[1]);
            sum += Integer.parseInt(tmp[2]);
            path.add(tmp);
            graph.get(tmp[1]).stream().filter(i->!(visited.contains(i[0]) && visited.contains(i[1]))).forEach(j -> q.add(j));
        }
        return sum;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] ve = sc.nextLine().split(" ");
        String[] vertices = sc.nextLine().split(" ");
        String[] tmp;

        Map<String,List<String[]>> graph = new HashMap<>();
        String[][] edges = IntStream.range(0, Integer.parseInt(ve[1])).mapToObj(i -> sc.nextLine().split(" ")).toArray(String[][]::new);
        TreeSet<Integer> q = new TreeSet<>();
        for(String[] com : edges)
        {
            graph = new HashMap<>();
            for(String[] edge : edges)
            {
                if(Arrays.deepEquals(com, edge)) continue;
                if(!graph.containsKey(edge[0])) graph.put(edge[0],new ArrayList<>());
                graph.get(edge[0]).add(edge);
                if(!graph.containsKey(edge[1])) graph.put(edge[1],new ArrayList<>());
                graph.get(edge[1]).add(edge);
            }
            q.add(prim(graph));
        }
        q.pollFirst();
        System.out.println(q.pollFirst());
    }
}
