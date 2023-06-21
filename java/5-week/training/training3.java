import java.util.Scanner;

public class training3 {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder str = new StringBuilder(sc.nextLine());
        System.out.println(str.toString().equals(str.reverse().toString()) ? true : false);
    }
}
