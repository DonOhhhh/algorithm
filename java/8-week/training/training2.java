import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.io.*;

public class training2 {

    public static int[] dfs(Map<int[],int[][]> linkedMap)
    {
        List<Integer> result = new LinkedList<>();
        while(linkedMap.size()>0)
        {
            Stack<int[]> stack = new Stack<>();
            List<int[]> visited = new LinkedList<>();
            int[] root = linkedMap.keySet().stream().findAny().get();
            stack.add(root);
            int[] tmp;

            while(stack.size()>0)
            {
                tmp = stack.pop();
                if(!visited.contains(tmp))
                {
                    int[] tmp2 = tmp;
                    if(linkedMap.keySet().stream().filter(i -> Arrays.equals(i, tmp2)).count()<1) continue;
                    visited.add(tmp);
                    stack.addAll(linkedMap.entrySet().stream().filter(i -> Arrays.equals(i.getKey(), tmp2)).flatMap(j -> Arrays.stream(j.getValue())).toList());
                    for(Map.Entry<int[],int[][]> map : linkedMap.entrySet())
                    {
                        if(Arrays.equals(map.getKey(), tmp2))
                        {
                            linkedMap.remove(map.getKey());
                            break;
                        }
                    }
                }
            }
            result.add(visited.size());
        }
        return result.stream().mapToInt(i->i).toArray();
    }

    public static int[][] isBoundary(int[][] adjacents, int w, int h)
    {
        return IntStream.range(0, adjacents.length).filter(i -> !(adjacents[i][0] >= h || adjacents[i][0] < 0 || adjacents[i][1] >= w || adjacents[i][1] < 0)).mapToObj(i->adjacents[i]).toArray(int[][]::new);
    }

    public static int[] countApart(int[][] matrix)
    {
        Map<int[],int[][]> linkedMap = new LinkedHashMap<>();
        for(int i = 0 ; i < matrix.length ; i++)
        {
            for(int j = 0 ; j < matrix[i].length ; j++)
            {
                if(matrix[i][j]==1)
                    linkedMap.put(new int[]{i,j},isBoundary(new int[][]{{i,j+1},{i,j-1},{i+1,j},{i-1,j},{i-1,j-1},{i+1,j+1},{i-1,j+1},{i+1,j-1}}, matrix[i].length, matrix.length));
            }
        }
        return dfs(linkedMap);
    }

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        List<Integer> list = new ArrayList<>();
        while(true)
        {
            int[] wh = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            if(wh[1] == 0 && wh[0] == 0) break;
            int[][] matrix = new int[wh[1]][wh[0]];
            IntStream.range(0, matrix.length).forEach(i -> matrix[i] = Arrays.stream(sc.nextLine().strip().split(" ")).mapToInt(Integer::parseInt).toArray());
            
            int[] answer = countApart(matrix);
            list.add(answer.length);
        }
        list.stream().forEach(System.out::println);
    }
}
