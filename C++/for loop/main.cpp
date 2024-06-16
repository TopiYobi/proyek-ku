#include <iostream>

using namespace std;

// for(inisialisasi; loop kondisi; increment){
//  statment }
int main()
{
    cout << "========loop 1" << endl;// dengan oprasi increment
    for(int c = 1; c <= 10;c++){
        cout << "hore";
        cout << c << endl;
    }
    cout << "========loop 2" << endl;// dengan semua oprasi assignmet
    for(int d = 1; d <= 10; d+= 2){
        cout << "hore";
        cout << d << endl;
    }
    cout << "========loop 3" << endl;// dengan oprasi descriment
    for(int a = 1; a >= -10; a--){
        cout << "hore";
        cout << a << endl;
    }
    cout << "========loop 4" << endl;
    int total = 0;
    for(int e= 1; e <= 10;e++){
        total += e;
        cout << e << "//||" << total << endl;
    }
    cout << "========loop 5" << endl;
    int total1 = 0;
    for(int r= 1; r <= 10; total1 += r, r++){
        cout << r << "//||" << total1 << endl;
    }
    cin.get();
    return 0;
}
