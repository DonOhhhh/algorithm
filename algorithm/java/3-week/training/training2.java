import java.util.*;

public class training2 {

    public static long fibo_tab(int n)
    {
        long[] table = new long[n+1];
        table[0] = 1;
        table[1] = 1;
        for(int i = 2; i < n+1 ; i++)
        {
            table[i] = table[i-1] + table[i-2];
        }
        return table[n];
    }

    public static int fibo_memo(int n, Map<Integer, Integer> map)
    {
        if(n<2) return 1;
        if(map.containsKey(n))
        {
            return map.get(n);
        }
        else
        {
            map.put(n,fibo_memo(n-1, map)+fibo_memo(n-2, map));
            return map.get(n);
        }
    }

    public static int fibo_recursive(int n) {
        if(n < 2) return 1;
        return fibo_recursive(n-1)+fibo_recursive(n-2);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        long[] begin = new long[3];
        long[] end = new long[3];
        long[] result = new long[3];

        // begin[0] = System.currentTimeMillis();
        // result[0] = fibo_recursive(n);
        // end[0] = System.currentTimeMillis();
        // System.out.println("Recursive time : " + (end[0]-begin[0])/1000.0);
        // System.out.println("Recursive result : " + result[0]);
        
        // begin[1] = System.currentTimeMillis();
        // result[1] = fibo_memo(n, new HashMap<Integer,Integer>());
        // end[1] = System.currentTimeMillis();
        // System.out.println("Memoization time : " + (end[1]-begin[1])/1000.0);
        // System.out.println("Memoization result : " + result[1]);
        
        begin[2] = System.currentTimeMillis();
        result[2] = fibo_tab(n);
        end[2] = System.currentTimeMillis();
        System.out.println("Tabulation time : " + (end[2]-begin[2])/1000.0);
        System.out.println("Tabulation result : " + result[2]);
    }  
}
