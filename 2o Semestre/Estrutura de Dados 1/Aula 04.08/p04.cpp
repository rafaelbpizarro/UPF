//Exemplos de laços de repetição

#include <iostream>

using namespace std;

int main(){

    int n = 0;
    cout << "Laço 'While' \n";

    while (n < 10){
        cout << n << endl;
        n++; //Atualiza o contador
        //n = n+1;
    }

    //O teste vem ao final do laço;
    // Garante que pelo menos uma vez será executado
    cout << "Laço 'do while' \n";
    do{
        cout << n << endl;
        n--;

    } while(n> 0); 

    //While true (infinito até que se tenha um break)
    
    while (true){
        cout << n << endl;
        if (n == 5){
            break;
        }
        n++;
        
    }


        cout << "Laço de repetição 'for' \n";
        //Laço for:
        // Tem 3 partes.
        // 1º (Inicialização da variável de controle)
        // 2º Teste while: vai permanecer neste laço enquanto a condição for verdadeira
        // 3º Atualização da variável de controle

        for (int i= 0; i <=20; i++){
            cout << i << endl;

        }
        
    

    return 0;
}