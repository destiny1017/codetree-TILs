import java.lang.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = Integer.parseInt(scan.nextLine());
        int[] people = new int[n];
        String[] peopleStr = scan.nextLine().split(" ");
        for(int i = 0; i < n; i++) {
            people[i] = Integer.parseInt(peopleStr[i]);
        }
        int[] leaderMember = Arrays.stream((scan.nextLine().split(" ")))
                                .mapToInt(Integer::parseInt)
                                .toArray();

        int val = 0;
        for(int p : people) {
            p -= leaderMember[0];
            val += 1;
            if(p > 0) {
                int ceil = (int) Math.ceil((double)p / leaderMember[1]);
                val += ceil;
            }
            
        }
        System.out.println(val);
    }
}