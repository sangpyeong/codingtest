import java.util.*;

class Solution {
    public int solution(String begin, String target, String[] words) {
        int answer = 0;
        
        Queue<String> queue = new LinkedList<>();
        queue.add(begin);
        int[] visited = new int[words.length];
        
        while (!queue.isEmpty()){
            String current = queue.poll();
            
            if (current.equals(target)){
                System.out.println(Arrays.toString(visited));
                return visited[Arrays.asList(words).indexOf(target)];
            }
            
            for(int i = 0; i < words.length; i++){
                int diffCount = 0;
                for (int j = 0; j < current.length(); j++) {
                    if (current.charAt(j) != words[i].charAt(j)) {
                        diffCount++;
                    }
                }
                
                if (diffCount == 1 && visited[i] == 0){
                    queue.add(words[i]);
                    if (Arrays.asList(words).indexOf(current) >= 0){
                        visited[i] = visited[Arrays.asList(words).indexOf(current)] + 1;
                    }
                    else{
                        visited[i] = 1;
                    }
                }
            }
        }
        
        return answer;
    }
}