//Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir.
//Cada caso de teste consiste de dois inteiros X e Y. Você deve apresentar a soma
//de todos os ímpares existentes entre X e Y.

#include <iostream>

using namespace std;

int main() {
    int N;
    cin >> N;

    for (int i = 0; i < N; i++) {
        int X, Y;
        cin >> X >> Y;
        
        if (X>Y){
            int temp = X;
            X = Y;
            Y = temp;
        }

        int soma = 0;
        for (int num = X + 1; num < Y; num++){
            if (num % 2 != 0){
                soma += num;
            } 
        }

        cout << soma << endl;
    }
   
    return 0;
}