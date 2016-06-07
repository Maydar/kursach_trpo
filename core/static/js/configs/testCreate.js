require(['./config'], () => {
    require(['jquery', 'lodash', 'utils/composite'],
        ($, _, Composite) => {
            let test = new Composite.Test($('.test-edit'), []),
                $addQuestion = $('js-question-add'),
                self = this;

            test.selector.on('focus', '.js-input' , (e) => {
              hideFormError(e.target);
            });
            
            
            $('.js-question-save').click((e) => {
               e.preventDefault(); 
            });
            
            $addQuestion.click((e) => {
                e.preventDefault();
                let $form = $('#hidden-question')
                    .clone(true, true)
                    .attr('id', getNextFormId('.question', 'question'))
                    .show();
                
                $("#id-question").append($form);
                question = new Question($form);
                test.add(question);
            });
            
            test.selector.submit((e) => {
                e.preventDefault();
                $.ajax({
                   url: test.selector.attr('action'),
                   method: 'POST',
                   data: test.serialize($),
                   dataType: 'json',

                   success: (response) => {
                       if (response.status === 'OK') {
                           $form.hide();
                           $('.message_success').show();
                       } else {
                           showFormErrors(test.selector, response.message);
                       }
                   }
               });
            });
        });
});