import java.util.Arrays;

class Solution {
    public int[] solution(long n) {
        StringBuilder sb = new StringBuilder(String.valueOf(n));
        int[] answer = new int[sb.length()];

        for (int i = sb.length() - 1; i >= 0; i--) {
            answer[sb.length() - (i + 1)] = Character.getNumericValue(sb.charAt(i));
        }
        return answer;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        long n = 12345;

        System.out.println(Arrays.toString(solution.solution(n)));
    }
}
