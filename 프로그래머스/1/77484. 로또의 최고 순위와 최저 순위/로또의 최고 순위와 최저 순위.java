import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;

class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[2];
        int[] rank = {6, 6, 5, 4, 3, 2, 1};
        int lottosZeroCount = 0;

        HashSet<Integer> lottosSet = new HashSet<Integer>();
        HashSet<Integer> winNumsSet = new HashSet<Integer>();

        for (int i : lottos) {
            lottosSet.add(i);
            if (i == 0) {
                lottosZeroCount++;
            }
        }

        for (int j : win_nums) {
            winNumsSet.add(j);
        }

        // lottos_set과 win_nums_set의 교집합
        lottosSet.retainAll(winNumsSet);

        int HitsCount = lottosSet.size();
        answer[0] = rank[HitsCount + lottosZeroCount];
        answer[1] = rank[HitsCount];

        return answer;
    }

    public static void main(String[] args) {
        int[] lottos = {44, 1, 0, 0, 31, 25};
        int[] win_nums = {31, 10, 45, 1, 6, 19};
        Solution solution = new Solution();

        System.out.println(Arrays.toString(solution.solution(lottos, win_nums)));
    }
//    [44, 1, 0, 0, 31, 25]	[31, 10, 45, 1, 6, 19]	[3, 5]
}