import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = Integer.parseInt(scan.nextLine());
        String[][] move = new String[n][2];
        for(int i = 0; i < n; i++) {
            move[i] = scan.nextLine().split(" ");
        }
        
        int maxLen = 10 * 100;
        Map<String, Integer[]> indicator = new HashMap<>();
        indicator.put("E", new Integer[]{0, 1});
        indicator.put("W", new Integer[]{0, -1});
        indicator.put("S", new Integer[]{1, 0});
        indicator.put("N", new Integer[]{-1, 0});
        
        int[][] visit = new int[maxLen*2][maxLen*2];
        int x = maxLen, y = maxLen, minVisit = maxLen;
        int step = 0;
        
        for(int i=0; i < n; i++) {
            String direction = move[i][0];
            int distance = Integer.parseInt(move[i][1]);
            for(int j=0; j < distance; j++) {
                step++;
                x += indicator.get(direction)[0];
                y += indicator.get(direction)[1];

                if(visit[x][y] < maxLen && visit[x][y] != 0) {
                    minVisit = Math.min(minVisit, step - visit[x][y]);
                } else {
                    visit[x][y] = step;
                }
            }
        }

        System.out.println(minVisit == maxLen ? -1 : minVisit);
    }
}