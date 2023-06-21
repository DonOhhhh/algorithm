import java.io.*;
import java.util.*;
import java.util.stream.Stream;

public class solution {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void fourth() throws IOException {
        int n = Integer.parseInt(br.readLine().trim());
        int total = 0;
        String line;
        while((line=br.readLine())!=null)
        {
            total += Arrays.stream(line.split(" ")).mapToInt(Integer::parseInt).sum();
        }
        bw.write(total+"\n");
        bw.flush();
    }

    public static void third() throws IOException{
        String line;
        String tmp = "";
        while((line=br.readLine())!=null)
        {
            tmp += line;
        }
        int total = Arrays.stream(tmp.split("")).map(Integer::parseInt).reduce(0, (a,b)->a+b);
        bw.write(total+"\n");
        bw.flush();
    }

    public static void second() throws IOException{
        String line;
        Stream<Integer> input = null;

        while((line=br.readLine())!=null)
        {
            input = Arrays.stream(line.split("")).map(Integer::parseInt);
        }
        input.forEach(System.out::println);        
    }

    public static void first() throws IOException{
        String line;
        while((line=br.readLine())!=null)
        {
            if(Integer.parseInt(line)%2==0)
                bw.write("Hello, Coding Test");
            else
                bw.write("Hello, Algorithm");
            bw.newLine();
            bw.flush();
        }
    }
    public static void main(String[] args) throws IOException{
        // solution.first();   
        // solution.second();
        // solution.third();
        solution.fourth();
    }
}
