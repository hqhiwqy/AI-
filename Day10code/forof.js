let  arr = [1,2,3]

//方法一： for循环，不足：不够简洁
let length = arr.length
for(let i = 0; i < length; i ++){
    //……
}

//方式二： forEach()  不足：无法中断整个循环
arr.forEach(function(value,index){
    console.log(index,value)  //index 下标 value 值
})

//方式三： for in 常用于遍历json对象  不足：每次循环得到的索引值是字符串类型

for(let index in arr){
    console.log(index, typeof index);
}

//方式四：for of
/*
for...of：一种新增的用于遍历数据结构的方法。它可以遍历数组、对象、字符串等数据结构。 
• 写法比 for 循环简洁
• 可以用 break 来终止整个循环，或者 continute 来跳出当前循环，继续后面的循环
• 结合 keys() 获取到循环的索引，并且是数字类型，而不是字符串类型
*/ 

for(let value of arr){
    console.log(value, typeof value)
}

for(let index of arr.keys()){
    console.log(index, typeof index)
}

