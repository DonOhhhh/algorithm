import java.util.Arrays;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class training2 {
    public static void main(String[] args) {
        Pattern pattern = Pattern.compile("(\\D+)(\\d+)");
        String[] inputs = Arrays.stream(new Scanner(System.in).nextLine().split(", ")).sorted((a,b)->{
            Matcher matA = pattern.matcher(a.toLowerCase());
            matA.find();
            Matcher matB = pattern.matcher(b.toLowerCase());
            matB.find();
            if(!matA.group(1).equals(matB.group(1))) return matA.group(1).compareTo(matB.group(1));
            if(Integer.parseInt(matA.group(2)) != Integer.parseInt(matB.group(2))) return Integer.parseInt(matA.group(2)) > Integer.parseInt(matB.group(2)) ? 1 : -1;
            return 0;
        }).toArray(String[]::new);
        System.out.println(Arrays.asList(inputs));
    }
}