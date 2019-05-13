function loadAtivos() {
    fetch('http://127.0.0.1:8000/api/v1/ativos/')
        .then((resp) => resp.json())
        .then(function (data) {
            let ativos = data;
            for (let i = 0; i < ativos.length; i++) {
                let coluna = document.getElementById("loadAtivos");
                let divAtivos = document.createElement("div");
                divAtivos.classList.add('tags');
                divAtivos.classList.add('has-addons');
                let firstSpan = document.createElement("span");
                let secondSpan = document.createElement("span");
                let thirdSpan = document.createElement("span");
                firstSpan.classList.add('tag');
                secondSpan.classList.add('tag');
                secondSpan.classList.add('is-info');
                thirdSpan.classList.add('tag');
                thirdSpan.classList.add('is-warning');
                firstSpan.innerHTML = ativos[i].codigo;
                secondSpan.innerHTML = "R$ " + ativos[i].preco;
                thirdSpan.innerHTML = "Qtd " + ativos[i].quantidade;
                divAtivos.appendChild(firstSpan);
                divAtivos.appendChild(secondSpan);
                divAtivos.appendChild(thirdSpan);
                coluna.appendChild(divAtivos);
            }
        })
        .catch(function (error) {
            console.log(error)
        })
}
