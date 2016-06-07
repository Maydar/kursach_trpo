require(['./config'], () => {
    require(['jquery', 'lodash', 'utils/composite'],
        ($, _, Composite) => {
            $('.js-question-save').click((e) => {
               e.preventDefault(); 
            });
        
            $('.test-edit__save').click((e) => {
                e.preventDefault();
            })
        });
});