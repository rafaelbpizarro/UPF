//Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos.
//Na próxima linha, deve-se mostrar a média de todos os valores positivos digitados,
//com um dígito após o ponto decimal.

#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    double numero, soma = 0.0;
    int positivos = 0;

    for (int i = 0; i < 6; i++) {
        cin >> numero;
        if (numero > 0) {
            soma += numero;
            positivos++;
        }
    }

    double media = soma / positivos;

    cout << positivos << " valores positivos" << endl;
    cout << fixed << setprecision(1) << media << endl;

    return 0;
}