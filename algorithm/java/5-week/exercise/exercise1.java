import java.util.Arrays;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.IntStream;

public class exercise1 {
    public static void main(String[] args)
    {
        Matcher inputs = Pattern.compile("(\\d+)([SDT])([*#]?)").matcher(new Scanner(System.in).nextLine());
        int[] scores = new int[inputs.groupCount()];
        String[] patterns = IntStream.range(0, scores.length).mapToObj(i -> {
            inputs.find();
            return inputs.group();
        }).toArray(String[]::new);

        for(int i = scores.length-1 ; i>=0 ; i--)
        {
            Matcher matcher = Pattern.compile("(\\d+)([SDT])([*#]?)").matcher(patterns[i]);
            matcher.find();
            int num = Integer.parseInt(matcher.group(1));
            switch(matcher.group(2).charAt(0))
            {
                case 'S':
                    scores[i] = num;
                    break;
                case 'D':
                    scores[i] = (int)Math.pow(num, 2);
                    break;
                case 'T':
                    scores[i] = (int)Math.pow(num, 3);
                    break;
                default:
                    break;
            }
            try {
                char special = matcher.group(3).charAt(0);
                switch(special)
                {
                    case '*':
                        scores[i] *= 2;
                        scores[i+1] *= 2;
                        break;
                    case '#':
                        scores[i] *= -1;
                        break;
                }
            } catch (Exception e) {
                //TODO: handle exception
            }
        }
        System.out.println(Arrays.stream(scores).reduce(Integer::sum).getAsInt());
    }
}
