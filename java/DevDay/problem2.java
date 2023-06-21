import java.util.*;
import java.util.stream.*;

public class problem2 {

    public static int[][] isBoundary(int[][] arounds, int[][] matrix)
    {
        List<int[]> result = new ArrayList<>();
        for(int i = 0 ; i < arounds.length ; i++)
        {
            if(arounds[i][0] >= matrix.length || arounds[i][0] < 0 || arounds[i][1] >= matrix[0].length || arounds[i][1] < 0) continue;
            result.add(arounds[i]);
        }
        return result.stream().toArray(int[][]::new);
    }

    public static void germReproduce(int[][] matrix, int i, int j, int max_virus, Set<int[]> visited) {
        // visited에 [i,j]가 있는지 검사
        if(visited.stream().anyMatch(arr-> arr[0] == i && arr[1] == j)) return;
        if(matrix[i][j]==max_virus)
        {
            // visited에 [i,j]를 넣고 주변 칸 중 범위를 벗어나지 않는 칸들을 구한다.
            visited.add(new int[]{i,j});
            int[][] inBoundary = isBoundary(new int[][]{{i,j+1},{i,j-1},{i+1,j},{i-1,j}}, matrix);
            List<int[]> completed = new ArrayList<>();
            // 주변 칸들의 값들을 살펴본다.
            for(int[] coord : inBoundary)
            {
                // 주변 칸의 값이 max_virus보다 작다면 visited에 추가하고 해당 칸의 값을 1 증가한다.
                if(matrix[coord[0]][coord[1]]<max_virus)
                {
                    visited.add(new int[]{coord[0],coord[1]});
                    matrix[coord[0]][coord[1]] += 1;
                }
                // 주변 칸의 값이 max_virus라면 completed에 추가한다.
                else completed.add(coord);
            }
            // completed가 있으면 해당 칸의 좌표를 인자로 germReproduce를 호출한다.
            for(int[] coord : completed)
                germReproduce(matrix, coord[0], coord[1], max_virus, visited);
        }
        else matrix[i][j] += 1;
    }

    public static int[][] solution(int rows, int columns, int max_virus,int[][] queries)
    {
        int[][] matrix = new int[rows][columns];
        for(int[] query : queries)
            germReproduce(matrix, query[0]-1, query[1]-1, max_virus, new HashSet<>());
        return matrix;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] rc = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int maxVirus = Integer.parseInt(sc.nextLine());
        List<int[]> queries = new ArrayList<>();
        while(sc.hasNextLine())
            queries.add(Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray());
        int[][] answer = solution(rc[0],rc[1],maxVirus,queries.stream().toArray(int[][]::new));
        System.out.println(Arrays.stream(answer).map(Arrays::toString).collect(Collectors.joining(", ","[","]")));
        sc.close();
    }
}
