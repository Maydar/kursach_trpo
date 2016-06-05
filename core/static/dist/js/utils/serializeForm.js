'use strict';

var _typeof = typeof Symbol === "function" && typeof Symbol.iterator === "symbol" ? function (obj) { return typeof obj; } : function (obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol ? "symbol" : typeof obj; };

define(['jquery', 'lodash'], function ($, _) {
    return function (form) {
        var result = {};
        _.each($(form).serializeArray(), function (element) {
            var regexp = /\[(\w+)\]/ig;
            var matchField = element.name.match(regexp);
            if (matchField == null) {
                result[element.name] = element.value;
            } else {
                var fieldName = element.name.slice(0, element.name.search(regexp));
                var walkFields = function walkFields(object, chain, value) {
                    if (chain.length == 0) {
                        if (!isNaN(parseInt(value)) && String(parseInt(value)).length === value.length) {
                            return parseInt(value);
                        }
                        if (!isNaN(parseFloat(value)) && String(parseFloat(value)).length === value.length) {
                            return parseFloat(value);
                        }
                        return value;
                    } else {
                        var indexName = chain[0].slice(1, chain[0].length - 1);
                        if (isNaN(parseInt(indexName)) || String(parseInt(indexName)).length !== indexName.length) {
                            if (object === undefined) {
                                object = {};
                            }
                        } else {
                            if (object === undefined) {
                                object = [];
                            }
                        }
                        object[indexName] = walkFields(object[indexName], chain.slice(1), value);
                    }
                    return object;
                };
                result[fieldName] = walkFields(result[fieldName], matchField, element.value);
            }
        });

        _.map(result, function (value, key) {
            if ((typeof value === 'undefined' ? 'undefined' : _typeof(value)) === 'object') {
                if (Array.isArray(value)) {
                    var nullLessArray = [];
                    for (var i = 0; i < value.length; i++) {
                        if (value[i] !== null && value[i] !== undefined) {
                            nullLessArray.push(value[i]);
                        }
                    }
                    value = nullLessArray;
                }
                result[key] = value;
            }
        });
        return result;
    };
});