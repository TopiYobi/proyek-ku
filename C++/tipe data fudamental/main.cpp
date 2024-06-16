#include <iostream>
#include <limits> // untuk mengunakan numberic_limits
using namespace std;

int main()
{
    //====bilangan bulat====
    int a = 1;// bilangan bulat 32-bit
    cout << a << endl;
    cout << sizeof(a)<<" byte" << endl;
    cout <<numeric_limits<int>::max() << endl; // header harus menyertakan limits (#include limits)
    short b = 3; // bilangan pendek kurang atau sama dengan 32-bit
    cout << b << endl;
    cout << sizeof(b)<<" byte" << endl;
    cout << numeric_limits<short>::max() << endl;
    long c = 7; // bilangan panjang dari 32-bit
    cout << c << endl;
    cout << sizeof(c)<<" byte" << endl;
    cout << numeric_limits<long>::max() << endl;

     //====desimal====
    float k = 2.0;
    cout << k << endl;
    cout << sizeof(k)<<" byte" << endl;
    double l = 1.5;
    cout << l << endl;
    cout << sizeof(l)<<" byte" << endl;

    //====charakter====
    char f = 'a';
    cout << f << endl;
    cout << sizeof(f)<<" byte" << endl;

    //====boolean====
    bool x = true;// hanya dua hasil yaitu true atau false
    cin.get();
    return 0;



}
