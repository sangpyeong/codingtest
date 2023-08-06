import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        //큐에 남은 시간들을 넣음, 맨압 남은 시간보다 작으면 poll, 결과 구함
        Queue<Integer> q = new LinkedList<>();
        for(int i=0;i<progresses.length;i++){
            q.add((100 - progresses[i]) % speeds[i] == 0 ? (100 - progresses[i]) / speeds[i]:(100 - progresses[i]) / speeds[i] + 1);
        }
        while(!q.isEmpty()){
            int num = 1;
            int current = q.poll();
            
            while (q.peek() != null && q.peek() <= current){
                num++;
                q.poll();
            }
            answer.add(num);
        }
        int[] result = new int[answer.size()];
        for (int i = 0; i < answer.size(); i++) {
            result[i] = answer.get(i);
        }
        return result;
    }
}