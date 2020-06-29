//Promise.all()

const { resolve } = require("path");

//Promise.race()

//创建pro1对象

let pro1 = new Promise((resolve,reject)=>{
   setTimeout(()=>{ 
    if(true){
        resolve('Success1!')
    }else{
        reject('Failed1!')
    }
    },3000)
})

let pro2 = new Promise((resolve,reject)=>{
    
    setTimeout(()=>{
    if(false){
        resolve('Success2!')
    }else{
        reject('Failed2!')
    }
    },2000)
})

/* Promise.race 方 法 ： 接受一个数组作为参数 ， 数组的元素是Promise 实例对象，
当参数中的实例对象只要有一个状态发生变化（不管成功状态还是异常状态），它就会返回那个结果，不会等所有Promise 都执行完。
*/

Promise.race([pro1,pro2]).then((res) =>{
    console.log(res)
}).catch((err) =>{
    console.error(err)  
})