let content_shop = $('#content-shop');
let block_pagination = $('#block_pagination');
let list_shop = $('#list_shop');
let url_datail_product = list_shop.data('url');
let url_detail = content_shop.data('url-detail').slice(0, -2);

$(document).ready(function () {
    if(content_shop.data('search') !== 'None'){
        get_list_product(content_shop.data('url') + '?searchp=' + content_shop.data('search'))
    }
    else if(content_shop.data('category') !== 'None'){
        get_list_product(content_shop.data('url') + '?category=' + content_shop.data('category'))
    }
    else{
        get_list_product()
    }

    if(content_shop.data('category') !== 'None')
        get_list_product(content_shop.data('url') + '?category=' + content_shop.data('category'))

    block_pagination.on('click', '#next', function () {
        get_list_product($(this).data('href'))
    })
    block_pagination.on('click', '#previous', function () {
        get_list_product($(this).data('href'))
    })

    list_shop.on('click', '.quick_button', function () {
        get_detail_product($(this).data('id'));
    })

    $('.select_option ul').on('click', 'li', function () {
        content_shop.attr('data-search', null);
        get_list_product(content_shop.data('url') + '?category=' + $(this).data('value'))
    })
})

function get_detail_product(id_product) {
    $.ajax({
        type: 'GET',
        url: url_datail_product + id_product.toString()
    }).then((data) => {
        $('#titulo_modal').html(data.name)
        $('#descripcion_modal').html(data.description)
        let html = '';
        let gallery = data.gallery;
        for (let foto in gallery) {
            let active = '';
            if (foto === '0') {
                active = 'show active';
            }
            html += `<div class="tab-pane fade ${active}" id="tab${gallery[foto].id}" role="tabpanel">
                            <div class="modal_tab_img">
                                <a href="#"><img src="${gallery[foto].imagen}" alt=""></a>
                            </div>
                        </div>`;
        }
        $('#detail_foto').html(html)

        html = '<ul class="nav product_navactive owl-carousel" role="tablist" >'
        for (let foto in gallery) {
            let active = '';
            if (foto === '0') {
                active = 'show active';
            }
            html += `<li>
                        <a class="nav-link ${active}" data-toggle="tab" href="#tab${gallery[foto].id}"
                        role="tab" aria-controls="tab${gallery[foto].id}" aria-selected="false">
                            <img src="${gallery[foto].imagen}" alt="">
                        </a>
                     </li>`
        }
        html += '</url>'
        $('#multi_gallery').html(html)

        $('.product_navactive').owlCarousel({
            loop: true,
            nav: true,
            autoplay: false,
            autoplayTimeout: 8000,
            items: 4,
            dots: false,
            navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
            responsiveClass: true,
            responsive: {
                0: {
                    items: 1,
                },
                250: {
                    items: 2,
                },
                480: {
                    items: 3,
                },
                768: {
                    items: 4,
                },

            }
        });

        $("#modal_box").modal('show');


    })
}

function get_list_product(url_page = null) {
    let url = content_shop.data('url')
    if (url_page != null)
        url = url_page
    $.ajax({
        type: 'GET',
        url: url
    }).then((data) => {
        let page = data.page;
        let link = data.links;
        let total = data.total;
        let results = data.results;
        construccion_listado_productos(results)
        construccion_numero_paginado(page, link, total);
    })
}

function construccion_numero_paginado(page, link, total) {
    let html = ''

    if (link.previous != null) {
        html += `<li class="previous"><a id="previous" data-href="${link.previous}">anterior</a></li>`
    }
    html += `<li class="current">${page}</li>`
    if (link.next != null) {
        html += `<li class="next"><a id="next" data-href="${link.next}">siguiente</a></li>`
    }

    $('#block_pagination ul').html(html)
}

function construccion_listado_productos(results) {
    let html = ''
    for (let indice in results) {
        html += `<div class="col-lg-3 col-md-4 col-12 obj_product">
                    <article class="single_product">
                        <figure>
                            <div class="product_thumb">
                                <a class="primary_img" href="${url_detail}${results[indice].id}">
                                    <img src="${results[indice].cover_image}" alt="">
                                </a>
                                <div class="action_links">
                                    <ul>
                                        <li class="quick_button" data-id="${results[indice].id}">
                                            <a title="quick view">
                                                <i class="icon-eye"></i>
                                            </a>
                                        </li>
                                    </ul>
                                </div>
                                <div class="action_links list_action">
                                    <ul>
                                        <li class="quick_button" data-id="${results[indice].id}">
                                            <a title="quick view">
                                                <i class="icon-eye"></i>
                                            </a>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                            <div class="product_content grid_content">
                                <div class="product_price_rating">
                                    <h4 class="product_name">
                                        <a href="${url_detail}${results[indice].id}">${results[indice].name}</a>
                                    </h4>
                                </div>
                            </div>
                            <div class="product_content list_content">
                                <h4 class="product_name">
                                    <a href="${url_detail}${results[indice].id}">${results[indice].name}</a>
                                </h4>
                                <div class="price_box">
                                    <span class="current_price">S/.${results[indice].precio}</span>
                                </div>
                                <div class="product_desc">
                                    <p>${results[indice].description}</p>
                                </div>
                                <div class="action_links list_action_right">
                                    <ul>
                                        <li class="add_to_cart">
                                            <a href="{% url 'app-website:contact' %}" title="Add to cart">Consultar stock</a>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </figure>
                    </article>
                </div>`
    }
    list_shop.html(html);
}