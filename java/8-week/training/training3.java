import java.util.*;
import java.util.stream.*;
import java.io.*;

public class training3 {

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
        int[] elem = Arrays.stream(matrix).flatMapToInt(data -> Arrays.stream(data)).distinct().filter(i->i!=0).toArray();
        Map<Integer, int[]> coloringBook = new LinkedHashMap<>();
        for(int e : elem)
        {
            Map<int[],int[][]> linkedMap = new LinkedHashMap<>();
            for(int i = 0 ; i < matrix.length ; i++)
            {
                for(int j = 0 ; j < matrix[i].length ; j++)
                {
                    if(matrix[i][j]==e)
                        linkedMap.put(new int[]{i,j},isBoundary(new int[][]{{i,j+1},{i,j-1},{i+1,j},{i-1,j}}, matrix[i].length, matrix.length));
                }
            }
            coloringBook.put(e,dfs(linkedMap));
        }

        int area = 0;
        int largestArea = 0;
        int[] result = new int[2];

        for(Map.Entry<Integer,int[]> tmp : coloringBook.entrySet())
        {
            area += tmp.getValue().length;
            largestArea = Arrays.stream(tmp.getValue()).max().getAsInt();
            result[1] = largestArea > result[1] ? largestArea : result[1];
        }
        result[0] = area;
        
        return result;
    }

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int[] hw = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int[][] matrix = new int[hw[0]][hw[1]];
        IntStream.range(0, hw[0]).forEach(i -> matrix[i] = Arrays.stream(sc.nextLine().strip().split("")).mapToInt(Integer::parseInt).toArray());
        
        int[] answer = countApart(matrix);
        Arrays.stream(answer).forEach(System.out::println);
    }
}
