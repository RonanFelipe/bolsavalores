function showUsers() {
    fetch('http://127.0.0.1:8000/api/v1/user/')
        .then((res) => res.json())
        .then(function (data) {
            let users = data;
            for (let i = 0; i < users.length; i++) {
                let coluna = document.getElementById("allUsers");
                let divUsers = document.createElement("div");
                let h5 = document.createElement("h5");
                h5.classList.add('subtitle');
                h5.classList.add('is-5');
                h5.innerHTML = users[i].id + " - " + users[i].name + " from " + users[i].nacionalidade;
                divUsers.appendChild(h5);
                coluna.appendChild(divUsers);
            }
        })
}