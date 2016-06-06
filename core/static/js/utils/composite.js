'use strict';

define(['jquery'], function ($) {
    class Test extends Field {
        constructor(fields, questions) {
            super("test", "test", {});
            this.questions = questions;
        }
        add(object) {
            if (object instanceof Question) {
                this.questions.append(object);
            } else if (object instanceof Field) {
                this.fields.append(object);
            }
        }
        
        print() {
            this.questions.forEach((item, i, arr) => {
                item.print();
            })
        }
    }

    class Question extends Field {
        constructor(fields) {
            super("question", "question", {});
        }

        print() {
            this.fields.forEach((item, i, arr) => {
                item.print(this.$el)
            });
        }
    }
    
    class Field {
        constructor(type, name, options) {
            this.type = type;
            this.name = name;
            this.options = options;
        }

        print($el) {
            $el.append(this);
        }
    }

    return {
        Test: Test,
        Question: Question,
        Field: Field
    }
});




