'use strict';

require(['./config'], function () {
    require(['jquery', 'lodash', 'utils/composite', 'text!app/test/test.html'], function ($, _, Composite, TestTemplate) {
        var $beginTest = $('.test-brief__begin-test'),
            $testWrapper = $('.test'),
            $addAnswer = $('.answer-variant__add');
        var template = _.template(TestTemplate);

        $beginTest.click(function (event) {
            event.preventDefault();
            $beginTest.hide();
            $(template({
                number: 1,
                title: "Первый вопрос",
                text: "Lorem ipsum dolor sit amet, consectetur adipisicing elit. A aliquid architecto assumenda at blanditiis " + "consectetur cumque delectus dolorum ducimus esse est harum, laudantium porro quae quam " + "recusandae soluta voluptate voluptatibus.",
                answers: [{
                    text: "123"
                }, {
                    text: "456"
                }]
            })).appendTo($testWrapper).hide().fadeIn();
        });

        $addAnswer.click(function (event) {
            event.preventDefault();
            var $target = $(event.target);
            if ($target.parents('.form__line').find('.answer-variant').length > 3) {
                return;
            } else {
                $target.parent().after($target.parent().clone(true));
            }
        });
    });
});