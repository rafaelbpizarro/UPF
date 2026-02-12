#include <iostream>
#include <queue>
#include <string>

using namespace std;

int main() {
    queue<string> filaPrioritaria;
    queue<string> filaNormal;
    int opcao;
    string nome, tipo;

    do {
        cout << "\n=== Central de Atendimento ===" << endl;
        cout << "1 - Adicionar cliente à fila" << endl;
        cout << "2 - Atender próximo cliente" << endl;
        cout << "0 - Sair" << endl;
        cout << "Escolha uma opcao: ";
        cin >> opcao;
        cin.ignore();

        switch (opcao) {
            case 1:
                cout << "Nome do cliente: ";
                getline(cin, nome);
                cout << "Tipo de atendimento (Prioritario/Normal): ";
                getline(cin, tipo);

                if (tipo == "Prioritario" || tipo == "prioritario" || tipo == "P" || tipo == "p") {
                    filaPrioritaria.push(nome);
                    cout << "Cliente " << nome << " adicionado à fila PRIORITÁRIA." << endl;
                } else {
                    filaNormal.push(nome);
                    cout << "Cliente " << nome << " adicionado à fila NORMAL." << endl;
                }
                break;

            case 2:
                if (!filaPrioritaria.empty()) {
                    cout << "Atendendo cliente PRIORITÁRIO: " << filaPrioritaria.front() << endl;
                    filaPrioritaria.pop();
                } else if (!filaNormal.empty()) {
                    cout << "Atendendo cliente NORMAL: " << filaNormal.front() << endl;
                    filaNormal.pop();
                } else {
                    cout << "Nenhum cliente aguardando atendimento." << endl;
                }
                break;

            case 0:
                cout << "Encerrando o sistema..." << endl;
                break;

            default:
                cout << "Opcao invalida. Tente novamente." << endl;
        }

    } while (opcao != 0);

    return 0;
}
