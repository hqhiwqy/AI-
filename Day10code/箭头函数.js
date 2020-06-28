{
    //传统方式定义函数
        //方式一：
        function he1(x,y){
            return x + y;
        }
        console.log(he1(1,2));

        //方式二：
        let he2 = function(x,y){
            return x + y;
        }
        console.log(he2(1, 2));

        //新的方式：箭头函数
        let he3 = (x, y) => {
            return x + y;
        }
        console.log(he3(1, 2));
}

{
    let Person1 = {
        name: '张三',
        age: 18,
        say(){
            setInterval(function(){
                console.log(this) //this指向window对象

                //
            },1000)
        }
    }
    Person1.say();


    //箭头函数中的this其实是父级作用域中的this

    let Person2 = {
        name: '里斯',
        age: 18,
        say(){
            console.log(this); //this指向Person2对象
            setInterval(() => {
                console.log(this)//this指向Person2对象
                console.log(this.name,this.age) 
            },1000)
        }
    }
    Person2.say();

    //一个常犯的错误：使用箭头函数来定义对象的方法

    let Person3 = {
        name:"栗子",
        age: 20,
        say:()=>{
            console.log(this.name)
        }
    }
    Person3.say() //此时箭头函数的this没有指向Person3对象


}