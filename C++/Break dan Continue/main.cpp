#include <iostream>

using namespace std;

int main()
{
    int a;
    a = 0;
    while(a < 10){
        a++;
        cout << "Hore ";
        cout << a << endl;
        if(a == 18){
            break; // nilai ditemukan langsung stop
            // or
            //continue; (Nilai ditemukan langsung dilewati/skip)
        }
    }
}
