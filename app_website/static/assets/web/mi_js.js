let contenido_servicio = $('#contenido_servicio');

$(document).ready(function () {
    listar_servicios();
})

function listar_servicios() {
    $.ajax({
        type: 'GET',
        url: contenido_servicio.data('url')
    }).then((data) => {
        console.log()

        let html = '<div class="blog_carousel blog_column3 owl-carousel" >'
        for (let x in data) {
            let url_x = contenido_servicio.data('url-detail').slice(0, -2) + data[x].id
            html += `<div class="col-lg-3">
                            <article class="single_blog">
                                <figure>
                                    <div class="blog_thumb">
                                        <a href="${url_x}">
                                            <img src="${data[x].cover_image}" alt="">
                                        </a>
                                    </div>
                                    <figcaption class="blog_content">
                                        <h4 class="post_title"><a href="${url_x}">${data[x].name}</a>
                                        </h4>
                                        <p class="post_desc">${data[x].description_corta}</p>
                                        <footer class="blog_footer">
                                            <a href="${url_x}">Leer más</a>
                                        </footer>
                                    </figcaption>
                                </figure>
                            </article>
                        </div>`
        }
        html += '</div>'
        $('#contenido_servicio').html(html)

        $('.blog_column3').owlCarousel({
            loop: true,
            nav: true,
            autoplay: true,
            autoplayTimeout: 5000,
            items: 3,
            dots: false,
            margin: 30,
            navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
            responsiveClass: true,
            responsive: {
                0: {
                    items: 1,
                },
                768: {
                    items: 2,
                },
                992: {
                    items: 3,
                },
            }
        });
    });
}


