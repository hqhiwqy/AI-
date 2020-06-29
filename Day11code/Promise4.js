//Promise.all()

const { resolve } = require("path");

//Promise.race()

//创建pro1对象

let pro1 = new Promise((resolve,reject)=>{
    
    if(true){
        resolve('Success1!')
    }else{
        reject('Failed1!')
    }
})

let pro2 = new Promise((resolve,reject)=>{
    
    if(false){
        resolve('Success2!')
    }else{
        reject('Failed2!')
    }
})

//静态方法
//Promise.all 方 法 ： 接受一个数组作为参数 ， 数组的元素是Promises 实例对象，当参数中的实例对象的状态都为 fulfilled 时，才会返回成功。

Promise.all([pro1,pro2]).then((res) =>{
    console.log(res)
}).catch((err) =>{
    console.error(err)  
})