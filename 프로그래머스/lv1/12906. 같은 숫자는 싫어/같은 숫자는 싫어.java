import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        ArrayList<Integer> li = new ArrayList<Integer>();
        int num = -1;
        
        
        for (int i : arr){
            if (i != num){
                li.add(i);
                num = i;
            }
        }
        int answer[] = new int[li.size()];
        int a = 0;
        for (int j :li){
            answer[a] = j;
            a++;
        }
        return answer;
    }
}