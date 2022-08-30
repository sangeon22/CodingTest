import java.util.Arrays;

class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        for(int i=0; i<10; i++){
            boolean b = contains(numbers, i);
            if(!b){
                answer += i;
            }
        }
        return answer;
    }
    
    public boolean contains(int arr[], int key){
        return Arrays.stream(arr).anyMatch(i -> i ==key);
    }
}