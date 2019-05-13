function loadAtivos() {
    fetch('http://127.0.0.1:8000/api/v1/ativos/')
        .then((resp) => resp.json())
        .then(function (data) {
            let ativos = data;
            for (let i = 0; i < ativos.length; i++) {
                let coluna = document.getElementById("loadAtivos");
                let tagLarge = document.createElement("span");
                tagLarge.innerHTML = ativos[i].nome;
                tagLarge.classList.add('tag');
                tagLarge.classList.add('is-primary');
                tagLarge.classList.add('is-medium');
                brElement = document.createElement("br");
                coluna.appendChild(tagLarge);
                coluna.appendChild(brElement);
            }
        })
        .catch(function (error) {
            console.log(error)
        })

}