#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int main() {
    string s;
    cin >> s;
    
    char current = 'a';
    int total_rotations = 0;

    for (char c : s) {
        int clockwise = abs(c - current);
        int counterclockwise = 26 - clockwise;
        total_rotations += min(clockwise, counterclockwise);
        current = c;
    }

    cout << total_rotations << endl;
    return 0;
}
