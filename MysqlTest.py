import pymysql
def MySql():
    try:
        conn=pymysql.connect(   #连接mysql库
            host='127.0.0.1',
            port=3306,
            username='root',
            password='123123',
            db='five')
    except Exception as e:
        return e.args
    else:
        #单条语句的插入
        sql='insert into user value (%s,%s,%s,%s)'
        params=[(3,'weike',18,'xian'),
                (4,'weike',19,'xian')]
        #批量插入
        sql = 'insert into user value (%s,%s,%s,%s)'
        params = (3, 'weike', 18, 'xian')
        cur=conn.cursor() #创建游标
        cur.execute(sql,params)  #单条插入执行
        cur.executemany(sql,params)#批量插入执行
        conn.commit()#备注，insert与update后一定要commit

    finally:
        cur.close()   #关闭数据库连接
        conn.close()
def deleteMysql():
    try:
        conn = pymysql.connect(  # 连接mysql库
            host='127.0.0.1',
            port=3306,
            username='root',
            password='123123',
            db='five')
    except Exception as e:
        return e.args
    else:
        sql = 'delete from user where id=%s'
        params = (3, )
        cur = conn.cursor()  # 创建游标
        cur.execute(sql, params)  # 单条删除执行
        conn.commit()  # 备注，insert与update，delete后一定要commit

    finally:
        cur.close()  # 关闭数据库连接
        conn.close()
class MySqlHelper:
    def conn(self):
        conn=pymysql.connect(
            host='127.0.0.1',
            port=3306,
            username='root',
            password='123123',
            db='five'
        )
        return conn
    def get_one(self,sql,params):
        cur=self.conn().cursor()
        data=cur.execute(sql,params)
        result=cur.fetchone()
        return result
def checkValid(username,password):
    opera=MySqlHelper()
    sql='select * from login where username=%scale and password=%s'
    params=(username,password)
    return opera.get_one(sql,params)
def info():
    username=input('用户名：')
    password=input('密码：')
    result=checkValid(username,password)
    if result:
        print('登录成功')
    else:
        print('登录失败')
