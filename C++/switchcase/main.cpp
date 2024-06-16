#include <iostream>

using namespace std;

int main()
{
    int a;
    cout << "masukan nilai ";
    cin >> a;

    switch(a){
        case 1:
            cout << "nilai 1"<< endl;
            break;// mengakhiri case untuk menampilkan semua
        case 2:
             cout << "nilai 2"<< endl;
        case 3:
             cout << "nilai 3"<< endl;
        case 4:
             cout << "nilai 4"<< endl;
        default: // jika case salah
            cout << "nilai tidak di temukan"<<endl;

    }
}
