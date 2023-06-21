import java.util.stream.*;
import java.io.*;

public class training1 {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static long fact_reduce(int n)
    {
        // return IntStream.rangeClosed(1, n).reduce((a,b)->a*b).getAsInt();
        return LongStream.rangeClosed(1, (long)n).reduce((a,b)->a*b).getAsLong();
    }

    public static long fact_recur(int n)
    {
        if(n==1) return 1;
        return n*fact_recur(n-1);
    }

    public static void main(String[] args) throws IOException
    {
        int n = Integer.parseInt(br.readLine());
        long start,end,value;

        start = System.currentTimeMillis();
        value = fact_recur(n);
        end = System.currentTimeMillis();
        // Recursion
        bw.write("[재귀]걸린 시간 : "+(end-start)/1000.0+"\n");
        bw.write("value : " + value + "\n");
        bw.flush();

        bw.newLine();

        start = System.currentTimeMillis();
        value = fact_reduce(n);
        end = System.currentTimeMillis();
        // Reduce
        bw.write("[Reduce]걸린 시간 : "+(end-start)/1000.0+"\n");
        bw.write("value : " + value + "\n");
        bw.flush();
    }
}
