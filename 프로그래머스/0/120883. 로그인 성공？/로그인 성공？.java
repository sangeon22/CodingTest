import java.util.Arrays;
import java.util.OptionalInt;

class Solution {
    public String solution(String[] idPw, String[][] db) {
        String answer = "fail";
        for (String[] row : db){
            if (idPw[0].equals(row[0])){
                if (idPw[1].equals(row[1])){
                    answer = "login";
                    break;
                }
                answer = "wrong pw";
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        Solution T = new Solution();
        String[] idPw = {"meosseugi", "1234"};
        String[][] db = {{"rardss", "123"}, {"yyoom", "1234"}, {"meosseugi", "1234"}};


        System.out.println(T.solution(idPw, db));
    }
}
