import java.util.Arrays;

class Solution {
    public int[] solution(String[] keyInput, int[] board) {
        int[] answer = {0, 0};
        int width = board[0] / 2;
        int height = board[1] / 2;

        for (String key : keyInput) {
            if ("left".equals(key) && width >= Math.abs(answer[0] - 1)) {
                answer[0] -= 1;
            } else if ("right".equals(key) && width >= Math.abs(answer[0] + 1)) {
                answer[0] += 1;
            } else if ("up".equals(key) && height >= Math.abs(answer[1] + 1)) {
                answer[1] += 1;
            } else if ("down".equals(key) && height >= Math.abs(answer[1] - 1)) {
                answer[1] -= 1;
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        Solution T = new Solution();
        String[] keyInput = {"left", "left", "left", "right"};
        int[] board = {3, 3};

        System.out.println(Arrays.toString(T.solution(keyInput, board)));
    }
}
