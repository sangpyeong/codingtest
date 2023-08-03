import java.util.*;

class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] visited = new boolean[n];
        
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                bfs(i, computers, visited);
                answer += 1;
            }
        }
        
        return answer;
    }

    public void bfs(int start, int[][] computers, boolean[] visited) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(start);
        
        while (!queue.isEmpty()) {
            int current = queue.poll();
            visited[current] = true;

            for (int i = 0; i < computers[current].length; i++) {
                if (i != current && computers[current][i] == 1 && !visited[i]) {
                    queue.add(i);
                }
            }
        }
    }
}
