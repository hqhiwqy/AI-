
//Promise 基本用法

/*
    new Promise(function(resolve, reject){
        ……

    })

*/

let pro1 = new Promise(function(resolve,reject){
    //实例化的时候，刚离开的状态时pending（进行中）
    if(true){
        resolve('Success!') //状态由pending -> resolved（成功）
    }else{
        reject('Failed!') //状态由pending -> rejected(失败)
    }

})

//实例方法
//then 方法：用于指定发生状态改变时的回调函数。它的第一个参数是 Resolved 状态的回调函数，第二个参数（可选）是 Rejected 状态的回调函数。
//catch 方法：用于指定发生错误时的回调函数。它的参数是 Rejected状态的回调函数。
pro1.then(function(res){
    console.log(res)
})

pro1.catch(function(err){
    console.log(err)
})