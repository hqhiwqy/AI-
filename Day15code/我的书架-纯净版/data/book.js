// 编写书目模块（CRUD）

const db = wx.cloud.database();  //获取数据库引用

const book = db.collection('book'); //获取book集合引用

//查询

//更具用户openid查询所有的书目信息

let getBookByUid = function(uid,cb){
  book.where({
    _openid: uid
  }).get().then(res=>{
    cb(res)
  })
}

//新增

let addBook =function(obj,cb){
  book.add({
    data:{
      bookName:obj.data.creatingBookName
    }
  }).then(res=>{
    cb(res)
  })
}

//删除

//根据记录ID来删除书目

let deleteBookById = function(id,cb){
  book.doc(id).remove().then(res=>{
    cb(res);
  })
}

//更新
let updateBook = function(id,obj,cb){
    book.doc(id).update({
      data:{
        bookName:obj.data.editingBookName
      }
    }).then(res=>{
      cb(res);
    })
}


module.exports = {
  getBookByUid,
  addBook,
  deleteBookById,
  updateBook

}