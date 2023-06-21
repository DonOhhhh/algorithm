import java.util.regex.*;
import java.util.stream.IntStream;
import java.util.*;

public class training1 {
    public static void main(String[] args) {
        Pattern pattern = Pattern.compile("(\\d+)([SDT])([*#]?)");
        Matcher matcher = pattern.matcher(new Scanner(System.in).nextLine());
        int[] scores = new int[matcher.groupCount()];
        for(int i = 0 ; matcher.find() ; i++)
        {
            if(matcher.group(2).equals("D"))
                scores[i] = (int)Math.pow(Integer.parseInt(matcher.group(1)), 2);
            else if(matcher.group(2).equals("T"))
                scores[i] = (int)Math.pow(Integer.parseInt(matcher.group(1)), 3);
            else
                scores[i] = Integer.parseInt(matcher.group(1));
            
            try
            {
                if(matcher.group(3).equals("*"))
                {
                    if(i!=0)
                    {
                        scores[i-1] *= 2;
                        scores[i] *= 2;
                    }
                    else
                    {
                        scores[i] *= 2;
                    }
                }
                else if(matcher.group(3).equals("#"))
                {
                    scores[i] *= -1;
                }
            }
            catch(ArrayIndexOutOfBoundsException e){}
        }
        System.out.println(Arrays.stream(scores).reduce(Integer::sum).getAsInt());
    }
}
