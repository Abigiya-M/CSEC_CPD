#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    
    string prev, current;
    int groups = 1; // At least one group exists
    
    cin >> prev; // Read the first magnet
    
    for (int i = 1; i < n; i++) {
        cin >> current;
        if (current != prev) {
            groups++; // New group is formed
        }
        prev = current; // Update previous magnet
    }
    
    cout << groups << endl;
    return 0;
}