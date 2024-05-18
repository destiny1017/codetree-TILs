import java.lang.*;
import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner scan = new Scanner(System.in);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        int[] people = new int[n];
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < n; i++) {
            people[i] = Integer.parseInt(st.nextToken());
        }
        int[] leaderMember = new int[2];
        st = new StringTokenizer(br.readLine());
        leaderMember[0] = Integer.parseInt(st.nextToken());
        leaderMember[1] = Integer.parseInt(st.nextToken());

        long val = 0;
        for(int p : people) {
            p -= leaderMember[0];
            val += 1;
            if(p > 0) {
                val += (int) Math.ceil((double)p / leaderMember[1]);
            }
            
        }
        System.out.println(val);
    }
}