'use strict';

require(['./config'], function () {
    require(['jquery', 'lodash', 'utils/composite'], function ($, _, Composite) {
        var test = new Composite.Test($('.test-edit'), []),
            $addQuestion = $('js-question-add'),
            self = undefined;

        test.selector.on('focus', '.js-input', function (e) {
            hideFormError(e.target);
        });

        $addQuestion.click(function (e) {
            e.preventDefault();
            var $form = $('#hidden-question').clone(true, true).attr('id', getNextFormId('.question', 'question')).show();

            $("#id-question").append($form);
            question = new Question($form);
            test.add(question);
        });

        test.selector.submit(function (e) {
            e.preventDefault();
            console.log(test.serialize($));
            //  $.ajax({
            //     url: test.selector.attr('action'),
            //     method: 'POST',
            //     data: test.serialize($),
            //     dataType: 'json',
            //
            //     success: (response) => {
            //         if (response.status === 'OK') {
            //             $form.hide();
            //             $('.message_success').show();
            //         } else {
            //             showFormErrors(test.selector, response.message);
            //         }
            //     }
            // });
        });
    });
});