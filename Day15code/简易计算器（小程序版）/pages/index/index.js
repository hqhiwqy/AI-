import math from '../../utils/math.min'
Page({
  
  /**
   * 页面的初始数据
   */
  data: {
    //16个键盘的值
    keybords: [
      'clear', '+', '-', '*',
      '7', '8', '9', '/',
      '4', '5', '6', '0',
      '1', '2', '3', '='
  ],
    result: 0, //存储计算结果
    enter:""   //存储输入的值
  },
  //获取键盘值
  getKeyboardValue:function(e){
    //事件对象
    console.log(e)
    let value = e.currentTarget.dataset.value
    console.log(value)
    switch(value){
      case'clear':
        //清楚计算结果和输入的值
        this.setData({
          result: 0,
          enter:""
        })
      break;
      case'=':
      //进行计算结果
      this.setData({
        result: math.evaluate(this.data.enter),
        enter:""
      })
      break;
      default: 
      this.setData({
        enter: this.data.enter + value
      })
    }
  },


  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
    
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {
    
  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {
    
  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
    
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {
    
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {
    
  }
})