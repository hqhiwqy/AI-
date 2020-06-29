const fs = require('fs')

let readFile =(filePath,callback) =>{
    fs.readFile(filePath,'utf-8',(err,data)=>{
        if(err){
            console.error(err)
        }else{
            console.log(data)
            if(callback){callback()}
        }
    })
}
/* readFile('a.txt')
readFile('b.txt')
readFile('c.txt')
 */

 readFile('a.txt',()=>{
    readFile('b.txt',()=>{
        readFile('c.txt',()=>{

        })
    })
 })

 //回调地狱  层层嵌套，代码不易阅读也不宜维护