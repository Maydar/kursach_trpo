'use strict';

define(['jquery'], function ($, serializeForm) {
    
    class Form {
        constructor(selector) {
            this.selector = selector;
        }

        serialize($) {
            //$ajax
        }
        
        add() {
            //
        }
    }
    
    class Test extends Form {
        constructor(selector, questions) {
            super(selector);
            this.questions = questions;
        }

        serialize($) {
            var result = {
                questions: {}
            };
            for (var i = 0; i < this.questions.length; i++) {
                var id = this.questions[i].selector.attr('id');
                result.questions[id] = this.questions[i].serialize($);
            }
            
            var dataId = this.selector.attr('id');
            result[dataId] =  _serializeFrom(this.selector);
            return JSON.stringify(result);
        }
        
        add(question) {
            this.questions.push(question);
        }
    }

    class Question extends Form {
        constructor(selector) {
            super(selector);
        }
        
        serialize($) {
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
    }
    return {
        Test: Test,
        Question: Question,
        Form: Form
    }
});




