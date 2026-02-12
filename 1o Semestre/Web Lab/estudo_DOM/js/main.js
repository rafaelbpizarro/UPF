let corpo = document.body;
let formulario = document.getElementById("form");

formulario.addEventListener('submit',function(event){
    event.preventDefault();
    salvar(); /// chama a função de salvar os dados
});

function salvar(){
    ///obter os valores do form;
    let nome = document.getElementById("nome");
    let curso = document.getElementById("curso");
    let universidade = document.getElementById("universidade");
    //obtem o tbody da tabela
    let tabela = document.getElementById("customers").getElementsByTagName("tbody")[0];
    //Validar o nome
    let NomeValido = validaNome(nome.value);
    if(NomeValido){
        //Cria uma nova linha na tabela
        let linha = tabela.insertRow() 
        //1º celular recebe o nome
        linha.insertCell(0).textContent = nome.value; 
        linha.insertCell(1).textContent = curso.value;
        linha.insertCell(2).textContent = universidade.value;
        mensagem.textContent = "";
    }
}

//Função para limpar os campos do formulário
function limpar(){
    let nome = document.getElementById("nome");
    nome.value = "";
    let curso = document.getElementById("curso");
    curso.value = "";
    let universidade = document.getElementById("universidade");
    universidade.value = "";
}

function limparTabela(){
    let tabela = document.getElementById("customers").getElementsByTagName("tbody")[0];
    tabela.innerHTML="";
}

function addDarkTheme(){
    corpo.className = "";
    corpo.classList.add("dark");
}

function removeDarkTheme(){
    corpo.className = "";
    corpo.classList.add("white")
}

function validaNome(nome){
    if(nome.length < 3){
        mensagem.textContent = "Atenção! O nome deve ter pelo menos 3 caracteres";
        mensagem.style.color = "red";
        return false;
    }
    return true;
}