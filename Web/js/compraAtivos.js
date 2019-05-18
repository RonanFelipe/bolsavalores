function ativarCompra(id){
    let spanButton = document.getElementById(id);
    fetch('http://127.0.0.1:8000/api/v1/ativos/' + id + '/', {
        method: 'PATCH',
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            user: 2,
            status: 1
        })
    }).then(res => res.json())
        .then(res => console.log(res));
}