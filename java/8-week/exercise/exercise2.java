import java.util.*;
import java.util.stream.*;

public class exercise2
{
    public static int[] dfs(int[][] memo, int start) {
        Stack<Integer> stack = new Stack<>();
        stack.push(start);
        List<Integer> visited = new ArrayList<>();
        int tmp;
        while(stack.size()>0)
        {
            tmp = stack.pop();
            if(!visited.contains(tmp))
            {
                visited.add(tmp);
                if(memo[tmp]==null) continue;
                stack.addAll(Arrays.stream(memo[tmp]).boxed().toList());
            }
        }
        return visited.stream().mapToInt(Integer::intValue).toArray();
    }


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        int[][] memo = new int[n][];
        IntStream.range(0, n).forEach(i-> {
            try {
                memo[i] = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();    
            } catch (NumberFormatException e) {}
        });
        int[] answer = dfs(memo, 0);
        System.out.println(answer.length == n ? "True" : "False");
    }
}