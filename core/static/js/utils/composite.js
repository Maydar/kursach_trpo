'use strict';

define(['jquery'], function ($) {
    class Test {
        constructor(fields, questions) {
            this.fields = fields;
            this.questions = questions;
        }
    
        add(object) {
            if (object instanceof Question) {
                this.questions.append(object);
            } else if (object instanceof Field) {
                this.fields.append(object);
                console.log("");
            }
        }
        
        print() {
            
        }
    }

    class Question {
        constructor(fields) {
            this.fields = fields;
        }
    }
    
    class Field {
        constructor(type, name, options) {
            this.type = type;
            this.name = name;
            this.options = options;
        }
    }

    return {
        Test: Test,
        Question: Question,
        Field: Field
    }
});




