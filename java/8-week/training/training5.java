import java.util.*;
import java.util.stream.*;
import java.io.*;

public class training5 {

    public static double getDistance(int[] cur, int[] next)
    {
        return Math.sqrt(Math.pow(Math.abs(cur[0]-next[0]),2) + Math.pow(Math.abs(cur[1]-next[1]),2));
    }

    public static int exploreMaze(int[][] matrix, int startX, int startY, int endX, int endY)
    {
        int[] cur = {startY, startX};
        int[] end = {endY, endX};
        Map<Double,int[]> tmpDis;
        List<String> visited = new ArrayList<>();
        visited.add(cur[0]+""+cur[1]);
        double distance = getDistance(cur, end);
        int cnt = 1;

        while(distance>0)
        {
            tmpDis = new HashMap<>();
            for(int[] preNext: new int[][]{{cur[0],cur[1]+1},{cur[0],cur[1]-1},{cur[0]+1,cur[1]},{cur[0]-1,cur[1]}})
            {
                // Check if preNext Coordinates are out of Boundaries
                try{if(matrix[preNext[0]][preNext[1]]==0) continue;}
                catch(ArrayIndexOutOfBoundsException e){continue;}
                if(visited.contains(preNext[0]+""+preNext[1])) continue;
                tmpDis.put(getDistance(preNext, end),preNext);
            }
            cur = tmpDis.get(tmpDis.keySet().stream().min(Double::compareTo).get());
            visited.add(cur[0]+""+cur[1]);
            distance = getDistance(cur, end);
            cnt++;
        }

        return cnt;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] hw = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int[][] matrix = new int[hw[0]][hw[1]];
        IntStream.range(0, hw[0]).forEach(i -> matrix[i] = Arrays.stream(sc.nextLine().split("")).mapToInt(Integer::parseInt).toArray());

        int fromTopToDown = exploreMaze(matrix,0,0,hw[1]-1,hw[0]-1);
        int fromDownToTop = exploreMaze(matrix,hw[1]-1,hw[0]-1,0,0);
        System.out.println(fromDownToTop > fromTopToDown ? fromTopToDown : fromDownToTop);
    }
}
