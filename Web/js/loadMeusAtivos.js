function searchUser() {
    fetch('http://127.0.0.1:8000/api/v1/meusativos/')
        .then((resp) => resp.json())
        .then(function (data) {
            let ativos = data;
            let userAtivos = [];
            let nomeUser = document.getElementById("nomeUser").value;
            let removeChildNodes = document.getElementById("loadMeusAtivos").innerHTML = "";
            for (let i = 0; i < ativos.length; i++){
                if (nomeUser === ativos[i].user.name) {
                    userAtivos.push(ativos[i]);
                }
            }
            for (let i = 0; i < userAtivos.length; i++) {
                let coluna = document.getElementById("loadMeusAtivos");
                let divMeusAtivos = document.createElement("div");
                divMeusAtivos.classList.add('tags');
                divMeusAtivos.classList.add('has-addons');
                let firstSpan = document.createElement("span");
                let secondSpan = document.createElement("span");
                let sellSpan = document.createElement("a");
                sellSpan.classList.add('tag');
                sellSpan.classList.add('is-danger');
                firstSpan.classList.add('tag');
                firstSpan.classList.add('is-dark');
                secondSpan.classList.add('tag');
                secondSpan.classList.add('is-success');
                firstSpan.innerHTML = userAtivos[i].codigo;
                secondSpan.innerHTML = "R$ " + userAtivos[i].preco;
                sellSpan.innerHTML = "Vender";
                sellSpan.id = userAtivos[i].id;
                sellSpan.setAttribute('onclick', 'ativarVenda(this.id)');
                divMeusAtivos.appendChild(firstSpan);
                divMeusAtivos.appendChild(secondSpan);
                divMeusAtivos.appendChild(sellSpan);
                coluna.appendChild(divMeusAtivos);
            }
        })
}