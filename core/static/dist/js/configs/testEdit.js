'use strict';

require(['./config'], function () {
    require(['jquery', 'lodash', 'utils/composite'], function ($, _, Composite) {
        $('.js-question-save').click(function (e) {
            e.preventDefault();
        });

        $('.test-edit__save').click(function (e) {
            e.preventDefault();
        });
    });
});