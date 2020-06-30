//class 类 

//声明一个Person类

class Person{
    //构造方法
    constructor(name, age){
        //属性
        this.name = name;
        this.age =age
    }

    //方法
    say(){
        return `我叫${this.name},今年${this.age}岁`
    }

    //静态方法 static
    static friend(p1,p2){
        return `${p1.name}和${p2.name}是好朋友`
    }
}

//分别实例化对象
let p1 = new Person('张三',18);

let p2 = new Person('李四',28);

//调用实例方式

console.log(p1.say());

console.log(p2.say());

//调用静态方式 由于静态方法是属于类的，不属于实例对象，应该通过类名直接调用

console.log(Person.friend(p1, p2));

//继承

//定义一个学生类Student来继承父类Person

class Student extends Person{
    //构造方法
    constructor(name,age,school){
       
        //子类必须在constructor方法中调用super方法
        //必须先调用super方法菜能使用this，否则会报错。

        //通过super方法来继承父类所有的属性
        super(name,age);

        //子类可以拥有自己的属性
        this.school = school;
    }

    //子类还可以拥有属于自己的方法
    study(){
        return `${this.name}正在${this.school}读书`
    }

    //如果子类和父类的方法同名了，那么子类的这个方法会覆盖父类的方法。有需要才这样！
}



//实例化一个学生类对象

let s1 = new Student('王五',37,'中北大学');

console.log(s1.say());

console.log(s1.study());