#include <iostream>

using namespace std;
//increment(Tambah) dan descrement(Kurang)
int main()
{
    int a,b;
    //postincrement(melalukan oprasi sesudah)
    a = 10;
    cout << a << endl;
    cout << a++ << endl;
    cout << a << endl;
    // preincrement (melakukan oprasi sebelum)
    b = 10;
    cout << b << endl;
    cout << ++b << endl;
    cout << b << endl;
    cout << "akhir dari Increment......\n" << endl;

    int c,n;
    //postdescrement (melalukan oprasi sesudah)
    c = 15;
    cout << c << endl;
    cout << c++ << endl;
    cout << c << endl;
    //predescrement (melalukan oprasi sebelum)
    n = 15;
    cout << n << endl;
    cout << ++n << endl;
    cout << n << endl;
    cout << "akhir dari Descrement......\n" << endl;

    cin.get();
    return 0;
}
