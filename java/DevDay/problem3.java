import java.util.*;
import java.util.stream.*;

public class problem3 {

    public static int getTree(Map<Integer,Set<Integer>> tree, int[] info, int n, Set<Integer> visited, int type, int cnt) {

        Set<Integer> connected = new HashSet<>(tree.get(n));
        connected.removeAll(visited);
        int result = 0;

        while(connected.size()>0)
        {
            int nextNode = connected.stream().findAny().get();
            connected.remove(nextNode);
            if(type==0)
            {
                if(cnt==1 && info[n-1]==0) result += getTree(tree, info, nextNode, visited, type, cnt+1);
                if(cnt==2 && info[n-1]==1) result += getTree(tree, info, nextNode, visited, type, cnt+1);
                if(cnt==3 && info[n-1]==1) result += getTree(tree, info, nextNode, visited, type, cnt+1);
            }
            else
            {
                if(cnt==1 && info[n-1]==1) result += getTree(tree, info, nextNode, visited, type, cnt+1);
                if(cnt==2 && info[n-1]==0) result += getTree(tree, info, nextNode, visited, type, cnt+1);
                if(cnt==3 && info[n-1]==0) result += getTree(tree, info, nextNode, visited, type, cnt+1);
            }
        }

        if(type == 0 && cnt==4 && info[n-1]==0) result += 1;
        else if(type == 1 && cnt==4 && info[n-1]==1) result += 1;
        
        return result;
    }

    public static long[] solution(int[] info, int[][] edges) {
        Map<Integer,Set<Integer>> tree = new HashMap<>();
        for(int[] e : edges)
        {
            if(!tree.containsKey(e[0])) tree.put(e[0],new HashSet<>());
            tree.get(e[0]).add(e[1]);

            if(!tree.containsKey(e[1])) tree.put(e[1],new HashSet<>());
            tree.get(e[1]).add(e[0]);
        }

        long blue = 0;
        long red = 0;

        for(Integer i : tree.keySet())
        {
            if(info[i-1]==0)
                blue += getTree(tree, info, i, new HashSet<>(), info[i-1], 1);
            else
                red += getTree(tree, info, i, new HashSet<>(), info[i-1], 1);
        }

        blue = (long)blue/2;
        red = (long)red/2;

        return new long[]{blue%1000000007, red%1000000007};
    }
    public static void main(String[] args) {
        // 0 - 파란색, 1 - 빨간색
        Scanner sc = new Scanner(System.in);
        int[] info = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int[][] edges = IntStream.range(0, info.length-1).mapToObj(i -> Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).sorted().toArray()).toArray(int[][]::new);
        long[] answer = solution(info, edges);
        System.out.println(Arrays.stream(answer).mapToObj(String::valueOf).collect(Collectors.joining(" ")));
        sc.close();
    }
}
