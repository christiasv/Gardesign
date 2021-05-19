let contact_form = $('#contact-form');
let formMessages = $('.form-messege');

$(document).ready(function () {
    save_submit();
});

function save_submit() {
    contact_form.on('submit', function (e) {
        e.preventDefault();
        let formData = new FormData(this);

        $.ajax({
            url: contact_form.data('url-post'),
            type: "POST",
            data: formData,
            processData: false,
            contentType: false,
            headers: {
                'X-CSRFToken': CSRF_TOKEN,
            },
            success: function (result) {
                // Make sure that the formMessages div has the 'success' class.
                $(formMessages).removeClass('error');
                $(formMessages).addClass('success');

                // Set the message text.
                $(formMessages).text('ok');

                // Clear the form.
                $('#contact-form input,#contact-form textarea').val('');
            },
            error: function (result) {
                // Make sure that the formMessages div has the 'error' class.
                $(formMessages).removeClass('success');
                $(formMessages).addClass('error');

                // Set the message text.
                if (data.responseText !== '') {
                    $(formMessages).text(data.responseText);
                } else {
                    $(formMessages).text('Oops! An error occured and your message could not be sent.');
                }
            },
        });
    });
}