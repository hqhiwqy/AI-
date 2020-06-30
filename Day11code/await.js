// await 就是异步等待，它等待一个Promise对象，所有await后面应该写一个Promise对象
// 如果不是promise，就被立即 resolve的Promise

async function fnA(){
    console.log('async function is running!')
    const num1 = await 100;
    console.log(`num1 is ${num1}`);
    const num2 = await num1 + 100;
    console.log(`num2 is ${num2}`);
    const num3 = await num2 + 100;
    console.log(`num3 is ${num3}`);
}

fnA();
console.log('run me before await!');

//async 函数被调用后立即执行，但是一旦遇到 await 就会返回，等到异步操作执行完成，再接着
//执行函数体内后面的语句。

//*结论：async 函数调用不会造成代码的阻塞，但是await会引起async函数内部的代码阻塞。