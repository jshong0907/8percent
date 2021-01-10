#include <iostream>
using namespace std;
int fibo(int n) {
    int result = 1;
    int result2 = 0;
    if(n >= 0 && n <= 2) {
        return 1;
    }
    for(int i=3;i<=n;i++) {
        result = result + result2;
        result2 = result;
    }
    return result;
    }
    int main() {
        for(int i=1;i<=5;i++) {
        cout << i << ": " << fibo(i) << endl;
    }
    return 0;
}