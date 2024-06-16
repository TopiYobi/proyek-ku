#include <iostream>

using namespace std;

int main()
{
    char a,b;
    int c;

    cout << "Nama = ";
    cin >> a;
    cout << "Kelas = ";
    cin >> b;
    cout << "Nilai = ";
    cin >> c;

    if(c > 50){
        cout <<"Nama : " << a << endl;
        cout <<"Kelas : "<< b << endl;
        cout << "Keterangan : Tidak lulus" << endl;
    }
    else{
        cout <<"Nama : " << a << endl;
        cout <<"Kelas : "<< b << endl;
        cout << "Keterangan : lulus " << endl;
    }
}
