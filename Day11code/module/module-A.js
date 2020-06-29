//模块A

let title = "ES6模块化"
let desc = "一个JS中确实已久的新特性"
let hello = () => {
    console.log("hello ES6模块化")
}


//导出属性和方法

//默认导出——default常用的设置方式

export default{
    title,
    desc
}