#include <iostream>

using namespace std;

int main()
{
    while(true){
        int a;
        cout << "Masukan Nilai = ";
        cin >> a;

        if(a >= 90 ){
                cout << "Nilai A " << endl;
        }
        if(a >= 88 && a <= 89 ){
            cout << "Nilai B " << endl;
        }
        if(a >= 60 && a <= 79){
            cout << "Nilai C " << endl;
        }
        if(a >= 33 && a <= 59){
            cout << " Nilai D " << endl;
        }
        else{
            cout << "Nilai F "<< endl;
        }
    }
}
