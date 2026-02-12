#include <iostream>
#include <vector>

using namespace std;

int main(){
    vector<double> v;
    cout << "Digite 0.0 para sair\n";
    double x;
    cout << "Tamanho: " << v.size() << " Capacidade: " << v.capacity() << endl;

    while(cin >> x && x!=0){ //Encerra quando o x for 0
        v.push_back(x);
        cout << "Tamanho: " << v.size() << " Capacidade: " << v.capacity() << endl;
    }

    //Exibir os valores de forma reversa
    for(int i=v.size()-1; i>0;i--){
        cout << v[i] << endl;
    }
}