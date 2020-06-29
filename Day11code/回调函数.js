const { threadId } = require("worker_threads");

function first(){
    console.log(1);
}

function second(){
    console.log(2);
}

function third(){
    console.log(3);
}

first();
second();
third();