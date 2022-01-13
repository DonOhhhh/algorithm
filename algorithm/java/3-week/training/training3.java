import java.util.*;
import java.util.stream.*;

public class training3 {

    public static <T> T[][] permutation(T[] arr)
    {
        if(arr.length == 1) return (T[][])new Object[][]{arr};
        T[][] tmp;
        List<T[]> list = new ArrayList();
        for(T i: arr)
        {
            tmp = (T[][])permutation(Arrays.stream(arr).filter(a->a!=i).toArray());
            for(T[] j : tmp)
            {
                list.add((T[])Stream.concat(Arrays.stream((T[])new Object[]{i}),Arrays.stream(j)).toArray());
            }
        }
        return list.toArray((T[][])new Object[list.size()][]);
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
        int[][] result = permutation_recursion(arr);
        // Integer[] arr2 = IntStream.rangeClosed(1, n).boxed().toArray(Integer[]::new);
        // Object[][] result = permutation(arr2);
        // Arrays.stream(result).forEach(data->System.out.println(Arrays.toString(data)));
    }
    
}
