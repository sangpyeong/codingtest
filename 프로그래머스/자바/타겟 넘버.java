class Solution {
    static int len;
    static int tar;
    static int answer;
    static int[] nums;
    public int solution(int[] numbers, int target) {
        answer = 0;
        nums = numbers;
        len = numbers.length;
        tar = target;
        
        dfs(0, 0);
        
        return answer;
    }
    
    public void dfs(int idx, int result){
        //종결조건
        if (idx == len){
            if (result == tar){
                answer += 1;
            }
            return;
        }
        
        dfs(idx+1, result+nums[idx]);
        dfs(idx+1, result-nums[idx]);
        
    }
}

class Solution_other {
    int answer = 0;

    public int solution(int[] numbers, int target) {
        dfs(numbers, 0, target, 0);

        return answer;
    }

    // 깊이 우선 탐색
    public void dfs(int[] numbers, int depth, int target, int sum){
        if(depth == numbers.length){ // 마지막 노드 까지 탐색한 경우
            if(target == sum) answer++;
        } else {
            dfs(numbers, depth + 1, target, sum + numbers[depth]); // 해당 노드의 값을 더하고 다음 깊이 탐색
            dfs(numbers, depth + 1, target, sum - numbers[depth]); // 해당 노드의 값을 빼고 다음 깊이 탐색
        }
    }
}