import java.util.*;
import java.util.stream.*;

public class training3 {

    public static int[][] combination_recursion(int[] arr, int n)
    {
        if(n == 0 || n > arr.length) return null;
        Set<Set<Integer>> result = new HashSet<>();
        int[][] tmp;
        Set<Set<Integer>> tmp2;
        for(int i : arr)
        {
            tmp = combination_recursion(Arrays.stream(arr).filter(j->i!=j).toArray() , n-1);
            // 요소가 1개밖에 없을 때
            if(tmp==null)
            {
                tmp2 = new HashSet<>();
                tmp2.add(Stream.of(i).collect(Collectors.toSet()));
            } 
            // 요소가 1개 이상일 때
            else tmp2 = Arrays.stream(tmp).map(j -> Stream.concat(Stream.of(i), Arrays.stream(j).boxed()).collect(Collectors.toSet())).collect(Collectors.toSet());
            for(Set<Integer> a : tmp2)
            {
                if(a.size()<n) continue;
                result.add(a);
            }
        }
        
        return result.stream().map(data -> data.stream().mapToInt(i->i).toArray()).toArray(int[][]::new);
    }

    public static int[][] permutation_recursion(int[] arr)
    {
        if(arr.length==1) return new int[][]{arr};
        int[][] tmp;
        List<int[]> list = new ArrayList<int[]>();
        for(int i : arr)
        {
            tmp = permutation_recursion(Arrays.stream(arr).filter(a -> a!=i).toArray());
            for(int[] j : tmp)
            {
                list.add(Stream.concat(Arrays.stream(new int[]{i}).boxed(), Arrays.stream(j).boxed()).mapToInt(data->data).toArray());
            }
        }
        return list.toArray(new int[list.size()][]);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        long start,end;
        int[] arr = IntStream.rangeClosed(1, n).toArray();
        // int[][] result1 = permutation_recursion(arr);
        int[][] result2 = combination_recursion(arr, 1);
        System.out.println();
    }
    
}
