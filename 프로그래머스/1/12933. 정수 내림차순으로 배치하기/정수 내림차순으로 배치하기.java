class Solution {
    public long solution(long n) {
        StringBuilder answer = new StringBuilder();
        int[] count = new int[10];
        String s = String.valueOf(n);

        for (int i = 0; i < s.length(); i++) {
            count[Character.getNumericValue(s.charAt(i))] += 1;
        }

        for (int i = 0; i < count.length; i++) {
            answer.append(String.valueOf(i).repeat(Math.max(0, count[i])));
        }
        return Long.parseLong(answer.reverse().toString());
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        long n = 118372;

        System.out.println(solution.solution(n));
    }
}
