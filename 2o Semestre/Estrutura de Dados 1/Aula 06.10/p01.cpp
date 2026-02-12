#include <iostream>
#include <queue>

using namespace std;

struct pessoa{
    string nome;
    string email;
};

int main(){
    queue<pessoa> fila;
    pessoa aux;
    /* a variavel aux servira para coletar as informacoes
    lidas e posteriormente inserir na fila.
    IMPORTANTE: todo novo valor ira sobrescrever a variavel AUX
    */

    while(true){
        cout << "Digite o nome ou FIM para sair\n";
        getline(cin, aux.nome); //le o nome do teclado
        if(aux.nome == "FIM"){
            break;
        }
        
        cout << "Email:";
        getline(cin, aux.email); //le o email do teclado
        fila.push(aux);
        cout << "T: " << fila.size() << endl;
    }

    while(!fila.empty()){
        cout << fila.front().nome << "" << fila.front().email << endl;
        fila.pop();
    }

    
    

    return 0;
}