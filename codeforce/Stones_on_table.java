import java.util.Scanner;

public class StonesOnTheTable {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int n = scanner.nextInt();  // Number of stones
        String stones = scanner.next();  // Colors of the stones
        
        int removals = 0;
        
        for (int i = 1; i < n; i++) {
            if (stones.charAt(i) == stones.charAt(i - 1)) {
                removals++;
            }
        }
        
        System.out.println(removals);
        
        scanner.close();
    }
}
