#include <iostream>

using namespace std;

int main()
{
    int a;
    cout << "Masukan Kode = ";
    cin >> a;

    if (a == 1234){
        cout << "kode benar"<<endl;
    }
    else{
        cout << "kode salah"<<endl;
    }
    if (a == 123){
        cout<< "dikit lagi benar"<<endl;
    }
    cin.get();
    return 0;

}
