//求所有参数的和

//传统的方式
function sum(){
    let result = 0
    let length = arguments.length
    for(let i = 0;i < length; i++){
        result += arguments[i];
    }
    return result
}
console.log(sum(1, 2))
console.log(sum(1, 2, 3, 4))

//新的方式： 剩余参数（rest参数）

function sum2(...values){
    //console.log(values)  //values 参数数组 [1, 2, 3]
    let result = 0 ;
    values.forEach(function(value,index){
        result += value
    })
        return result
    }
console.log(sum2(1,2,3))

function sum2(x,y,...values){
    //console.log(values)  //values 参数数组 [1, 2, 3]
    let result = 0 ;
    values.forEach(function(value,index){
        result += value
    })
        return result
    }
console.log(sum2(1,2,3,4,5)) //3+4+5=12

//扩展运算符  一般结合数组使用，把数组的元素用逗号分割开，组成一个序列。

function sum3(x, y, z){
    return x + y + z;
}

let arr = [1, 2, 3];

console.log(sum3(...arr)); //sum3(...arr) -> sum3(...[1, 2, 3]) -> sum3(1, 2, 3) -> 6
