#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;  
    cin >> n;  // Number of wires

    vector<int> birds(n + 1);  // Using 1-based indexing
    for (int i = 1; i <= n; i++) {
        cin >> birds[i];  // Read birds on each wire
    }

    int m;
    cin >> m;  // Number of shots

    while (m--) {
        int x, y;
        cin >> x >> y;  // Wire x, bird at position y is shot

        if (x > 1) {
            birds[x - 1] += y - 1;  // Birds move to the left wire
        }
        if (x < n) {
            birds[x + 1] += birds[x] - y;  // Birds move to the right wire
        }
        birds[x] = 0;  // All birds on this wire are gone
    }

    for (int i = 1; i <= n; i++) {
        cout << birds[i] << endl;  // Print final bird counts
    }

    return 0;
}
