//FIFO - First In First Out

#include <iostream>
#include <queue>

using namespace std;

int main(){

    queue<int> fila;

    fila.push(100); //Adiciona valores na fila
    fila.push(200);
    fila.push(300);

    cout << "Tamanho da fila: " << fila.size() << endl;

    while(!fila.empty()){ // fila.size() > 0
        cout << "Size: " << fila.size() << endl; //Tamanho
        cout << "Front: " << fila.front() << endl; //Primeiro Elemento
        cout << "Back: " << fila.back() << endl; //Último Elemento
        cout << endl;
        fila.pop(); //Remove o Primeiro Elemento da Fila
    }

    return 0;
}