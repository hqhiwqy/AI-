async function fnB(){
    console.log('async function is running!');
    try{
        const num1 = await 100;
        console.log(`num1 is ${num1}`);
        const num2 = await Promise.reject('num2 is wrong!');
        console.log(`num2 is ${num2}`);
        const num3 = await num2 + 100;
        console.log(`num3 is ${num3}`);
    }catch (error){
        console.log(error)
    }
}
fnB();
console.log('run me before await!');

// 实际情况，await 后面的 Promise 对象不总是返回 resovled 状态，只要有一个 await 后面的 promise 状态变为 rejected ，
// 那么整个async函数都会中断执行，为了保存错误的位置和错误信息，我们需要使用 try catch语句来封装多个 await 操作。