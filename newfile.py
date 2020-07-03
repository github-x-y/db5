from sqlalchemy import create_engine,Column,Integer,String,Date,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine(
    'mysql+pymysql://root:123qqq...A@192.168.1.11/tedu1908?charset=utf8',
    encoding = 'utf8',
    echo = True
)
Base = declarative_base()

class Departments(Base):
    __tablename__ = 'departments'
    dep_id = Column(Integer,primary_key=True)
    dep_name = Column(String(20),unique=True)
class Employees(Base):
    __tablename__ = 'employees'
    emp_id = Column(Integer,primary_key=True)
    emp_name = Column(String(20))
    birth_date = Column(Date)
    email = Column(String(50))
    dep_id = Column(Integer,ForeignKey('departments.dep_id'))
class gz(Base):
    __tablename__ = 'gzb'
    id = Column(Integer,primary_key=True)
    gz_data = Column(Date)
    emp_id = Column(Integer,ForeignKey('departments.dep_id'))
    basic = Column(Integer)
    awards = Column(Integer)
if __name__ == '__main__':
    Base.metadata.create_all(engine)