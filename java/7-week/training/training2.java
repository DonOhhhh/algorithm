import java.io.*;
import java.util.*;

public class training2 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        List<Integer> A = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).boxed().toList();
        int m = Integer.parseInt(br.readLine());
        List<Integer> X = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).boxed().toList();
        for(int i : X)
        {
            if(A.contains(i))
                bw.write(1+"\n");
            else
                bw.write(0+"\n");
            bw.flush();
        }
    }
}
