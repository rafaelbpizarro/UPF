//Exemplo de função externa

#include <iostream>
#include "funcoes.cpp"

using namespace std;

int main(){

    int n;
    cout << "N:";
    cin >> n;
    cout << "Fatorial " << fatorial(n) << endl;

    return 0;
}