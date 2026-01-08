import pymysql
import random

number = random.randint(1,100)
print(number)

for i in range(number):
    print('老虎'+str(random.randint(1,100)), end='*'*5)
else:
    print('random over,total '+str(number)+' 条记录。')


"""
   启动mysql服务: net start mysql
   关闭mysql服务: net stop mysql
   mysql登陆:    mysql -u root -p  (输入管理员密码)
   查看数据库：   show databases;
   打开库表：     use xxx(database name); 
   查看库表：     show tables;
   查看库表结构：  desc xxx(table name);
   python data migrate to this new computer on 2022-9-8
   mysql is commit on 2023-9-28
   Happy National Day!
   update on 2024-11-11
"""

# 建立数据库连接实例
# 2025/10/27下午，更新数据库名称和数据库表名
db = pymysql.connect(user="root", password="123", host='localhost', database="bookdb")
# 获取数据库实例的游标
cur = db.cursor()

# SQL语句
query_sql = "select * from bookinfo"
count_sql = "select count(*) from bookinfo"
ins_sql = '''INSERT INTO bookinfo \
             (book_name, book_author, publish_date)\
             VALUES ("萍踪侠影", "梁羽生", "1983-8-3")
'''

"""
创建表语句
crt_sql ='''CREATE TABLE person_salary_tbl (
   id INT,
   FIRST_NAME CHAR(20) NOT NULL,
   LAST_NAME CHAR(20),
   INCOME FLOAT )'''

cur.execute(crt_sql)
"""

# 游标执行SQL语句, 插入记录
for i in range(20):
    cur.execute(ins_sql)

# 将插入的记录提交数据库, 记录正式生效
db.commit()

# 游标执行SQL语句查询，返回记录数量int
rs = cur.execute(query_sql)
print('总记录数：', rs, '条')

# 利用count(*)函数获取表中记录总数 --2022/9/8 11:05 am
# 下面语句无意义，应删除：
'''
ct = cur.execute(count_sql) 
print('总记录数：', ct)
'''
"""
It's not the latest version.
"""

# 利用查询结果（int），cur.fetchone 逐条输出数据库记录
for i in range(rs):
    print(cur.fetchone())
    print('*' * 50)

# 程序结束，关闭数据库实例的游标
cur.close()

# 程序结束，关闭数据库实例连接
db.close()

#pin 重新设定