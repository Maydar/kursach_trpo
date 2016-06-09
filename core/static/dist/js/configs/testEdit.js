'use strict';

require(['./config'], function () {
    require(['jquery', 'lodash', 'utils/composite'], function ($, _, Composite) {
        var $form = $('.test-edit'),
            $addQuestion = $('.js-question-new'),
            $addAnswer = $('.answer-variant__add'),
            $removeQuestion = $('.js-remove');

        $form.on('focus', '.js-input', function (e) {
            hideFormError(e.target);
        });

        $form.on('change', '.js-input', function (e) {
            $('.test-edit__save').removeAttr('disabled');
        });

        $removeQuestion.click(function (e) {
            e.preventDefault();
            $(e.target).closest('form').remove();
        });

        $addQuestion.click(function (e) {
            e.preventDefault();
            var $form = $('#hidden-question').clone(true, true).attr('id', getNextFormId('.question', 'question')).show();

            $addQuestion.before($form);
        });

        $addAnswer.click(function (event) {
            event.preventDefault();
            var $target = $(event.target);
            if ($target.parents('.form__line').find('.answer-variant').length > 3) {} else {
                $target.parent().after($target.parent().clone(true));
            }
        });

        $form.submit(function (e) {
            e.preventDefault();
            var data = {
                test: serializeForm($form),
                questions: serializeFormSet($('form.question-form'))
            };

            e.preventDefault();
            $.ajax({
                url: $form.attr('action'),
                method: 'POST',
                data: data,
                dataType: 'json',

                success: function success(response) {
                    if (response.status === 'OK') {
                        $('#id-question').hide();
                        $('.message_success').show();
                    } else {
                        showFormErrors(test.selector, response.message);
                    }
                }
            });
        });
    });
});