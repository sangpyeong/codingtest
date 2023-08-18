import java.util.*;

class Solution {
    int MOD = 20170805;
    public int solution(int m, int n, int[][] cityMap) {
        
        int[][] dp = new int[m][n];
        dp[0][0] = 1;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(cityMap[i][j]==0 || cityMap[i][j]==2){
                    int ti = i - 1;
                    int tj = j - 1;
                    while(ti >= 0 && cityMap[ti][j] == 2){
                        ti--;
                    }
                    while(tj >= 0 && cityMap[i][tj] == 2){
                        tj--;
                    }
                    if(ti >= 0){
                        dp[i][j] += dp[ti][j];
                    }
                    if(tj >= 0){
                        dp[i][j] += dp[i][tj];
                    }
                    dp[i][j] = dp[i][j]%MOD;
                    
                }
                else if(cityMap[i][j] == 1){
                    dp[i][j] = 0;
                }
            }
        }
        return dp[m-1][n-1];
    }
}