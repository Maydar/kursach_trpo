require(['./config'], () => {
    require(['jquery', 'lodash', 'utils/composite'],
        ($, _, Composite) => {
            let $form = $('.test-edit'),
                $addQuestion = $('.js-question-new'),
                $addAnswer = $('.answer-variant__add'),
                $removeQuestion = $('.js-remove');
            
            $form.on('focus', '.js-input' , (e) => {
              hideFormError(e.target);
            });

            $form.on('change', '.js-input', (e) => {
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
            });

            $addAnswer.click((event) => {
               event.preventDefault();
               const $target = $(event.target);
               if ($target.parents('.form__line').find('.answer-variant').length > 3) {} else {
                   $target.parent().after($target.parent().clone(true));
               }
           });
            
            $form.submit((e) => {
                e.preventDefault();
                let data = {
                    test: serializeForm($form),
                    questions: serializeFormSet($('form.question-form'))
                };
                
                e.preventDefault();
                $.ajax({
                   url: $form.attr('action'),
                   method: 'POST',
                   data: data,
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