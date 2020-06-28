//同一个块级作用域内，不允许重复声明同一个变量

/*
(function(){
    var a = 1;
    let a = 2;   //报错！不能重复声明同一个变量
})();
*/

//正确方法：
(function(){
    let b = 1;
})();
    let b = 2;
    console.log(b)

//函数内不能用let重新声明函数的参数

function test(str){
    //let str = "caocao" //报错！
    console.log(str)
}
test('caocao')

//先声明后使用！！