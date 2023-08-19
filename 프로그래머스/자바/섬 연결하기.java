import java.util.*;

class Solution {
    
    public int find(int n, int[] parent){
        if(parent[n] == n){
            return n;
        }
        return find(parent[n],parent);
    }
    public boolean posible(int start, int end, int[] parent){
        int p1 = find(start, parent);
        int p2 = find(end, parent);
        
        if(p1 == p2){
            return false;
        }
        else{
            if(p1 < p2){
                parent[p2] = p1;
            }
            else{
                parent[p1] = p2;
            }
            return true;
        }
    }
    
    
    
    public int solution(int n, int[][] costs) {
        int answer = 0;
        
        int[] parent = new int[n];
        for(int i=0;i<n;i++){
            parent[i] = i;
        }
        Arrays.sort(costs, new Comparator<int[]>(){
            @Override
            public int compare(int[] a1, int[] a2){
                return a1[2] - a2[2];
            }
        });
        for(int i=0;i<costs.length;i++){
            if(posible(costs[i][0], costs[i][1], parent)){
                answer+=costs[i][2];
            }
            
        }
    
        
        return answer;
    }
}