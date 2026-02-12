#include <iostream>

int calcularFatorialRecursivo(int n){
    if (n == 0 || n == 1){
        return 1;
    }
    return n * calcularFatorialRecursivo(n - 1); 
}

int main(){
    int numero;
    std::cout << "digite um número inteiro: ";
    std::cin >> numero;

    if (numero < 0){
        std::cout << "O fatorial de um número negativo não existe";
    } else{
        int fatorial = calcularFatorialRecursivo(numero);
        std::cout << "O fatorial de " << numero << "é: " << fatorial << std::endl;
    }
    return 0;
}