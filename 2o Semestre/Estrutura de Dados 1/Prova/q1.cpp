//q1.cpp) (Peso 5,0) Escreva um programa em C++ que monitore o índice pluviométrico (em milímetros) de
//uma cidade durante M meses. O programa deve ler o valor de M e, em seguida, os índices de chuva de cada
//mês, guardando-os em um vetor de float de tamanho M. O programa deverá exibir:
//● A quantidade de meses com seca (chuva abaixo de 50 mm).
//● A quantidade de meses com chuva moderada (entre 50 mm e 150 mm).
//● A quantidade de meses com chuva intensa (acima de 150 mm).
//● O menor e o maior índice de chuva registrados.
//● A média de chuva mensal para o período (com uma casa decimal).
//OBS: Além da função main, o programa deve ter, no mínimo duas outras funções que recebam parâmetro e
//retornem valor (a sua escolha).

#include <iostream>
#include <algorithm>
#include <iomanip>

using namespace std;

struct indice{
    float milimetros;
};

bool comparar(const indice &a, const indice &b){
    return a.milimetros > b.milimetros;
};

int main(){ 
    
    int seca;
    int moderada;
    int intensa;

    float maior;
    float menor;
    float media;

    int N;
    cin >> N;
    indice mes[N];

    for(int i=0; i < N; i++ ){
        cin >> mes[i].milimetros;
        if (mes[i].milimetros < 50){
            seca++;
        }
        else if (mes[i].milimetros >= 50 and mes[i].milimetros <= 150){
            moderada++;
        }
        else if(mes[i].milimetros > 150){
            intensa++;
        }
        media += mes[i].milimetros;
    }

    for(int i=0; i < N; i++ ){
        if (mes[i].milimetros > maior){
            maior = mes[i].milimetros;
        }
    }
    
    menor = maior;

    for(int i=0; i < N; i++ ){
        if (mes[i].milimetros < menor){
            menor = mes[i].milimetros;
        }
    }

    sort(mes,mes + N,comparar);

    media = media / N;

    cout << "Meses com seca: " << seca << endl;
    cout << "Meses com chuva moderada: " << moderada << endl;
    cout << "Meses com chuva intensa: " << intensa << endl;
    cout << "Menor índice de chuva registrado: " << menor << endl;
    cout << "Maior índice de chuva registrado: " << maior << endl;
    cout << "Média de chuva mensal: " << fixed << setprecision(1) << media << endl;
   return 0;
}