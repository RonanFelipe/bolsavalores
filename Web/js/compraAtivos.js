function ativarCompra(id){
    let spanButton = document.getElementById(id);
    let nomeUser = document.getElementById("nomeUser").value;
    let userId = 0;
    fetch('http://127.0.0.1:8000/api/v1/user/')
        .then((resp) => resp.json())
        .then(function (data) {
            let users = data;
            for (let i =0; i < users.length; i++){
                if (users[i].name === nomeUser){
                    userId = users[i].id;
                }
            }
            comprar(id, userId)
        });
}

function comprar(id, userId) {
    fetch('http://127.0.0.1:8000/api/v1/ativos/' + id + '/', {
        method: 'PATCH',
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            user: userId,
            status: 1
        })
    }).then(res => res.json())
        .then(res => console.log(res));
}