import java.util.ArrayList;
import java.util.List;
class Solution {
    static class Node{
		int data;
		int left, right;
		public Node(int data, int left, int right) {
			this.data = data;
			this.left = left;
			this.right = right;
		}
	}
    static int INF = 789654321, MAX_SECTION =10001;
    static List<Node>[] list;
    static int[][] cost;
    public int solution(int k, int[] num, int[][] links) {
        int size = num.length;
        list = new ArrayList[size];
        for(int i=0; i<size; i++) {
            list[i] = new ArrayList<>();
        }
        int sum = 0;
        boolean[] check = new boolean[size];
        for(int i=0; i<size; i++) {
            int left = links[i][0];
            int right = links[i][1];
            if(left != -1) check[left] = true;
            if(right != -1) check[right] = true;
            list[i].add(new Node(num[i], left, right));
            sum += num[i];
        }	

        int root = -1;
        for(int i=0; i<size; i++) {
            if(!check[i]) root = i;
        }

        int left = sum/k;
        int right = sum;
        if(left == right) return right;
        while(left < right) {
            int mid = (left+right)/2;
            cost = new int[size][2];
            traversal(root, mid);
            if(cost[root][0] <= k) {
                right = mid;
            }else {
                left = mid+1;
            }
        }
        return right;

    }

    static void traversal(int pos, int w) {
        Node curNode = list[pos].get(0);
        int data = curNode.data;
        int l = curNode.left;
        int r = curNode.right;

        if(l != -1) traversal(l,w);
        if(r != -1) traversal(r,w);
        // leaf 노드 
        if(l == -1 && r== -1) {
            if(data <= w) {
                cost[pos][0] = 1;
                cost[pos][1] = data;
            }else {
                cost[pos][0] = MAX_SECTION;
                cost[pos][1] = INF;
            }
        }
        // full 노드 
        else if(l!=-1&&r!=-1){
            // 1) pos + 왼쪽 트리 + 오른쪽 트리 <= L 
            // section l+r-1
            if(data + cost[l][1] + cost[r][1] <=w) {
                cost[pos][0] = cost[l][0] + cost[r][0] -1;
                cost[pos][1] = data + cost[l][1] + cost[r][1];
            }
            // 2) pos + min(왼쪽, 오른쪽)  <= L
            // section  l+r
            else if(data + Math.min(cost[l][1],cost[r][1]) <= w) {
                cost[pos][0] = cost[l][0] + cost[r][0];
                cost[pos][1] = data + Math.min(cost[l][1], cost[r][1]);
            }
            // 3) pos <= L
            // section  l+r +1
            else if(data <= w) {
                cost[pos][0] = cost[l][0] + cost[r][0] +1;
                cost[pos][1] = data;
            }
            else {
                cost[pos][0] = MAX_SECTION;
                cost[pos][1] = INF;
            }
        }else {
            // 왼쪽 자식만 있는 경우
            if(r == -1) {
                // 1) pos + 왼쪽 트리 <= L
                // section l 
                if(data + cost[l][1] <=w) {
                    cost[pos][0] = cost[l][0];
                    cost[pos][1] = data + cost[l][1];
                }
                // 1) pos <= L
                // section l +1  
                else if(data <= w) {
                    cost[pos][0] = cost[l][0]+1;
                    cost[pos][1] = data;
                }
                else {
                    cost[pos][0] = MAX_SECTION;
                    cost[pos][1] = INF;
                }
            }

            // 오른쪽 자식만 있는 경우
            if(l == -1) {
                // 1) pos + 오른쪽 트리 <= L
                // section r 
                if(data + cost[r][1] <=w) {
                    cost[pos][0] = cost[r][0];
                    cost[pos][1] = data + cost[r][1];
                }
                // 1) pos <= L
                // section r +1  
                else if(data <= w) {
                    cost[pos][0] = cost[r][0]+1;
                    cost[pos][1] = data;
                }
                else {
                    cost[pos][0] = MAX_SECTION;
                    cost[pos][1] = INF;
                }
            }
        }
    }
}

