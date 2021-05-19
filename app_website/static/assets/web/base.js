let form_search = $('#form_search');
let url = form_search.data('url');
let redirect = form_search.data('redirect');

$(document).ready(function () {
    form_search.on('submit', function (e) {
        e.preventDefault();
        let p_search = $('#input_s').val()
        window.location.replace(redirect + '?search_inicial=' + p_search);
    })
})