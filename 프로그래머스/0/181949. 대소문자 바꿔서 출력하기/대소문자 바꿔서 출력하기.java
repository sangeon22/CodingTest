import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        StringBuilder answer = new StringBuilder();

        for (int i = 0; i < str.length(); i++) {
            if (Character.isUpperCase(str.charAt(i))){
                answer.append(Character.toLowerCase(str.charAt(i)));
                continue;
            }
            answer.append(Character.toUpperCase(str.charAt(i)));
        }
        System.out.println(answer);
    }
}