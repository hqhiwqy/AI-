//index.js

import Util from '../../utils/util'

let page = 1 // 页数

const LIMIT = 100 // 每页的个数
Page({

  /**
   * 页面的初始数据
   */
  data: {
    noValue: "",
    dateValue: "",
    dateShow: 0,
    currentDate: new Date().getTime(),
    minDate: new Date(2019, 1, 1).getTime(),
    maxDate: new Date().getTime(),
    formatter(type, value) {
      if (type === 'year') {
        return `${value}年`;
      } else if (type === 'month') {
        return `${value}月`;
      } else if (type === 'day') {
        return `${value}日`;
      }
      return value;
    },
    data: [],
    total: 0,
    loadAll: 1
  },

  dateOpen () {
    this.setData({
      dateShow: 1
    })
  },

  dateClose () {
    this.setData({
      dateShow: 0
    })
  },

  dateConfirm (e) {
    // console.log(e.detail)
    const dateValue=  Util.formatTime(new Date(e.detail))
    // console.log(dateValue)
    this.setData({
      dateValue,
      dateShow: 0
    })
  },

  noInput (e) {
    // console.log(e)
    this.setData({
      noValue: e.detail
    })
  },

  // 重置
  reset () {
    page = 1
    this.setData({
      noValue: "",
      dateValue: "",
      data: [],
      loadAll: 1
    })
    this.getNcovData()
  },

  // 查询
  search () {

    const { noValue, dateValue } = this.data
    console.log(noValue, dateValue)

    if (noValue == "" || dateValue == "") {
      wx.showToast({
        title: '请输入查询条件',
        icon: 'none',
        duration: 2000
      })
    } else {
      page = 1
      this.setData({
        data: [],
        loadAll: 1
      })
      this.getNcovData()
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