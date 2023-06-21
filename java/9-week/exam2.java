import java.util.*;
import java.util.stream.*;

public class exam2 {

    public static int b_search(int[] arr, int key)
    {
        int start = 0;
        int end = arr.length-1;
        int mid = end;
        while(end>start)
        {
            if(arr[mid] > key) end = mid - 1;
            else if(arr[mid] < key) start = mid + 1;
            else break;
            mid = (int)((end+start)/2);
        }
        return mid;
    }

    public static int minPower(int[] base, int[] power)
    {
        int pos = 0;
        int dis = 0;
        int answer = Integer.MIN_VALUE;
        for(int b : base)
        {
            pos = b_search(power, b);
            if((pos == 0 && power[pos] > b) || (pos == power.length-1 && power[pos] < b) || (power[pos]==b)) dis = Math.abs(power[pos]-b);
            else dis = Math.abs(power[pos]-b) < Math.abs(power[pos+1]-b) ? Math.abs(power[pos]-b) : Math.abs(power[pos+1]-b);
            
            if(answer < dis) answer = dis;
        }
        return answer;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] base = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).sorted().toArray();
        int[] power = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).sorted().toArray();
        System.out.println(minPower(base, power));
    }
}
