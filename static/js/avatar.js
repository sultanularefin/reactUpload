// myproject/site_static/site/js/avatar.js
// let userToken="d2040cb830f5590e444e2bcf853cdf5e26d2e9d1";
let userToken;

document.getElementById('login_form').addEventListener('submit', function(event) {
    event.preventDefault();
    // let email = document.getElementById('id_email').value;
    let username = document.getElementById('id_username').value;


    let password = document.getElementById('id_password').value;
    //https://arefinreact.pythonanywhere.com/users/
    // http://127.0.0.1:8000/api/auth-token/




    // https://arefinreact.pythonanywhere.com/users/
    // https://arefinreact.pythonanywhere.com/api/auth-token/
    // http://127.0.0.1:8000/api/auth-token/
    fetch(
        // 'http://127.0.0.1:8000/api/auth-token/',
        'https://arefinreact.pythonanywhere.com/api/auth-token/',
        {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            "username": username,
            "password": password,
        })
    }).then( response => {
        return response.json();
    }).then(data => {
        console.log(data);
        userToken = data.token;
        console.log('Logged in. Got the token.');
    }).catch((error) => {
        console.error('Error:', error);
    });
});

document.getElementById('avatar_form').addEventListener('submit', function(event) {
    event.preventDefault();
    let input = document.getElementById('id_avatar');

    let data = new FormData();
    console.log("data: FormData() => username and password (should contain) ", data);
    data.append('avatar', input.files[0]);

    fetch('http://127.0.0.1:8000/api/user-avatar/', {
        method: 'POST',
        headers: {
            'Authorization': `Token ${userToken}`
        },
        body: data
    }).then(response => {
        return response.json();
    }).then(data => {
        console.log(data);
    }).catch((error) => {
        console.error('Error:', error);
    });
});