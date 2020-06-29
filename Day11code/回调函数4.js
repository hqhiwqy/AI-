function first(callback){
    setTimeout(()=>{
        console.log(1);
        if(callback)callback();
    },500);
}


//需求：我们希望的顺序是先执行first，再执行second，可以通过回调函数的方式来实现同步的功能。
first(function(){
    console.log(2);
});
