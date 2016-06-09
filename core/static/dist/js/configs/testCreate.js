'use strict';

require(['./config'], function () {
    require(['jquery', 'lodash', 'utils/composite'], function ($, _, Composite) {
        var test = new Composite.Test($('.test-edit'), []),
            question_0 = new Composite.Question($('#question_0')),
            $addQuestion = $('.js-question-new'),
            $addAnswer = $('.answer-variant__add'),
            $removeQuestion = $('.js-remove'),
            self = undefined;

        test.add(question_0);
        test.selector.on('focus', '.js-input', function (e) {
            hideFormError(e.target);
        });

        test.selector.on('change', '.js-input', function (e) {
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
            var question = new Composite.Question($form);
            test.add(question);
        });

        $addAnswer.click(function (event) {
            event.preventDefault();
            var $target = $(event.target);
            if ($target.parents('.form__line').find('.answer-variant').length > 3) {} else {
                $target.parent().after($target.parent().clone(true));
            }
        });

        test.selector.submit(function (e) {
            e.preventDefault();
            console.log({ data: test.serialize($) });
            e.preventDefault();
            $.ajax({
                url: test.selector.attr('action'),
                method: 'POST',
                data: { data: test.serialize($) },
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