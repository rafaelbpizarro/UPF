//EXEMPLO DE MANIPULAÇÃO DE STRING

#include <iostream>
#include <cstring>

using namespace std;

int main(){
    string nome;
    cout << "Digite o seu nome completo: ";
    //cin >> nome; ENTRADA ATÉ O ESPAÇO EM BRANCO
    getline(cin, nome); //OBTÉM TODA A LINHA ESCRITA NO TERMINAL
    
    //PARA OBTER A LINHA EM UM ARQUIVO POR EXEMPLO SE TROCA O cin EM GETLINE PELO ARQUIVO

    //cout << "Seu primeiro nome é " << nome << endl;
    cout << "Seu nome completo é " << nome << endl;

    return 0;
}