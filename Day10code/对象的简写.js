let {name, age} = {name: '张三', age: 18}

// 对象属性的简写  对象的属性名和变量名相同才能简写。

let Person = {
    name,
    age
}

console.log(Person)

// 对象方法的简写

let Person2 = {
    say(){
        console.log('hello');
    }
}

Person2.say();