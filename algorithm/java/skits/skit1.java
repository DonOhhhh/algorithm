import java.util.*;
import java.util.stream.Collectors;
import java.io.*;

public class skit1 {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        Integer[][] test = {{0,1},{0,2},{0,3},{0,4}};
        Integer[] tmp = {0,1};
        int[] result = Arrays.stream(test).flatMapToInt(data -> Arrays.stream(data).mapToInt(Integer::intValue)).distinct().toArray();
        System.out.println();
    }
}
