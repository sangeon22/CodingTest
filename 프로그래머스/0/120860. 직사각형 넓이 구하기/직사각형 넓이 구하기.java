import java.util.Arrays;
import java.util.OptionalInt;

class Solution {
    public int solution(int[][] dots) {
        int max_x = Arrays.stream(dots)
                .mapToInt(row -> row[0])
                .max()
                .getAsInt();

        int min_x = Arrays.stream(dots)
                .mapToInt(row -> row[0])
                .min()
                .getAsInt();

        int max_y = Arrays.stream(dots)
                .mapToInt(row -> row[1])
                .max()
                .getAsInt();

        int min_y = Arrays.stream(dots)
                .mapToInt(row -> row[1])
                .min()
                .getAsInt();

        return (max_x - min_x) * (max_y - min_y);
    }

    public static void main(String[] args) {
        Solution T = new Solution();
        int[][] dots = {{1, 1}, {2, 1}, {2, 2}, {1, 2}};

        System.out.println(T.solution(dots));
    }
}
