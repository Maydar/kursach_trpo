require(['./config'], function () {
   require(['jquery', 'lodash', 'utils/composite', 'text!app/test/test.html'
   ], ($, _, Composite, TestTemplate) => {
       const
           $beginTest = $('.test-brief__begin-test'),
           $testWrapper = $('.test'),
           $addAnswer = $('.answer-variant__add');
       const template = _.template(TestTemplate);

       $beginTest.click((event) => {
           event.preventDefault();
           $beginTest.hide();
           $(template({
               number: 1,
               title: "Первый вопрос",
               text: "Lorem ipsum dolor sit amet, consectetur adipisicing elit. A aliquid architecto assumenda at blanditiis " +
               "consectetur cumque delectus dolorum ducimus esse est harum, laudantium porro quae quam " +
               "recusandae soluta voluptate voluptatibus.",
               answers: [
                   {
                       text: "123"
                   },
                   {
                       text: "456"
                   }
               ]
           })).appendTo($testWrapper).hide().fadeIn();
       });

       $addAnswer.click((event) => {
           event.preventDefault();
           const $target = $(event.target);
           if ($target.parents('.form__line').find('.answer-variant').length > 3) {} else {
               $target.parent().after($target.parent().clone(true));
           }
       });
   });
});