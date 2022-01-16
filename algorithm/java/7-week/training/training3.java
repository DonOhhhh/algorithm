package training;

import java.util.Arrays;
import java.util.stream.LongStream;
import java.io.*;

public class training3 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        String[] nm = br.readLine().strip().split(" ");
        long n = Long.parseLong(nm[0]);
        long m = Long.parseLong(nm[1]);
        long[] examiners = new long[(int)n];
        for(int i = 0 ; i < n ; i++) examiners[i] = Long.parseLong(br.readLine().strip());
        
        long end = Arrays.stream(examiners).max().getAsLong() * m;
        long start = 1;
        long result = 0;
        long mid = end;
        long answer = 0;
        while(end>=start)
        {
            long tmp = mid;
            result = Arrays.stream(examiners).map(i -> (long)(tmp/i)).reduce(Long::sum).getAsLong();
            if(m > result) start = mid+1;
            else
            {
                end = mid-1;
                answer = mid;
                if(m==result) break;
            }
            mid = (long)((end+start)/2);
        }
        System.out.println(answer);
    }
}
