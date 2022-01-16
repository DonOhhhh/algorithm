import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class exercise1 {

    public static String[] dfs(HashMap<String,String[]> hashMap, String start)
    {
        Stack<String> stack = new Stack<>();
        LinkedList<String> visited = new LinkedList<>();
        String tmp;
        stack.push(start);
        while(stack.size() > 0)
        {
            tmp = stack.pop();
            if(!visited.contains(tmp))
            {
                visited.add(tmp);
                stack.addAll(Arrays.asList(hashMap.get(tmp)));
            }
        }
        return visited.stream().toArray(String[]::new);
    }

    public static String[] bfs(HashMap<String,String[]> hashMap, String start)
    {
        Queue<String> queue = new LinkedList<>();
        LinkedList<String> visited = new LinkedList<>();
        String tmp;
        queue.add(start);
        while(queue.size()>0)
        {
            tmp = queue.poll();
            if(!visited.contains(tmp))
            {
                visited.add(tmp);
                queue.addAll(Arrays.asList(hashMap.get(tmp)));
            }
        }
        return visited.stream().toArray(String[]::new);
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String startNode = br.readLine();
        String s;
        String[] tmp;
        HashMap<String,String[]> hashMap = new HashMap<>();
        while((s=br.readLine())!=null)
        {
            tmp = s.split(" ");
            hashMap.put(tmp[0], Arrays.copyOfRange(tmp, 1, tmp.length));
        }
        tmp = bfs(hashMap, startNode);
        System.out.println(Arrays.stream(tmp).collect(Collectors.joining(" ")));
        tmp = dfs(hashMap, startNode);
        System.out.println(Arrays.stream(tmp).collect(Collectors.joining(" ")));
    }
}
