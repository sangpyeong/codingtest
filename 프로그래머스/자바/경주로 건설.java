// import java.util.*;

// class Solution {
//     public int solution(int[][] board) {
//         int answer = 0;
//         int n = board.length;
//         int[][] dp = new int[n][n];
//         for(int i=0;i<n;i++){
//             for(int j=0;j<n;j++){
//                 dp[i][j] = 1000000000;
//             }
//         }
//         dp[0][0] = 0;
//         int[] dx = {-1, 0, 1, 0};
//         int[] dy = {0, 1, 0, -1};
//         Queue<int[]> q = new LinkedList<>();
//         int[] start = {0, 0, 0};
//         q.add(start);
//         while(!q.isEmpty()){
//             int[] point = q.poll();
           
//             for(int i=0;i<4;i++){
//                 int nx = point[0] + dx[i];
//                 int ny = point[1] + dy[i];
//                 if(nx < 0 || nx >= n || ny < 0 || ny >= n){
//                     continue;
//                 }
//                 if(board[nx][ny] == 1){
//                     continue;
//                 }
                
//                 int next = dp[point[0]][point[1]] + 100;
//                 if(point[2] != i){
//                     next += 500;
//                 }
//                 if(next > dp[nx][ny]){
//                     continue;
//                 }
//                 if(nx == 1 && ny ==0){
//                     next -= 500;
//                 }
//                 if(nx == 0 && ny == 1){
//                     next -= 500;
//                 }
//                 if(point[2] != i){
//                     int bx = point[0] - dx[i];
//                     int by = point[1] - dy[i];
//                     if(bx >= 0 && bx < n && by >=0 && by < n && dp[bx][by] + 200 < next){
//                         dp[nx][ny] = dp[bx][by] + 200;
//                         int[] ns = {nx, ny, i};
//                         q.add(ns);
//                         continue;
//                     }
//                 }
                
//                 dp[nx][ny] = next;
                
//                 int[] ns = {nx, ny, i};
//                 q.add(ns);
//             }
//         }
//         System.out.println(Arrays.deepToString(dp));
//         answer = dp[n-1][n-1];
//         return answer;
//     }
// }


import java.util.Queue;
import java.util.LinkedList;
import java.io.*;

public class RaceTrack {
    static int[][][] price;
    static int N;
    static int[][] move = { {-1,0}, {1,0}, {0,-1}, {0,1} }; // 상하좌우

    static int solution(int[][] board) {
        N = board.length;
        price = new int[4][N][N]; // 방향, 행, 열
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++) {
                price[0][i][j] = Integer.MAX_VALUE; price[1][i][j] = Integer.MAX_VALUE;
                price[2][i][j] = Integer.MAX_VALUE; price[3][i][j] = Integer.MAX_VALUE;
            }
        }
        Queue<int[]> q = new LinkedList<>();
        if(board[1][0]==0){
            price[1][1][0] = 100;
            q.add(new int[]{1,0,1});
        }
        if(board[0][1]==0){
            price[3][0][1] = 100;
            q.add(new int[]{0,1,3});
        }

        while(!q.isEmpty()){
            int[] cur = q.poll();
            int cRow = cur[0];  int cCol = cur[1];  int cDir = cur[2];

            for(int nDir=0; nDir<4; nDir++){
                int nRow = cRow + move[nDir][0]; int nCol = cCol + move[nDir][1];
                if(!isInRange(nRow, nCol) || board[nRow][nCol]==1)   continue;
                if(cDir!=nDir) { // 방향이 달라질 경우
                    if(cDir+nDir==1 || cDir+nDir==5)  continue; // 역방향으로 돌아가면 넘겨
                    if(price[nDir][nRow][nCol]<price[cDir][cRow][cCol]+600) continue;
                    q.add(new int[]{nRow,nCol,nDir});
                    price[nDir][nRow][nCol] = price[cDir][cRow][cCol] + 600;
                }
                else{ // 직선으로 갈 경우
                    if(price[nDir][nRow][nCol]<price[cDir][cRow][cCol]+100) continue;
                    q.add(new int[]{nRow, nCol, nDir});
                    price[nDir][nRow][nCol] = price[cDir][cRow][cCol] + 100;
                }
            }
        }
        int result = Integer.MAX_VALUE;
        for(int i=0; i<4; i++)
            result = (result>price[i][N-1][N-1] ? price[i][N-1][N-1]:result);
        return result;
    }

    static Boolean isInRange(int row, int col){
        if(row<0 || row>=N || col<0 || col>=N)  return false;
        return true;
    }
}