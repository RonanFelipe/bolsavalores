function ativarVenda(id){
    fetch('http://127.0.0.1:8000/api/v1/meusativos/' + id + '/', {
        method: 'PATCH',
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            status: 0
        })
    }).then(res => res.json())
        .then(res => console.log(res));
}