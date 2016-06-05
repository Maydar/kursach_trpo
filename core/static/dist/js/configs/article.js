'use strict';

require(['./config'], function () {
    require(['jquery', 'lodash', 'utils/serializeForm', 'cookies'], function ($, _, serializeForm, Cookies) {
        var $form = $('form#article');

        $form.on('focus', '.js-input', function (e) {
            hideFormError(e.target);
        });

        $form.submit(function (event) {
            event.preventDefault();
            var data = serializeForm($form);

            $.ajax({
                url: $form.attr('action'),
                method: 'POST',
                data: data,
                dataType: 'json',

                success: function success(response) {
                    if (response.status === 'OK') {
                        $form.hide();
                        $('.message_success').show();
                    } else {
                        showFormErrors($form, response.message);
                    }
                }
            });
        });

        $('.js-delete').click(function (event) {
            event.preventDefault();
            $.ajax({
                url: $(event.target).attr('href'),
                method: 'POST',
                data: {
                    'csrfmiddlewaretoken': Cookies.get('csrftoken')
                },
                dataType: 'json',
                success: function success(response) {
                    if (response.status === 'OK') {
                        $form.hide();
                        $('.message_success-delete').show();
                    }
                }
            });
        });
    });
});