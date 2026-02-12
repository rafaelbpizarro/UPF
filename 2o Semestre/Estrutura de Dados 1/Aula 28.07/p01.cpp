//EXEMPLO DE ENTRADA DE DADOS EM C++

#include <iostream>

using namespace std;

int main(){
    
    int idade;
    float altura;

    cout << "Digite a sua idade: "; //PRINT
    cin >> idade; //INPUT

    cout << "Digite a sua altura (em metros): "; //PRINT
    cin >> altura; //INPUT

    cout << "Você tem " << idade << " anos e " << altura << "m de altura" << endl;

    return 0;
}