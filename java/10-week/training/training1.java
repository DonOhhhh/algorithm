import java.util.*;
import java.util.stream.*;

public class training1
{
    static Map<String,String> parent = new HashMap<>();
    static Map<String,Integer> rank = new TreeMap<>();

    public static void union(String u, String v) {
        String root1 = find(u);
        String root2 = find(v);

        if(!root1.equals(root2))
        {
            if(rank.get(root1) > rank.get(root2))
                parent.replace(root2, root1);
            else
            {
                parent.replace(root1, root2);
                if(rank.get(root1) == rank.get(root2))
                    rank.replace(root2, rank.get(root2)+1);
            }
        }

    }

    public static String find(String v) {
        if(!parent.get(v).equals(v))
            parent.replace(v, find(parent.get(v)));
        return parent.get(v);
    }

    public static int kruskal(ArrayList<String[]> edges, String[] vertices)
    {
        for(String vertex : vertices)
        {
           parent.put(vertex,vertex);
           rank.put(vertex,0);
        }

        List<String[]> mst = new ArrayList<>();
        int sum = 0;
        for(String[] edge : edges)
        {
            if(!find(edge[0]).equals(find(edge[1])))
            {
                union(edge[0],edge[1]);
                mst.add(edge);
                sum += Integer.parseInt(edge[2]);
            }
        }
        return sum;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] input = sc.nextLine().split(" ");
        int v = Integer.parseInt(input[0]);
        int e = Integer.parseInt(input[1]);
        String[] vertices = sc.nextLine().split(" ");

        ArrayList<String[]> edges = new ArrayList<>();
        IntStream.range(0, e).forEach(i -> edges.add(sc.nextLine().split(" ")));
        edges.sort((a,b)->Integer.parseInt(a[2]) > Integer.parseInt(b[2]) ? 1 : -1);

        int answer = kruskal(edges, vertices);
        System.out.println(answer);
    }
}