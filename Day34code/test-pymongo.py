# 安装pymongo
# pip install pymongo -i https://pypi.tuna.tsinghua.edu.cn/simple

# 引入pymongo
import pymongo

# 链接mongodb服务器
client = pymongo.MongoClient("127.0.0.1", 27017)

# 指定test数据库(如果没有会自动创建)
db = client.test

# 指定students集合(如果没有会自动创建)
students_collection = db.students

# 插入一条文档
# result = students_collection.insert_one({"name": "栗子", "age": 19, "sex": 1, "grade": 99})

# 查询文档 find(), find_one()

result = students_collection.find()

print(result)

# 更新文档 update(), update_one(), update_many()

students_collection.update_one({"name": "栗子"}, {"$set": {"grade": 59}})

# 删除文档 delete_one()、 delete_many()
students_collection.delete_many({"name": "栗子"})
