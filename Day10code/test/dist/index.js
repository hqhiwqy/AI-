"use strict";

var hello = "hello es6!";
var  PI = 3.14;
class Person{
    constructor(name,age){
        this.name = name
        this.age = age
    }
    say(){
        return`我叫${this.name},今年${this.age}岁`
    }
}
console.log(hello,PI)