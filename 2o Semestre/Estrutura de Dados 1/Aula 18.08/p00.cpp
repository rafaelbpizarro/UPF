#include <iostream>

using namespace std;

void imprimir(string texto){
    cout << texto << endl;
};

int adiciona(int x, int y){
    int t = x + y;
    return t;
}

int main(){

    int t = 500;
    int x = 10, y = 2;
    int soma = adiciona(y,x);
    cout << "Soma: " << soma << endl;

    imprimir("Exemplo de função 'void' \n");

    cout << "Valor da variável T: " << t << endl;
    
    return 0;
}