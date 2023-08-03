import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int answer = 0;
        int n = maps.length;
        int m = maps[0].length;
        
        int[] dx = {0, 1, 0, -1};
        int[] dy = {1, 0, -1, 0};
        
        int[][] visited = new int[n][m];
        
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{0, 0});
        visited[0][0] = 1;
        
        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int x = current[0];
            int y = current[1];
            
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                if (nx >= 0 && nx < n && ny >= 0 && ny < m && maps[nx][ny] == 1 && visited[nx][ny] == 0) {
                    queue.add(new int[]{nx, ny});
                    visited[nx][ny] = visited[x][y] + 1;
                }
            }
        }
        
        answer = visited[n - 1][m - 1] != 0 ? visited[n - 1][m - 1] : -1;
        
        return answer;
    }
}
