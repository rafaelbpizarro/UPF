#include <iostream>
#include <algorithm>

using namespace std;

struct Pais{
    string nome;
    int ouro;
    int prata;
    int bronze;
};

    bool comparar(const Pais &a, const Pais &b){
        return a.ouro > b.ouro ||
        a.ouro == b.ouro && a.prata > b.prata ||
        a.ouro == b.ouro && a.prata == b.prata && a.bronze > b.bronze ||
        a.ouro == b.ouro && a.prata == b.prata && a.bronze == b.bronze && a.nome < b.nome;
    }

int main(){ 
    
    int N;
    cin >> N;
    Pais paises[N];

    for(int i=0; i < N; i++ ){
        cin >> paises[i].nome >> paises[i].ouro >> paises[i].prata >> paises[i].bronze;
    }

    sort(paises,paises + N,comparar);

    for (int i=0; i < N; i++){
        cout << paises[i].nome << " "
        << paises[i].ouro << " "
        << paises[i].prata << " "
        << paises[i].bronze<< endl;
    }

    return 0;
}