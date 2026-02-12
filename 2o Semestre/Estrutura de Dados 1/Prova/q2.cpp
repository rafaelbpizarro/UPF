//q2.cpp) (Peso 5,0): Escrever um programa em C++ que inicialmente irá ler um inteiro (N) com a quantidade
//de equipes participantes de um torneio de vôlei. Após, o seu programa deverá ler algumas informações sobre
//a classificação deste torneio. Cada linha da entrada contém uma string E e 3 inteiros P, SG e SP, que são
//respectivamente o nome da equipe (E), a quantidade de pontos (P), a quantidade de sets ganhos (SG) e a
//quantidade de sets perdidos (SP). Todos os valores serão separados por um espaço.
//Os dados lidos devem ser ordenados de acordo com os seguintes critérios:
//1. Primeiro critério: Quantidade de pontos (P) em ordem decrescente.
//2. Segundo critério: Maior saldo de sets (SG - SP) em ordem decrescente.
//3. Terceiro critério: Número de sets ganhos (SG) em ordem decrescente.
//4. Quarto critério: Ordem alfabética do nome das equipes (E).
//O programa deve exibir o ranking final dos clubes, um por linha, no formato:
//nome da equipe, pontos, saldo de sets e o número de sets vencidos

#include <iostream>
#include <algorithm>

using namespace std;

struct equipe{
    string E;
    int P;
    int SG;
    int SP;
};

    bool ordenar(const equipe &a, const equipe &b){
        return a.P > b.P ||
        a.P == b.P && (a.SG - a.SP) > (b.SG - b.SP) ||
        a.P == b.P && (a.SG - a.SP) == (b.SG - b.SP) && a.SG > b.SG ||
        a.P == b.P && (a.SG - a.SP) == (b.SG - b.SP) && a.SG == b.SG && a.E < b.E;
    }

int main(){ 
    
    int N;
    cin >> N;
    equipe equipes[N];

    for(int i=0; i < N; i++ ){
        cin >> equipes[i].E >> equipes[i].P >> equipes[i].SG >> equipes[i].SP;
    }

    sort(equipes,equipes + N,ordenar);

    cout << "\n";

    for (int i=0; i < N; i++){
        cout << equipes[i].E << " "
        << equipes[i].P << " "
        << (equipes[i].SG - equipes[i].SP) << " "
        << equipes[i].SG<< endl;
    }

    return 0;
}