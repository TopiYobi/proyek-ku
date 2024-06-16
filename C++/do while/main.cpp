#include <iostream>

using namespace std;
// do while akan selalu mengeksekusi kode meskipun syarat while (false)
int main()
{
    int a = 1;
    do{
        cout << "hore";
        cout << a << endl;
        ++a;
    }while( a <= 10 );
    cin.get();
    return 0;
}
