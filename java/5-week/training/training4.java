import java.util.Scanner;

public class training4 {

    public static boolean isPalindrome(String s)
    {
        StringBuilder str = new StringBuilder(s);
        return str.toString().equals(str.reverse().toString()) ? true : false;
    }

    public static int lps(String str)
    {
        String[] words = str.split("");
        int result = Integer.MIN_VALUE;
        int cnt;
        // odd length
        for(int i = 1 ; i < words.length-1 ; i++)
        {
            cnt = 1;
            for(int j = 1 ; (i-j) >= 0 && (i+j) < words.length ; j++)
            {
                if(!words[i-j].equals(words[i+j])) break;
                cnt+=2;
            }
            if(cnt > result) result = cnt;
            if(cnt!=1) i += (int)(cnt/2);
        }
        // even length
        for(int i = 0 ; i < words.length ; i++)
        {
            cnt = 0;
            for(int j = 0 ; (i-j) >= 0 && (i+1+j) < words.length ; j++)
            {
                if(!words[i-j].equals(words[i+1+j])) break;
                cnt+=2;
            }
            if(cnt > result) result = cnt;
            if(cnt!=0) i += ((int)(cnt/2));
        }

        return result;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        System.out.println(lps(str));
    }
}
