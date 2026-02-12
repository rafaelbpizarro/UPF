//Com base na tabela abaixo, escreva um programa que leia o código de um item e a
//quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

// CÓDIGO               ESPECIFICAÇÃO               PREÇO
//   1                 Cachorro-quente              R$4.00
//   2                    X-salada                  R$4.50
//   3                     X-bacon                  R$5.00
//   4                 Torrada simples              R$2.00
//   5                  Refrigerante                R$1.50


#include <iostream>
#include <iomanip>

using namespace std;

int main() {

    int codigo;
    int qtd;
    double total;

    cin >> codigo >> qtd;

    switch(codigo){
        case 1:
            total = 4 * qtd;
            cout << "Total: R$" << fixed << setprecision(2) << total << endl;
            break;
        case 2:
            total = 4.5 * qtd;
            cout << "Total: R$" << fixed << setprecision(2) << total << endl;
            break;
        case 3:
            total = 5 * qtd;
            cout << "Total: R$" << fixed << setprecision(2) << total << endl;
            break;
        case 4:
            total = 2 * qtd;
            cout << "Total: R$" << fixed << setprecision(2) << total << endl;
            break;
        case 5:
            total = 1.5 * qtd;
            cout << "Total: R$" << fixed << setprecision(2) << total << endl;
            break;
        default:
            cout << "Código inválido. Por favor, insira um valor entre 1 e 5." << endl;
    }

    return 0;
}