import java.util.Arrays;
import java.util.Collections;
import java.util.List;

class Solution {
    public static String solution(String s) {
        String answer = "";
        StringBuilder sb = new StringBuilder();

        char[] a = s.toCharArray();
        Arrays.sort(a);
        sb.append(a);
        sb.reverse();

        return sb.toString();
    }

    public static void main(String[] args) {
        String s = "Zbcdefg";

        System.out.println(solution(s));
    }
}