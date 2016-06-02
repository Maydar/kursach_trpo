'use strict';

class Test {
    constructor(fields, questions) {
        this.fields = fields;
        this.questions = questions;
    }

    add(object) {
        if (object instanceof Question) {
            
        } else if (object instanceof Field) {

        }
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



