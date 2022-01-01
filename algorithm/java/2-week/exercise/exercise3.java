import java.util.*;
import java.io.*;

public class exercise3 {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException{
        // n,k,i를 입력받음
        String line;
        line = br.readLine();
        int[] input = Arrays.stream(line.trim().split(" ")).mapToInt(Integer::parseInt).toArray();
        int k = input[1];
        int i = input[2];
        line = br.readLine();
        input = Arrays.stream(line.trim().split(" ")).mapToInt(Integer::parseInt).sorted().toArray();
        bw.write(input[k-1]+input[input.length-1-(i-1)]+"\n");
        bw.flush();
        
    }
}
