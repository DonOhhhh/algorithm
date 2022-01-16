import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.stream.IntStream;
import static org.junit.Assert.*;
import org.junit.Test;

public class tester {

    public static String myinput1(String path) throws IOException
    {
        BufferedInputStream bis = new BufferedInputStream(new FileInputStream(path));
        byte[] buf = bis.readAllBytes();
        StringBuilder sb = new StringBuilder("");
        for(byte a : buf)
        {
            if(a==13) continue;
            if(a==10)
            {
                sb.append("\n");
                continue;
            } 
            sb.append(String.valueOf((char)a));
        }
        return sb.toString();
    }

    public static String myinput2(String path) throws IOException
    {
        FileReader fr = new FileReader(path);
        // FileInputStream fis = new FileInputStream("D:\\Programming\\algorithm\\java\\7-week\\training\\inputs3.txt");
        char[] buf = new char[10000];
        fr.read(buf);

        StringBuilder sb = new StringBuilder("");
        for(char a : buf)
        {
            if((byte)a==13) continue;
            if((byte)a==10)
            {
                sb.append("\n");
                continue;
            } 
            sb.append(String.valueOf(a));
        }
        return sb.toString();
    }

    public static String[] myinput3(String path) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream(path)));
        String s;
        StringBuilder sb = new StringBuilder("");
        ArrayList<String> arrayList = new ArrayList<>();
        while((s=br.readLine())!=null)
        {
            if(s.strip().equals(""))
            {
                arrayList.add(sb.toString().strip());
                sb = new StringBuilder("");
            }
            else
            {
                sb.append(s.strip()+"\n");
            }
        }
        return arrayList.toArray(String[]::new);
    }

    public static String execCmd(String[] cmd) {
        try {
            Process process = Runtime.getRuntime().exec(cmd);
            BufferedReader reader = new BufferedReader(
                    new InputStreamReader(process.getInputStream()));
            String line = null;
            StringBuffer sb = new StringBuffer();
            sb.append(cmd);
            while ((line = reader.readLine()) != null) {
                sb.append(line);
                sb.append("\n");
            }
            return sb.toString();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }

    @Test
    public static void test(String input, String answer)
    {
        assertEquals(answer,0);
    }

    public static void main(String[] args) throws IOException{
        String path = "D:\\Programming\\algorithm\\java\\7-week\\training\\inputs4.txt";
        String[] result = myinput3(path);
        String[][] processed = IntStream.range(0, result.length).filter(i -> i%2==0).mapToObj(i -> new String[]{result[i],result[i+1]}).toArray(String[][]::new);
        // Arrays.stream(processed).forEach(arr -> System.out.println(arr[0] + "\n" + arr[1] + "\n"));
        for(String[] data : processed)
        {
            test(data[0],data[1]);
        }
    }
}
