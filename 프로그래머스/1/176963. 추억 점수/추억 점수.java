import java.util.Arrays;
import java.util.List;

class Solution {
    public static int[] solution(String[] name, int[] yearning, String[][] photo) {
        int[] answer = new int[photo.length];
        int idx = 0;

        List<String> name_list = Arrays.asList(name);

        for (String[] i : photo) {
            int count = 0;
            for (String j : i) {
                try {
                    count += yearning[name_list.indexOf(j)];
                } catch (Exception e){
                    //System.out.println(e);
                }
            }
            answer[idx] = count;
            idx ++;
        }
        return answer;
    }

    public static void main(String[] args) {

        String[] name = {"may", "kein", "kain", "radi"};
        int[] yearning = {5, 10, 1, 3};
        String[][] photo = {{"may", "kein", "kain", "radi"}, {"may", "kein", "brin", "deny"}, {"kon", "kain", "may", "coni"}};

        System.out.println(Arrays.toString(solution(name, yearning, photo)));
    }
}