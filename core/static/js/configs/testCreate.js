require(['./config'], () => {
    require(['jquery', 'lodash', 'utils/composite'],
        ($, _, Composite) => {
            let test = new Composite.Test($('.test-edit'), []),
                question_0 = new Composite.Question($('#question_0')),
                $addQuestion = $('.js-question-new'),
                $addAnswer = $('.answer-variant__add'),
                $removeQuestion = $('.js-remove'),
                self = this;

            test.add(question_0);
            test.selector.on('focus', '.js-input' , (e) => {
              hideFormError(e.target);
            });

            test.selector.on('change', '.js-input', (e) => {
               $('.test-edit__save').removeAttr('disabled');
            });
            
            
            $removeQuestion.click((e) => {
                e.preventDefault();
                $(e.target).closest('form').remove();
            });
            
            $addQuestion.click((e) => {
                e.preventDefault();
                let $form = $('#hidden-question')
                    .clone(true, true)
                    .attr('id', getNextFormId('.question', 'question'))
                    .show();
                
                $addQuestion.before($form);
                let question = new Composite.Question($form);
                test.add(question);
            });

            $addAnswer.click((event) => {
               event.preventDefault();
               const $target = $(event.target);
               if ($target.parents('.form__line').find('.answer-variant').length > 3) {} else {
                   $target.parent().after($target.parent().clone(true));
               }
           });
            
            test.selector.submit((e) => {
                e.preventDefault();
                console.log({ data: test.serialize($) });
                e.preventDefault();
                $.ajax({
                   url: test.selector.attr('action'),
                   method: 'POST',
                   data: { data: test.serialize($) },
                   dataType: 'json',

                   success: (response) => {
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