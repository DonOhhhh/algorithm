import java.util.*;
import java.util.stream.*;

public class problem4 {

    public static int solution(int[][] timetable, int[][] tuition, int limit)
    {
        
        return 0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] input = sc.nextLine().split(" ");
        int student = Integer.parseInt(input[0]);
        int classNum = Integer.parseInt(input[1]);
        int[][] timetable = IntStream.range(0, student).mapToObj(i -> Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray()).toArray(int[][]::new);
        int[][] tuition = IntStream.range(0, student).mapToObj(i -> Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray()).toArray(int[][]::new);
        int limit = Integer.parseInt(sc.nextLine());
        System.out.println(solution(timetable, tuition, limit));
    }   
}
