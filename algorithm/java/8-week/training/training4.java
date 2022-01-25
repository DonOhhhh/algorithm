import java.util.*;
import java.util.stream.*;
import java.io.*;

public class training4 {

    public static List<int[]> checkValidate(int[][] matrix, int[][] ewns)
    {
        List<int[]> result = new ArrayList<>();
        for(int[] coor : ewns)
        {
            try
            {
                if(matrix[coor[0]][coor[1]] == 0)
                    result.add(coor);
            }
            catch(ArrayIndexOutOfBoundsException e) {}
        }
        return result;
    }

    public static int tomato(int[][] matrix, int width, int height) 
    {
        int cnt = 0;
        List<int[]> list;
        do
        {
            list = new ArrayList<>();
            for(int i = 0 ; i < height ; i++)
            {
                for(int j = 0 ; j < width ; j++)
                {
                    if(matrix[i][j]==1)
                        list.addAll(checkValidate(matrix, new int[][]{{i,j+1},{i,j-1},{i+1,j},{i-1,j}}));
                }
            }

            for(int[] coor: list) matrix[coor[0]][coor[1]] = 1;
            cnt++;
        } while(list.size()>0);
        
        int isDone = (int)Arrays.stream(matrix).flatMapToInt(arr->Arrays.stream(arr)).filter(i->i==1 || i==-1).count();
        return isDone == width*height ? --cnt : -1;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] wh = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int[][] matrix = new int[wh[1]][wh[0]];
        IntStream.range(0, wh[1]).forEach(i->matrix[i] = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray());
        int answer = tomato(matrix, wh[0], wh[1]);
        System.out.println(answer);
    }
}
