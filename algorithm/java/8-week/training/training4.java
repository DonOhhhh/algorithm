import java.util.*;
import java.util.stream.*;
import java.io.*;

public class training4 {

    public static void isZeroExistNearby() {
        
    }

    public static void tomato(int[][] matrix) 
    {
        for(int i = 0; i < matrix.length ; i++)
        {
            for(int j = 0 ; j < matrix[i].length ; j++)
            {
                if(matrix[i][j]==1)
                    
            }
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] wh = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int[][] matrix = new int[wh[1]][wh[0]];
        IntStream.range(0, wh[1]).forEach(i->matrix[i] = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray());
        System.out.println();
    }
}
