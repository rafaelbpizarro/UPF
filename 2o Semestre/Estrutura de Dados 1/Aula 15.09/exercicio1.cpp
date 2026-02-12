#include <iostream>
#include <algorithm>

using namespace std;

struct veiculo{
    string modelo;
    float valor;
    int ano;
};

    bool comparar(const veiculo &v1, const veiculo &v2){
        return v1.valor > v2.valor ||                                      //primeiro critério
        v1.valor == v2.valor && v1.ano > v2.ano ||                         //segundo critério
        v1.valor == v2.valor && v1.ano == v2.ano && v1.modelo < v2.modelo; //terceiro critério
    }

int main(){
    
    int N;
    cin >> N;
    veiculo veiculos[N];

    for(int i=0; i < N; i++ ){
        cin >> veiculos[i].modelo >> veiculos[i].valor >> veiculos[i].ano;
    }

    sort(veiculos,veiculos + N,comparar);

    cout << "\n";

    for (int i=0; i < N; i++){
        cout << veiculos[i].modelo << " "
        << veiculos[i].valor << " "
        << veiculos[i].ano << "\n" << endl;
    }

    return 0;
}