async function fnA(){
    return "hello!"
}

fnA().then(res =>{
    console.log(res)
})

//单独 async 函数，其实和Promise执行的功能是一样的。
//async函数返回一个Promise对象（如果指定的返回值不是Promise对象，也会返回一个Promise，只不过立即resolve）