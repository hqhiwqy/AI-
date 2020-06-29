/*JavaScript 是一个单线程的编程语言
    所谓单线程，就是指一次只能完成一件任务。如果有多个任务，就必须排队，前面一个任务完成，再执行后面一个任务，依次类推。*/

//同步：只能等到前面的任务完成了，才能继续下一个任务。
//异步：不需要等待前面的任务完成，也可以执行下一个任务。

console.log(1);
console.log(2);
console.log(3);

console.log("张三");

setTimeout(()=>{
    console.log("李四");
},1000)

setTimeout(()=>{
    console.log("王五");
},800)

setTimeout(()=>{
    console.log("赵六");
},500)

    console.log("田七")