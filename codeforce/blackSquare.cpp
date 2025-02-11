#include <iostream>
#include <string>

using namespace std;

int main() {
    int a[4]; // Stores calories for each strip (1 to 4)
    
    // Read the calorie values for the four strips
    for (int i = 0; i < 4; i++) {
        cin >> a[i];
    }
    
    string s;
    cin >> s; // Read the sequence of squares appearing

    int totalCalories = 0;

    // Loop through the string and add up the calories
    for (char c : s) {
        totalCalories += a[c - '1']; // Convert '1', '2', '3', '4' to index 0, 1, 2, 3
    }

    cout << totalCalories << endl;
    
    return 0;
}
