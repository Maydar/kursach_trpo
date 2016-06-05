require(['./config'], function () {
   require(['jquery', 'lodash', 'utils/serializeForm', 'cookies'], 
       ($, _, serializeForm, Cookies) => {
           let $form = $('form#article');
       
           $form.on('focus', '.js-input' , (e) => {
              hideFormError(e.target);
           });
           
           $form.submit((event) => {
               event.preventDefault();
               let data = serializeForm($form);
               
               $.ajax({
                   url: $form.attr('action'),
                   method: 'POST',
                   data: data,
                   dataType: 'json',
                   
                   success: (response) => {
                       if (response.status === 'OK') {
                           $form.hide();
                           $('.message_success').show();
                       } else {
                           showFormErrors($form, response.message);
                       }
                   }
               });
           });
    
           $('.js-delete').click((event) => {
               event.preventDefault();
               $.ajax({
                   url: $(event.target).attr('href'),
                   method: 'POST',
                   data: {
                       'csrfmiddlewaretoken' : Cookies.get('csrftoken')
                   },
                   dataType: 'json',
                   success: (response) => {
                       if (response.status === 'OK') {
                           $form.hide();
                           $('.message_success-delete').show();
                       } 
                   }
               })
           });
       });
});