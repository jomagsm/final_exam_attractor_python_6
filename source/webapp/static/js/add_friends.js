const addFriends = document.getElementsByClassName('btn btn-secondary btn-lg btn-block')
const delFriends = document.getElementsByClassName('btn btn-outline-dark btn-lg btn-block')
const addFriendUrl = 'http://localhost:8000/api/add_friends/'
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


async function makeRequest(url, method = 'GET', data = undefined) {
    let opts = {method, headers: {}};

    if (!csrfSafeMethod(method))
        opts.headers['X-CSRFToken'] = getCookie('csrftoken');

    if (data) {
        opts.headers['Content-Type'] = 'application/json';
        opts.body = JSON.stringify(data);
    }

    let response = await fetch(url, opts);

    if (response.ok) {
        return await response.json();
    } else {
        let error = new Error(response.statusText);
        error.response = response;
        throw error;
    }
}

async function add(event) {
    event.preventDefault();
    let idUser = event.target;
    let data = idUser.id
    try {
        let response = await makeRequest(addFriendUrl, "POST", data);
    } catch (e) {
        alert("Неправильное значение");
    }
}

async function del(event) {
    event.preventDefault();
    let idUser = event.target;
    let url = urlDeleteFriend.replace('123', idUser.id);
    try {
        let response = await makeRequest(url, "DELETE");
        let friend = document.getElementById(response.success)
        friend.parentElement.parentNode.remove()
    } catch (e) {
        alert("Неправильное значение");
    }
}
console.log(addFriends)
for (let addFriend of addFriends) {addFriend.onclick = add}
for (let delFriend of delFriends) {delFriend.onclick = del}