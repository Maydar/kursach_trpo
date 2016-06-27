'use strict';

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

define(['jquery'], function ($, serializeForm) {
    var Form = function () {
        function Form(selector) {
            _classCallCheck(this, Form);

            this.selector = selector;
        }

        _createClass(Form, [{
            key: 'serialize',
            value: function serialize($) {
                //abstract
            }
        }, {
            key: 'add',
            value: function add() {
                //abstract
            }
        }]);

        return Form;
    }();

    var Test = function (_Form) {
        _inherits(Test, _Form);

        function Test(selector, questions) {
            _classCallCheck(this, Test);

            var _this = _possibleConstructorReturn(this, Object.getPrototypeOf(Test).call(this, selector));

            _this.questions = questions;
            return _this;
        }

        _createClass(Test, [{
            key: 'serialize',
            value: function serialize($) {
                var result = {
                    questions: {}
                };
                for (var i = 0; i < this.questions.length; i++) {
                    var id = this.questions[i].selector.attr('id');
                    result.questions[id] = this.questions[i].serialize($);
                }

                var dataId = this.selector.attr('id');
                result[dataId] = _serializeFrom(this.selector);
                return JSON.stringify(result);
            }
        }, {
            key: 'add',
            value: function add(question) {
                this.questions.push(question);
            }
        }]);

        return Test;
    }(Form);

    var Question = function (_Form2) {
        _inherits(Question, _Form2);

        function Question(selector) {
            _classCallCheck(this, Question);

            return _possibleConstructorReturn(this, Object.getPrototypeOf(Question).call(this, selector));
        }

        _createClass(Question, [{
            key: 'serialize',
            value: function serialize($) {
                var data = this.selector.serializeArray();
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
        }]);

        return Question;
    }(Form);

    return {
        Test: Test,
        Question: Question,
        Form: Form
    };
});