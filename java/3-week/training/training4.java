import java.io.*;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.stream.*;

public class training4 {
   
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        int[] nodes = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int[][] vertices = IntStream.range(0, nodes.length).filter(x -> x%2==0).mapToObj(i-> Arrays.copyOfRange(nodes, i, i+2)).toArray(size -> new int[size][]);
        System.out.println(Arrays.stream(vertices).map(vertex->Arrays.toString(vertex)).collect(Collectors.joining(", ","[","]")));

        // int[][] vertices = new int[(int)nodes.length/2][2];
        // for(int i = 0 ; i < nodes.length ; i++)
        // {
        //     if(i%2==0)
        //         vertices[(int)i/2][0] = nodes[i];
        //     else
        //         vertices[(int)i/2][1] = nodes[i];
        // }
        // Arrays.stream(vertices).forEach(arr -> {
        //     Arrays.stream(arr).forEach(data->System.out.print(data+" "));
        //     System.out.println();
        // });
    }
}
