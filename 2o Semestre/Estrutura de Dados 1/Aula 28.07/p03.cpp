//OPERADORES ARITMÉTICOS

#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    float a, b;
    cout << "Digite dois valores: ";
    cin >> a >> b;

    cout << "O resultado da soma é : " << fixed << setprecision(2)
    << a + b << endl
    << "O resultado da subtração é : "
    << a - b << endl
    << "O resultado da multiplicação é : "
    << a * b << endl
    << "O resultado da divisão é : "
    << a / b << endl;

    return 1;
}