#encoding=utf-8
import MySQLdb
import time

#db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

f = open("zomato_site_map2","r")
lines = f.readlines()

cursor = db.cursor()

for line in lines:
       print line
       strs = line.split("\t")
       country = strs[0]
       city = strs[1]
       url = strs[2]
       print country, city, url
 
       time_str = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

       sql = """INSERT INTO crawl_info(src,
             crawl_index1, crawl_index2, crawl_index3, create_time, update_time)
             VALUES ('zomato', '"""+country+"""', '"""+city+"""', '"""+url+"""', '"""+time_str+"""','"""+time_str+"""')"""

       try:
              # 执行sql语句
              cursor.execute(sql)
              # 提交到数据库执行
              db.commit()
       except:
              # Rollback in case there is any error
              db.rollback()


db.close()
