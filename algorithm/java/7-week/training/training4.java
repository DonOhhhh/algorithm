import java.util.*;

public class training4 {
    public static int budget()
    {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        int[] req = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int limit = Integer.parseInt(sc.nextLine());
        int requestSum = Arrays.stream(req).reduce(Integer::sum).getAsInt();
        int start = 0;
        int end = Arrays.stream(req).max().getAsInt();
        int mid = end;
        int answer = 0;

        if(requestSum <= limit) return mid;
        
        while(end >= start)
        {
            int tmp = mid;
            requestSum = Arrays.stream(req).map(i-> i > tmp ? tmp : i).reduce(Integer::sum).getAsInt();
            if(requestSum > limit) end = mid-1;
            else
            {
                start = mid + 1;
                answer = mid;
            }
            mid = (int)((end+start)/2);
        }
        return answer;
    }
    public static void main(String[] args) {
        System.out.println(budget());
    }   
}
