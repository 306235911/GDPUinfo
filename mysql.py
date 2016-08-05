import Mysqldb

class Mysql:
    
    def __init__(self):
        try:
            self.db = Mysqldb.connect('localhost', 'root' , '306235911','gdpu')
            self.cur = self.db.cursor()
        except MySQL.Error,e:
            print '数据库连接错误，原因%d : %s' % (e.args[0] , e.args[1])
            
    def insertData(self,num,title,webside):
        sql = "INSERT INTO infomation VALUES (%s)" % (num , title , webside)
        try:
            result = self.cur.execute(sql)
            insert_id = self.db.insert_id()
            self.db.commit()
            if result:
                # 返回正数即正常
                return insert_id
            else:
                # 返回0为异常
                return 0
        except MySQLdb.Error , e:
            self.db.rollback()
            if "key'PRIMARY'" in e.args[1]:
                print self.getCurrentTime(),"数据已存在，未插入数据"
            else:
                print self.getCurrentTime(),"插入数据失败，原因 %d: %s" % (e.args[0], e.args[1])