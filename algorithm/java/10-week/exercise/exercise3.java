import java.util.*;
import java.util.function.Supplier;
import java.util.stream.*;

public class exercise3 {

    static int[] node;

    public static void bfs(Deque<int[]> answer, Set<int[]> tmp, int[] node)
    {
        // 노드가 연결된건지 확인하기 위한 리스트를 생성하고 node의 출발점을 선정해서 추가한다.
        List<Integer> visited = new ArrayList<>();
        visited.add(node[0] > node[1] ? node[1] : node[0]);
        // 다음 노드들을 저장하기 위한 리스트
        TreeSet<Integer> nextNode = new TreeSet<>();
        nextNode.add(node[0]);
        nextNode.add(node[1]);
        // nextNode의 값을 1개씩 빼오면서 해당 노드에 연결된 모든 edge들을 tmp에 중복없이 저장한다.
        while(nextNode.size() > 0)
        {
            int startNode = nextNode.pollFirst();
            Supplier<Stream<int[]>> tmpStream = () -> answer.stream().filter(i -> i[0]==startNode || i[1]==startNode);
            if(tmpStream.get().count()==0) continue;
            tmp.addAll(tmpStream.get().toList());
            visited.add(startNode);
            nextNode.addAll(tmpStream.get().flatMap(i->Stream.of(i[0],i[1])).filter(j->!visited.contains(j)).toList());
        }
    }
 
    public static int[][] buildVillage(Map<Integer, List<int[]>> graph, int[] baseCost)
    {
        PriorityQueue<int[]> q = new PriorityQueue<>((int[] i1, int[] i2)->i1[2] > i2[2] ? 1 : -1);
        Deque<int[]> answer = new LinkedList<>();
        
        // graph에서 각 key마다 연결된 노드가 있으면 정답 리스트에 추가한다. 만약 key가 이미 정답 리스트의 노드에 있다면 추가하지 않는다.
        for(Integer key : graph.keySet())
        {
            q.clear();
            q.addAll(graph.get(key));
            if(answer.stream().anyMatch(arr -> arr[0]==key || arr[1]==key)) continue;
            answer.add(q.poll());
        }

        // 새로운 정답이 저장될 리스트
        List<int[]> newAnswer = new LinkedList<>();
        // 연결된 그룹이 저장될 리스트
        Set<int[]> tmp = new HashSet<>();

        while(answer.size()>0)
        {
            // answer에서 값을 1개씩 빼온다.
            node = answer.pollFirst();
            // 그 노드가 newAnswer 리스트에 존재한다면 넘어가고 존재하지 않는다면 조건문을 실행한다.
            if(newAnswer.stream().anyMatch(arr->Arrays.equals(arr, node))) continue;
            
            // 먼저 tmp 출발점과 도착점이 같지 않은 노드를 추가하고 answer리스트를 돌면서 그 노드와 연결된 다른 노드들을 tmp에 추가한다.
            // 왜냐하면 한 노드에 연결된 모든 노드를 알아내기 위해서이다.
            tmp.clear();
            tmp.add(node);
            // bfs를 이용하여 연결된 그룹들을 모두 찾아냄.
            bfs(answer,tmp,node);
            // 만약 연결된 모든 노드들 중에 출발점과 도착점이 같은 노드가 존재하지 않는다면 연결된 그룹에 기지국이 없다는 말이므로
            // tmp리스트에서 출발점과 도착점을 가져다가 중복값을 제거하고 남은 노드들 중 자기자신에 기지국을 세우는 비용이 가장 싼 노드를 baseCose에서 가져다가 newAnswer에 추가한다.
            if(!tmp.stream().anyMatch(i->i[0]==i[1]))
                newAnswer.add(tmp.stream().flatMap(i -> Stream.of(i[0],i[1])).distinct().map(j->new int[]{j,j,baseCost[j-1]}).min((a,b)->a[2]>b[2]?1:-1).get());
            // 그리고 연결된 그룹을 newAnswer에 전부 추가한다.
            newAnswer.addAll(tmp);
            
        }

        // 거리 순으로 정렬하여 리턴한다.
        return newAnswer.stream().sorted((a,b)->a[2]>b[2]?1:-1).toArray(int[][]::new);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] ve = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int[] baseCost = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int[][] edgeCost = IntStream.range(0, ve[1]).mapToObj(i -> Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray()).toArray(int[][]::new);
        
        Map<Integer, List<int[]>> graph = new HashMap<>();
        for(int[] edge : edgeCost)
        {
            if(!graph.containsKey(edge[0])) graph.put(edge[0],new ArrayList<>());
            graph.get(edge[0]).add(edge);

            if(!graph.containsKey(edge[1])) graph.put(edge[1],new ArrayList<>());
            graph.get(edge[1]).add(edge);
        }
        for(int i = 0 ; i < baseCost.length ; i++)
        {
            if(!graph.containsKey(i+1)) graph.put(i+1, new ArrayList<>());
            graph.get(i+1).add(new int[]{i+1,i+1,baseCost[i]});
        }

        int[][] answer = buildVillage(graph, baseCost);
        int mstCost = Arrays.stream(answer).map(arr -> arr[2]).reduce(Integer::sum).get();
        System.out.print(mstCost + ", " + Arrays.stream(answer).map(Arrays::toString).collect(Collectors.joining(", ","[","]")));
    }
}
