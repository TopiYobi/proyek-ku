#include <iostream>

using namespace std;

int main()
{
    float a,b,c,d,e;
    cout << "Masukan Jumlah Data = ";
    cin >> a;
    int h1;
    h1 = a * 1/2;
    cout << h1 << endl;
    cout << "Masukan nilai Kelas terbawah dari "<< h1 << " = ";
    cin >> b;
    cout << "Masukan nilai FK = ";
    cin >> c;
    cout << "Masukan nilai Frekuensi = ";
    cin >> d;
    cout << "Masukan Panjang Kelas = ";
    cin >> e;

    float h2,h3,h4,h5;
    h2 = h1 - c;
    h3 = h2 / d;
    h4 = h3 * e;
    h5 = b + h4;

    cout << "Nilai Median Anda Yaitu = " << h5 << endl;

    cin.get();
    return 0;


}
