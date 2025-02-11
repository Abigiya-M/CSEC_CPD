import java.util.Scanner;

public class PoliceRecruits {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int n = scanner.nextInt(); // Number of events
        int officers = 0; // Available officers
        int untreatedCrimes = 0; // Crimes that go untreated
        
        for (int i = 0; i < n; i++) {
            int event = scanner.nextInt();
            
            if (event == -1) { // A crime occurs
                if (officers > 0) {
                    officers--; // An officer handles the crime
                } else {
                    untreatedCrimes++; // No officer available
                }
            } else { 
                officers += event; // Hiring officers
            }
        }
        
        System.out.println(untreatedCrimes);
        
        scanner.close();
    }
}
