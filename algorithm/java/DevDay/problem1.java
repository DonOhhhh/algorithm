import java.util.*;

public class problem1 {

    public static int solution(String s) {
        String[] inputs = s.split(" ");
        Stack<String> history = new Stack<>();
        Stack<String> backup = new Stack<>();
        Map<String,Integer> count = new HashMap<>();
        for(String input : inputs)
        {
            try
            {
                if(input.equals("B")) backup.push(history.pop());
                else if(input.equals("F")) history.push(backup.pop());
                else
                {
                    history.push(input);
                    backup.clear();
                }
            }
            catch(EmptyStackException e) {}
            try
            {
                if(!count.containsKey(history.peek())) count.put(history.peek(), 0);
                count.replace(history.peek(),count.get(history.peek())+1);
            }
            catch(EmptyStackException e) {}
            // System.out.println(history.stream().collect(Collectors.joining(" ")));
        }
        return count.values().stream().mapToInt(Integer::intValue).max().getAsInt();
    }

    public static void main(String[] args) {
        String s = new Scanner(System.in).nextLine();
        System.out.println(solution(s));
    }
}
