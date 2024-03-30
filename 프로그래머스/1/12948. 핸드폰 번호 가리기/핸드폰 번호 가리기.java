class Solution {
    public static StringBuilder solution(String phoneNumber) {
        StringBuilder sb = new StringBuilder();
        sb.append("*".repeat(phoneNumber.length() - 4));
        sb.append(phoneNumber.substring(phoneNumber.length() - 4));
        return sb;
    }

    public static void main(String[] args) {
        String phoneNumber = "01033334444";
        System.out.println(solution(phoneNumber));
    }
}