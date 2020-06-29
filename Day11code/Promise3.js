
//Promise 基本用法

/*
    new Promise(function(resolve, reject){
        ……

    })

*/

let pro1 = new Promise(function(resolve,reject){
    //实例化的时候，刚离开的状态时pending（进行中）
    if(false){
        resolve('Success!') //状态由pending -> resolved（成功）
    }else{
        reject('Failed!') //状态由pending -> rejected(失败)
    }

})

pro1.then(function(res){
    console.log(res)
}).catch(function(err){
    console.log(err)
})

//结合箭头函数一起使用
pro1.then((res)=>{
    console.log(res)
}).catch((err)=>{
    console.log(err)
})