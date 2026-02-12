//Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre
//a diferença do produto de A e B pelo produto de C e D segundo a fórmula:
//DIFERENCA = (A * B - C * D).

#include <iostream>

using namespace std;

int main() {
    int A, B, C, D;
    int diferenca;

    cin >> A;
    cin >> B;
    cin >> C;
    cin >> D;

    diferenca = (A * B - C * D);

    cout << "DIFERENCA = " << diferenca << endl;

    return 0;
}