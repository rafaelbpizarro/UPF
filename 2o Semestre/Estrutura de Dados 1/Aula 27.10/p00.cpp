#include <iostream>
#include <vector>

using namespace std;

int main(){
    vector<int> v; //Vector de int inicialmente vazio
    cout << "Size: " << v.size() << endl;

    for (int i=0; i<v.size(); i++){
        cout << i << ": " << v[i] << endl;
    }

    
}