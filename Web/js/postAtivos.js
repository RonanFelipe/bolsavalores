document.getElementById("submitAtivo").addEventListener("click", createAtivos);

function createAtivos() {
    let nome = document.getElementById("nomeAtivo").value;
    let codigo = document.getElementById("codigoAtivo").value;
    let descricao = document.getElementById("descricaoAtivo").value;
    let quantidade = document.getElementById("qtdAtivo").value;
    let preco = document.getElementById("precoAtivo").value;
    fetch('http://127.0.0.1:8000/api/v1/ativos/', {
        method: 'post',
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            nome: nome,
            codigo: codigo,
            descricao: descricao,
            quantidade: quantidade,
            preco: preco,
        })
    }).then(res => res.json())
        .then(res => console.log(res));
}