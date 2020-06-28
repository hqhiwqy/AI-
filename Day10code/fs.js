let fs = require("fs")
fs.readFile('data.txt','utf-8',function (err,data) {
    if (err) {
        console.error(err)              
    } else {
        console.log(data)
    }
})