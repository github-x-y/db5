import pymysql



conn = pymysql.connect(
    host = '192.168.1.11',
    port = 3306,
    user = 'tom',
    password = '123456',
    db = "db1",
    charset = 'utf8'
)
cur = conn.cursor()
delete1 = 'DELETE FROM departments WHERE dep_id=%s'
cur.execute(delete1,(6))
conn.commit()
cur.close()
conn.close()