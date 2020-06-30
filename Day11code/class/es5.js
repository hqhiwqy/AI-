//流行的面向对象的编写方式： 构造函数+原型混合方式，其中构造函数负责添加属性，原型负责添加方式。

//定义一个人类

//构造函数添加属性
function Person(name, age){
    this.name = name;
    this.age = age;
}

//原型添加方法
Person.prototype.say = function(){
    return `我叫${this.name},今年${this.age}岁。`
}
let p1 = new Person('张三',18);
console.log(p1.say());


//定义一个学生类Student来继承Person类

//首先继承构造函数

function Student(name,age,school){
    Person.call(this, name, age);
    //子类可以拥有自己的属性
    this.school = school;
}

//然后继承原型

//原型prototype的本质其实是一个对象

//Student.prototype = Person.prototype   //传址赋值，这样会造成子类影响父类！

for(let i in Person.prototype){
    Student.prototype[i] = Person.prototype[i]
}

//子类可以拥有自己的方法
Student.prototype.study = function(){
    return `我叫${this.name},我在${this.school}读书`
}

let s1 = new Student('李四',28,'zbdx');

console.log(s1.say());
console.log(s1.study());