const fs = require('fs')
const { resolve } = require('path')
const { reject } = require('assert')

let readFile = (filePath,ms) =>{
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            fs.readFile(filePath, 'utf-8', (err,data)=>{
                if(err){
                    reject(err)
                }else{
                    resolve(data)
                }
            })
        },ms)
    })
}

readFile('a.txt',1000).then(res =>{
    console.log(res)
    return readFile('b.txt',800)
}).then(res =>{
    console.log(res)
    return readFile('c.txt',500)
}).then(res =>{
    console.log(res)
}).catch(err => {
    console.error(err)
})