#include <iostream>
#include <algorithm>

using namespace std;

struct crianca{
    string comportado;
    string nome;
};

    bool comparar(const crianca &a, const crianca &b){
        return a.nome < b.nome;
    }

int main(){ 
    
    int comportados = 0;
    int naocomportados = 0;
    int N;
    cin >> N;
    crianca lista[N];

    for(int i=0; i < N; i++ ){
        cin >> lista[i].comportado >> lista[i].nome;
    }

    sort(lista,lista + N,comparar);

    for (int i=0; i < N; i++){
        if(lista[i].comportado == "+"){
            comportados++;
        }
        else if (lista[i].comportado == "-"){
            naocomportados++;
        }
        cout << lista[i].nome << endl;
        
    }
    cout << "Se comportaram: " << comportados << " | Nao se comportaram: " << naocomportados << endl;

    return 0;
}