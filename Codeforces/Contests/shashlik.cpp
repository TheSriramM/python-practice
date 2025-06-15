#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    vector<int> output;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int temp, req1, req2, dec1, dec2;
        int tot = 0;
        cin >> temp >> req1 >> req2 >> dec1 >> dec2;
        if (dec1 < dec2) {
            while (temp >= req1){
                temp -= dec1;
                tot += 1;
            }
        }
            if (req1 > req2){
                while (temp >= req2){
                    temp -= dec2;
                    tot += 1;
                }
            }
        else if (dec2 < dec1){
            if (dec2 < dec1){
                while (temp >= req2){
                    temp -= dec2;
                    tot += 1;
                }
                if (req2 > req1){
                    while (temp >= req1) {
                        temp -= dec1;
                        tot += 1;
                    }
                }
            }
        }
        else{
            if (req1 > req2){
                while (temp >= req2){
                    temp -= dec2;
                    tot += 1;
                }
            }
            else if (req2 > req1){
                while (temp >= req1){
                    temp -= dec1;
                    tot += 1;
                }
            }
            else{
                while (temp >= req1){
                    temp -= dec1;
                    tot += 1;
                }
            }
        }
    output.push_back(tot);
    }
    for (int i = 0; i < n; i++) {
        cout << output[i] << '\n';
    }
}