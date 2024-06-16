#include <iostream>

using namespace std;

int main()
{
    cout << "====Kalkulator Cabang====" << endl;
    int a,b;
    cout << "Masukan No Pertama = ";
    cin >> a;
    cout << "Masukan No Kedua = ";
    cin >> b;

    char hasil;
    cout << "====Pilih Oprasi====" << endl;
    cout << "a. +\n";
    cout << "b. -\n";
    cout << "c. *\n";
    cout << "d. /\n";
    cout << "e. %\n" << endl;

    cout << "Masukan pilihan = ";
    cin >> hasil;

    if(hasil == 'a'){
        int h2 = a + b;
        cout << "Hasil dari " << a << " + " << b << " = " << h2 << endl;
    }
    if(hasil == 'b'){
        int h2 = a - b;
        cout << "Hasil dari " << a << " - " << b << " = " << h2 << endl;
    }
    if(hasil == 'c'){
        int h2 = a * b;
        cout << "Hasil dari " << a << " X " << b << " = " << h2 << endl;
    }
    if(hasil == 'd'){
        int h2 = a / b;
        cout << "Hasil dari " << a << " / " << b << " = " << h2 << endl;
    }
        if(hasil == 'e'){
        int h2 = a % b;
        cout << "Hasil dari " << a << " % " << b << " = " << h2 << endl;
    }

    cin.get();
    return 0;
}
