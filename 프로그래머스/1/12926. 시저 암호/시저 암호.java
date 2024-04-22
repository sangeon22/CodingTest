import java.util.Arrays;
import java.util.Collections;
import java.util.List;

class Solution {
    public String solution(String s, int n) {
        StringBuilder sb = new StringBuilder();
        char[] charArray = s.toCharArray();
        for (char i : charArray) {
            // 공백은 그대로 sb에 append
            if (Character.isWhitespace(i)) {
                sb.append(i);
                continue;
            }

            int temp = i + n;

            if (Character.isLowerCase(i)) {
                if (temp > 122) {
                    temp -= 26;
                }
            } else if (Character.isUpperCase(i)) {
                if (temp > 90) {
                    temp -= 26;
                }
            }
            sb.append(Character.toString(temp));
        }

        return sb.toString();
    }

    public static void main(String[] args) {
        String s = "P";
        int n = 15;
        Solution solution = new Solution();

        System.out.println(solution.solution(s, n));
    }
}