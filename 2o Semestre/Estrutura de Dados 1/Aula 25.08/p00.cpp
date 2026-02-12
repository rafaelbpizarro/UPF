#include <iostream>

using namespace std;

/*Template de função para trocar dois valores de qualquer tipo T*/
template <typename T>
void swapT(T &a, T &b){
    T aux = a;
    a = b;
    b = aux;

}

int main(){

    int x = 10, y = 20;
    cout << "Antes x: " << x << ", y: " << y << endl;

    swapT(x,y);
    cout << "Depois x: " << x << ", y: " << y << endl;

    //ESPAÇO:
    cout << endl;

    // TESTAMOS A FUNÇÃO USANDO FLOAT:

    float a = 0.6, b = 1.4;
    cout << "Antes a: " << a << ", b: " << b << endl;

    swapT(a,b);
    cout << "Depois a: " << a << ", b: " << b << endl;

    //ESPAÇO:
    cout << endl;

    //STRING:

    string s1 = "Hello", s2 = "world";
    cout << "Antes s1: " << s1 << ", s2: " << s2 << endl;

    swapT(s1,s2);
    cout << "Depois s1: " << s1 << ", s2: " << s2 << endl;

    return 0;
}