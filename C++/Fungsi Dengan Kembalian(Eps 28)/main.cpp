#include <iostream>
using namespace std;

//ini fungsi kembalian yang nanti akan masuk ke main tanpa membuat
//rumus pada main
int kuadrat(int a)
{
    int b;
    b = a*a;
    return b;
}

int main()
{

    int input,hasil;
    cout << "Nilai kuadrat dari : ";
    cin >> input;

    hasil = kuadrat(input);
    cout << hasil << endl;

    cin.get();
    return 0;
}
