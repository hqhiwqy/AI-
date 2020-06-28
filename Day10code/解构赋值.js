{
    //传统的变量赋值方法
    let arr = [1,2,3];
    let a = arr[0];
    let b = arr[1];
    let c = arr[2];
    console.log(a, b, c);
}

{
    //解构赋值方式
    let arr = [1,2,3];
    let [a, b, c] = arr;
    console.log(a, b, c)
}

//数组的解构赋值
{
    //解构赋值支持嵌套

    let [a, b, [c, d]] = [1, 2, [3, 4]];

    console.log(a,b,c,d); // 1, 2, 3, 4

}

{
    //不完全解构  赋值不成功，变量的值为undefined
    let [a, b, c] = [4, 5];

    console.log(a, b, c);//4 5 undefined

}

{
    //允许设置默认值
    let [a, b, c = 6] = [4, 5];

    console.log(a, b, c);//4 5 6

}

{
    //允许设置默认值
    let [a, b, c = 6] = [4, 5, undefined];

    console.log(a, b, c); // 4 5 6 如果赋值的值为undefined时，最后赋值为默认值

}

{
    //允许设置默认值
    let [a, b, c = 6] = [4, 5, 7];

    console.log(a, b, c);// 4 5 7

}


{
    //数组的解构赋值受排列次序的影响

    let [b, a, [d, c]] = [1, 2, [3, 4]];

    console.log(a,b,c,d); // 2, 1, 4,3

}

// 对象的解构赋值
{
    let {a, b, c} = {a : 1, b : 2, c : 3};
    console.log(a, b, c) //  1, 2, 3
}

{

    //对象的解构赋值和数组的解构赋值基本一致，但对象的解构赋值不会受到属性的排列次序影响
    let {a, b, c} = {c : 3, b : 2, a : 1};
    console.log(a, b, c) //  1, 2, 3
}

{
    let oData = {
        "reason": "查询物流信息成功",
        "result": {
          "company": "EMS", /* 快递公司名字 */
          "com": "ems",
          "no": "1186465887499", /* 快递单号 */
          "status": "1", /* 1表示此快递单的物流信息不会发生变化，此时您可缓存下来；0表示有变化的可能性 */
          "status_detail": "PENDING", /* 详细的状态信息，可能为null，仅作参考。其中：
              PENDING 待查询
              NO_RECORD 无记录
              ERROR 查询异常
              IN_TRANSIT 运输中
              DELIVERING 派送中
              SIGNED 已签收
              REJECTED 拒签
              PROBLEM 疑难件
              INVALID 无效件
              TIMEOUT 超时件
              FAILED 派送失败
              SEND_BACK 退回
              TAKING 揽件 */
          "list": [
            {
              "datetime": "2016-06-15 21:44:04",  /* 物流事件发生的时间 */
              "remark": "离开郴州市 发往长沙市【郴州市】", /* 物流事件的描述 */
              "zone": "" /* 快件当时所在区域，由于快递公司升级，现大多数快递不提供此信息 */
            },
            {
              "datetime": "2016-06-15 21:46:45",
              "remark": "郴州市邮政速递物流公司国际快件监管中心已收件（揽投员姓名：侯云,联系电话:）【郴州市】",
              "zone": ""
            },
            {
              "datetime": "2016-06-16 12:04:00",
              "remark": "离开长沙市 发往贵阳市（经转）【长沙市】",
              "zone": ""
            },
            {
              "datetime": "2016-06-17 07:53:00",
              "remark": "到达贵阳市处理中心（经转）【贵阳市】",
              "zone": ""
            },
            {
              "datetime": "2016-06-18 07:40:00",
              "remark": "离开贵阳市 发往毕节地区（经转）【贵阳市】",
              "zone": ""
            },
            {
              "datetime": "2016-06-18 09:59:00",
              "remark": "离开贵阳市 发往下一城市（经转）【贵阳市】",
              "zone": ""
            },
            {
              "datetime": "2016-06-18 12:01:00",
              "remark": "到达  纳雍县 处理中心【毕节地区】",
              "zone": ""
            },
            {
              "datetime": "2016-06-18 17:34:00",
              "remark": "离开纳雍县 发往纳雍县阳长邮政支局【毕节地区】",
              "zone": ""
            },
            {
              "datetime": "2016-06-20 17:55:00",
              "remark": "投递并签收，签收人：单位收发章 *【毕节地区】",
              "zone": ""
            }
          ]
        },
        "error_code": 0 /* 错误码，0表示查询正常，其他表示查询不到物流信息或发生了其他错误 */
      }

    //   let list = oData.result.list
    //   let company = oData.result.company

    //   console.log(list, company)

    let {error_code, result, result: {list, company, com, no}} = oData

    console.log(error_code, list, company, com, no)
}


//字符串的解构赋值

{
    let [a, b, c, d, e, f, g, h, i, m] = "我是一个哇塞的男孩！"
    console.log(a, b, c, d, e, f, g, h, i, m)

}

//解构赋值的用途

{
    //交换变量的值

    //传统方式

    var x = 10;
    var y = 20;
    var z = x;
    x = y;
    y = z;
    console.log(x,y); //20,10

    //解构赋值方式
    [x,y] = [y,x];
    console.log(x,y);//10,20

}

{
    //提取函数返回的多个值
    function getUserInfo(){
        //……省略
        return{
            name:"caocao",
            age:18,
            sex:'男',
            address:"孝义"
        }
    }
    let {name, age} = getUserInfo()
    console.log(name,age)
}

{
    //定义函数的参数
    function setUserInfo({name, age}){
        console.log(name, age)
    }
    setUserInfo({name:'LIZI',age:20})
}

{
    //函数参数的默认值
    function sum({a=0, b=0}){
        return a + b;
    }

}