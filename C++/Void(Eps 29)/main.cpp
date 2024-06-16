#include <iostream>
using namespace std;

int tambah(int a, int b)
{
    int hasil;
    hasil = a + b;
    return hasil;
}

void tampilan(int tampil)
{
    cout << "tampilan menggunakan Void\n" << endl;
    cout << "Hasilnya = " << tampil << endl;
}

int main()
{
    int i1,i2,hasil;
    cout << "Masukan Nilai Pertama = ";
    cin >> i1;
    cout << "Masukan Nilai Kedua = ";
    cin >> i2;

    hasil = tambah(i1,i2);

    tampilan(hasil);

    cin.get();
    return 0;
}
