function loadAtivos() {
    fetch('http://127.0.0.1:8000/api/v1/ativos/')
        .then((resp) => resp.json())
        .then(function (data) {
            let ativos = data;
            for (let i = 0; i < ativos.length; i++) {
                let coluna = document.getElementById("loadAtivos");
                let h5 = document.createElement("h5");
                h5.innerHTML = ativos[i].nome;
                coluna.appendChild(h5);
            }
        })
        .catch(function (error) {
            console.log(error)
        })

}