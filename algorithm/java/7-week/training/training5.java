import java.lang.reflect.Array;
import java.util.*;
import java.util.stream.Stream;

public class training5 {

    static Scanner sc = new Scanner(System.in);
    
    public static int ramenFactory()
    {
        int stock = Integer.parseInt(sc.nextLine());
        int[] dates = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int[] supplies = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int k = Integer.parseInt(sc.nextLine());
        
        int neededDay = k - stock;
        int[] tmp = Arrays.stream(supplies).boxed().sorted((a,b)->b.compareTo(a)).mapToInt(i->i).toArray();
        int cnt = 0;
        for(int i : tmp)
        {
            if(neededDay <= 0) break;
            neededDay -= i;
            cnt+=1;
        }
        return cnt;
    }
    public static void main(String[] args) {
        System.out.println(ramenFactory());
    }    
}
