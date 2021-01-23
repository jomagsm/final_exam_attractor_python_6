const addFriends = document.getElementsByClassName('btn btn-outline-success')
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
        // TODO исправить на редирект детального просморта
        // window.location.href = urlRedirect.replace('123', response.success);
    } catch (e) {
        alert("Неправильное значение");
    }

    console.log(idUser.id)}
    // let addBtn = event.target;
    // let url = addBtn.href;
    // console.log(url);
    // try {
    //     let response = await makeRequest(url, 'POST');
    //     console.log(response);
    //
    // }
    // catch (error) {
    //     console.log(error);
    // }


for (let addFriend of addFriends) {addFriend.onclick = add}

//
// barcodeBtn.addEventListener('click', makeRequestBarcode)
// mainProductForm.addEventListener('submit', async function (event) {
//     event.preventDefault();
//     try {
//         let data = $(this).serializeJSON();
//         let response = await makeRequest(url_write_off, "POST", data);
//         // TODO исправить на редирект детального просморта
//         // window.location.href = urlRedirect.replace('123', response.success);
//     } catch (e) {
//         alert("Неправильное значение");
//     }
// });