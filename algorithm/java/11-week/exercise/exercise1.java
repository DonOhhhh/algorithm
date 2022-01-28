import java.util.*;
import java.util.stream.*;

public class exercise1 {

    public static String inorder(Map<String,String[]> tree, String root) {
        String result = "";
        if(!tree.get(root)[0].equals(".")) result += inorder(tree, tree.get(root)[0]);
        result += root;
        if(!tree.get(root)[1].equals(".")) result += inorder(tree, tree.get(root)[1]);
        return result;
    }

    public static String preorder(Map<String,String[]> tree, String root) {
        String result = "";
        result += root;
        if(!tree.get(root)[0].equals(".")) result += preorder(tree, tree.get(root)[0]);
        if(!tree.get(root)[1].equals(".")) result += preorder(tree, tree.get(root)[1]);
        return result;
    }

    public static String postorder(Map<String,String[]> tree, String root) {
        String result = "";
        if(!tree.get(root)[0].equals(".")) result += postorder(tree, tree.get(root)[0]);
        if(!tree.get(root)[1].equals(".")) result += postorder(tree, tree.get(root)[1]);
        result += root;
        return result;
    }

    public static String levelorder(Map<String,String[]> tree, String root) {
        List<String> visited = new ArrayList<>();
        Queue<String> q = new LinkedList<>();
        q.add(root);
        
        while(q.size()>0)
        {
            String tmp = q.poll();
            if(!visited.contains(tmp) && !tmp.equals("."))
            {
                visited.add(tmp);
                q.addAll(Arrays.stream(tree.get(tmp)).toList());
            }
        }
        
        return visited.stream().collect(Collectors.joining(""));
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        String[][] nodes = IntStream.range(0, n).mapToObj(i -> sc.nextLine().split(" ")).toArray(String[][]::new);
        Map<String,String[]> tree = new HashMap<>();
        for(String[] node : nodes)
            tree.put(node[0],new String[]{node[1],node[2]});
        System.out.println(preorder(tree, nodes[0][0]));            
        System.out.println(inorder(tree, nodes[0][0]));
        System.out.println(postorder(tree, nodes[0][0]));
        System.out.println(levelorder(tree, nodes[0][0]));
    }
}
