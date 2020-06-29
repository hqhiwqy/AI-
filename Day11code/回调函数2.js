const { threadId } = require("worker_threads");

function first(){
    setTimeout(()=>{
        console.log(1);
    },500);
}

function second(){
    console.log(2);
}


//需求：我们希望的顺序是先执行first，再执行second，结果并不是我们想要的！
first();
second();
