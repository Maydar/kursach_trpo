'use strict';

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

define(['jquery'], function ($) {
    var Test = function () {
        function Test(fields, questions) {
            _classCallCheck(this, Test);

            this.fields = fields;
            this.questions = questions;
        }

        _createClass(Test, [{
            key: 'add',
            value: function add(object) {
                if (object instanceof Question) {
                    this.questions.append(object);
                } else if (object instanceof Field) {
                    this.fields.append(object);
                    console.log("");
                }
            }
        }, {
            key: 'print',
            value: function print() {}
        }]);

        return Test;
    }();

    var Question = function Question(fields) {
        _classCallCheck(this, Question);

        this.fields = fields;
    };

    var Field = function Field(type, name, options) {
        _classCallCheck(this, Field);

        this.type = type;
        this.name = name;
        this.options = options;
    };

    return {
        Test: Test,
        Question: Question,
        Field: Field
    };
});