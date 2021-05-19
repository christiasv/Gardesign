let div_block = $('#div_block');
let block_pagination = $('#block_pagination');
let buscar = $('#buscar');
let  url_detail = div_block.data('url-detail').slice(0, -2);

$(document).ready(function () {
    get_list_block();
    block_pagination.on('click', '#next', function () {
        get_list_block($(this).data('href'))
    })
    block_pagination.on('click', '#previous', function () {
        get_list_block($(this).data('href'))
    })

    buscar.on('click', function () {
        let search = $('#search_c').val()
        get_list_block(search, true)
    })
})

function get_list_block(search = '', is_search = false) {
    let url = ''
    if (is_search === true) {
        url = div_block.data('url') + '?title=' + search.toString()
    } else {
        url = div_block.data('url') + search.toString()
    }
    $.ajax({
        type: 'GET',
        url: url
    }).then((data) => {
        let page = data.page;
        let link = data.links;
        let total = data.total;
        let results = data.results;
        construccion_listado_blocks(results)
        construccion_numero_paginado(page, link, total);
    })
}

function construccion_numero_paginado(page, link, total) {
    let html = ''

    if (link.previous != null) {
        html += `<li class="previous"><a id="previous" data-href="${link.previous}">next</a></li>`
    }
    html += `<li class="current">${page}</li>`
    if (link.next != null) {
        html += `<li class="next"><a id="next" data-href="${link.next}">next</a></li>`
    }

    $('#block_pagination ul').html(html)
}

function construccion_listado_blocks(results) {
    let html = ''
    for (let indice in results) {
        let fecha = moment(results[indice].created).format('DD/MM/YYYY HH:mm:ss');
        html += `<article class="single_blog">
                    <figure>
                        <div class="blog_thumb">
                            <a href="${url_detail}${results[indice].id}"><img src="${results[indice].image}" alt=""></a>
                        </div>
                        <figcaption class="blog_content">
                           <h4 class="post_title"><a href="${url_detail}${results[indice].id}">
                                <i class="fa fa-paper-plane"></i>${results[indice].title}</a>
                            </h4>
                            <div class="blog_meta">
                                <p>Por <a href="${url_detail}${results[indice].id}">${results[indice].user}</a> / Fecha <a href="#">${fecha}</a></p>
                            </div>
                            <p class="post_desc">${results[indice].descripcion_corta}</p>
                            <footer class="btn_more">
                                <a href="${url_detail}${results[indice].id}"> Leer más</a>
                            </footer>
                        </figcaption>
                    </figure>
                </article>`
    }
    div_block.html(html);
}