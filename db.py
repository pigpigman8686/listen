import pymysql.cursors

conn = pymysql.Connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = 'ZXCbnm.789',
    db = 'listen',
    cursorclass = pymysql.cursors.DictCursor
)

cur = conn.cursor()

def add_user(username,age,sex):
    try:
        sql = "insert into listen_user(username,age,sex) values('%s',%d,'%s');"%(username,age,sex)
        print(sql)
        cur.execute(sql)
        conn.commit()
        id = cur.lastrowid #获取最后插入的ID，并返回
        return id
    except:
        print("add_user item error!")
        return False

def add_question():
    try:
        sql = ""
        cur.execute(sql)
        conn.commit()
    except:
        print("add_question item error!")
        return False

def add_test(id,right,user_ans,count):
    try:
        #sql = "insert into listen_ans(id,right%s,user_ans%s) values('%s','%s','%s')"%(count,count,id,right,user_ans)
        sql = "INSERT INTO listen_ans(id,right%s,user_ans%s) VALUES('%s','%s','%s') ON DUPLICATE KEY UPDATE right%s='%s',user_ans%s='%s';"%(count,count,id,right,user_ans,count,right,count,user_ans)#以id为索引，若不存在则插入，存在则更新
        print(sql)
        cur.execute(sql)
        conn.commit()
        return True
    except:
        print("add_test item error!")
        return False

def getResult(id):
    try:
        sql = "SELECT * FROM listen_ans WHERE id='%s';"%id
        cur.execute(sql)
        result = cur.fetchall()
        return result
    except:
        print("getResult error!")
        return False