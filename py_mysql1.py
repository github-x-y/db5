import pymysql



conn = pymysql.connect(
    host = '192.168.1.11',
    port = 3306,
    user = 'root',
    password = '123qqq...A',
    db = "nsd1908",
    charset = 'utf8'
)
cur = conn.cursor()
insert1 = 'INSERT INTO departments VALUES(%s,%s)'
hr = [(1,'人事部')]
deps = [(2,'ops'),(3,'dev'),(4,'qa'),(5,'market'),(6,'sales')]
cur.executemany(insert1,hr)
cur.executemany(insert1,deps)
select1 = 'SELECT * FROM departments'
cur.execute(select1)
result1 = cur.fetchone()
print(result1)
result2 = cur.fetchmany(2)
print(result2)
result3 = cur.fetchall()
print(result3)
cur.execute(select1)
cur.scroll(2,mode='absolute')
result1 = cur.fetchone()
print(result1)
cur.scroll(1)
result2 = cur.fetchone()
print(result2)
update1 = 'UPDATE departments SET dep_name=%s WHERE dep_name=%s'
cur.execute(update1,('人力资源部','人事部'))
delete1 = 'DELETE FROM departments WHERE dep_id=%s'
cur.execute(delete1,(6))
conn.commit()
cur.close()
conn.close()