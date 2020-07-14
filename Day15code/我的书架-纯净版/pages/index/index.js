//index.js

import book from '../../data/book'

Page({
  data: {
    title: '我的书架',
    bookList: [],
    creatingBookName: '', // 当前正在创建的书名
    editingBookName: '', // 当前正在编辑的书名
  },

  onLoad(options) {
   
    this.fetchBookList();

  },

  // 获取 bookList 数据
  fetchBookList() {
    
    wx.cloud.callFunction({
      name:'login'
    }).then(res=>{
      let openid = res.result.openid;
      book.getBookByUid(openid,res=>{
        console.log(res);
        this.setData({
          bookList:res.data
        })
      })
      // const db = wx.cloud.database();

      // db.collection('book').where({
      //   _openid:openid
      // }).get().then(res =>{
      //   console.log(res);
      //   this.setData({
      //     bookList:res.data
      //   });
      // })
    })
    
    //let bookList = [
      // {
      //   "_id": "5984465311a55f59b38ea909",
      //   "bookName": "傲慢与偏见"
      // },
      // {
      //   "_id": "5984465311a55f59b38ea90b",
      //   "bookName": "双城记",
      // }, 
      // {
      //   "_id": "5984465311a55f59b38ea90f",
      //   "bookName": "黑客与画家",
      // }
  //  ];

    // this.setData({
    //   bookList
    // });


  },


  //添加事件
  createBook:function(){
    let creatingBookName = this.data.creatingBookName;
    if(creatingBookName == ''){
        wx.showToast({
          title: '请输入书目名称',
          icon: 'none'
        })
    }else{
      book.addBook(this,res=>{
          wx.showToast({
            title: '添加书目成功！',
            icon:'success'
          })
          this.fetchBookList();
      });

        // const db = wx.cloud.database();
        // db.collection('book').add({
        //   data:{
        //     bookName:creatingBookName
        //   }
        // }).then(res =>{
        //     console.log(res);
        //     wx.showToast({
        //       title: '添加书目成功！',
        //       icon: 'success'
        //     })
        //     this.fetchBookList();
        // })
    }
  },

  //删除事件
  deleteBook: function(e){
    let bookId = e.currentTarget.dataset.bookId

    book.deleteBookById(bookId,res=>{
      wx.showToast({
      title: '删除书目成功',
      icon:'success'
      })
      this.fetchBookList();
    })

    // const db = wx.cloud.database();

    // db.collection('book').doc(bookId).remove().then(res=>{
    //   console.log(res);
    //   wx.showToast({
    //     title: '删除书目成功',
    //     icon:'success'
    //   })
    //     this.fetchBookList();
    // })
  },

  //保存事件
  updateBook:function(e){
    let bookId = e.currentTarget.dataset.bookId;
    let editingBookName = this.data.editingBookName;

    book.updateBook(bookId,this,res=>{
      console.log(res);
      wx.showToast({
        title: '更新书目成功！',
        icon: 'success'
      })
      this.fetchBookList();
    })
    // const db = wx.cloud.database();

    // db.collection('book').doc(bookId).update({
    //   data:{
    //     bookName: editingBookName
    //   }
    // }).then(res=>{
    //   console.log(res);
    //   wx.showToast({
    //     title: '更新书目成功！',
    //     inco: 'success'
    //   })
    //   this.fetchBookList();
    // })
  },

  // 绑定添加书目的输入框事件，设置添加的数目名称
  bindCreateBookNameInput(e) {
    let value = e.detail.value
    console.log(value);
    this.setData({
      creatingBookName: value
    })
  },

  // 绑定每一行书目的“编辑”按钮点击事件，控制输入框和文本显示
  editBookButtonClicked(e) {
    let that = this
    let activeIndex = e.currentTarget.dataset.index
    let bookList = this.data.bookList

    bookList.forEach((elem, idx) => {
      if (activeIndex == idx) {
       elem.isEditing = true
      } else {
        elem.isEditing = false
      }
    })

    that.setData({
      bookList
    })
  },

  // 绑定每一行书目的输入框事件，设定当前正在编辑的书名
  bindEditBookNameInput(e) {
    let bookName = e.detail.value
    this.setData({
      editingBookName: bookName,
    })
  }

})