window.onload = function () {
    
        //获取label元素对象，并且赋值给变量oLabel
        var oLabel = document.getElementById('J_remmber')

        //获取div元素对象，并且赋值给变量oDiv
        var oDiv = document.getElementById('J_tips')

        //给oLabel元素对象绑定鼠标移入事件
        oLabel.onmouseover = function(){
            oDiv.style.display = "block"
        }

        //给oDiv元素对象绑定鼠标移出事件
        oDiv.onmouseout = function(){
            oDiv.style.display = "none"
        }
    }