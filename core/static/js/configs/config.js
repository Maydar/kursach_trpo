require.config({
    baseUrl: '/static',
    paths: {
        'jquery': 'bower_components/jquery/dist/jquery',
        'lodash': 'bower_components/lodash/dist/lodash',
        'text': 'bower_components/text/text',
        'cookies': 'bower_components/js-cookie/src/js.cookie',
         
        
        'utils': 'dist/js/utils',
        'app': 'dist/js/app'
   }
});

function _serializeFrom(form) {
    var data = form.serializeArray();
    var result = {};
    for (var i = 0; i < data.length; i++) {
        var name = data[i].name;
        if (!(name in result)) {
            result[name] = data[i].value;
        } else {
            if (result[name].constructor === Array) {
                result[name].push(data[i].value);
            } else {
                result[name] = [result[name], data[i].value];
            }
        }
    }
    return result;
}

function serializeForm(form) {
    var result = _serializeFrom(form);
    return JSON.stringify(result);
}

function serializeFormSet(forms) {
    var result = {};
    for (var i = 0; i < forms.length; i++) {
        var form = forms[i];
        var id = $(forms[i]).attr('id');
        result[id] = _serializeFrom($(form));
    }
    return JSON.stringify(result);
}

function appendError(form, name, error) {
    var $errorEl = $(form).find('#error_' + name);
    $errorEl.removeClass('hidden')
        .find('.js-error-text')
        .html(error);
}

function showFormErrors(form, errors) {
    for (var name in errors) {
        if (errors.hasOwnProperty(name)) {
            appendError(form, name, errors[name]);
        }
    }
}

function hideFormError(input) {
    $(input).next().addClass('hidden')
        .find('.js-error-text')
        .val('')
}

require(['jquery', 'cookies'], function ($, Cookies) {
    $.ajaxSetup({
        headers: { "X-CSRFToken": Cookies.get("csrftoken") }
    });
});