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
create_dep = '''CREATE TABLE departments(
dep_id INT PRIMARY KEY,dep_name VARCHAR(20))'''

create_emp = '''CREATE TABLE employee(emp_id INT,emp_name varchar(20),
brit_date DATE,email VARCHAR(50),dep_id INT,FOREIGN KEY(emp_id) REFERENCES  departments(dep_id))'''

create_gz = '''CREATE TABLE gzb(id INT,gz_data DATE,emp_id INT ,basic INT,awards INT,PRIMARY KEY(id)
 ,FOREIGN KEY(emp_id) REFERENCES employee(emp_id))'''
cur.execute(create_dep)
cur.execute(create_emp)
cur.execute(create_gz)
cur.close()
conn.close()
