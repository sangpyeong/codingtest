import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        
        Deque<String> dq = new ArrayDeque<>();
        for(int i=0;i<s.length();i++){
            if (s.charAt(i) == '('){
                dq.push("(");
            }
            else if(!dq.isEmpty() && s.charAt(i) == ')'){
                dq.pop();
            }
            else{
                return false;
            }
        }
        if(!dq.isEmpty()){
            return false;
        }
        
        return answer;
    }
}