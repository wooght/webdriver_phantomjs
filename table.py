# -*- coding: utf-8 -*-
__author__ = 'wooght'
from sqlalchemy import create_engine, Table, Column ,MetaData, select
from sqlalchemy import VARCHAR as Varchar,TEXT as Text, Integer, String, ForeignKey
# 连接数据库
#mysql+pymysql  表示数据库为mysql,通过pymysql为基础链接操作数据库
engine = create_engine("mysql+pymysql://root:wooght565758@localhost:3306/py_test?charset=utf8",encoding="utf-8", echo=True)
# 获取元数据
metadata = MetaData()

#上证E互动 sns_sseinfo
sns_sseinfo = Table('sns_sseinfo',metadata,
    Column('id',Integer,primary_key=True),
    Column('time',String(56)),              #时间
    # Column('ask',Varchar(256)),             #问题
    Column('ask',Text(256)),                #问题
    Column('anwser',Text()),                #回答
    Column('dm',String(16))                 #股票代码
)
#第一财经新闻
yicai = Table('yicai_news',metadata,
    Column('id',Integer,primary_key=True),
    Column('url',Integer,nullable=False),     #网页地址ID号
    Column('title',String(128),nullable=True),  #新闻标题
    Column('body',Text),                        #新闻内容
    Column('time',String(64))                   #发布时间
)
#雪球文章
xueqiuarticle = Table('xueqiuarticle',metadata,
    Column('id',Integer,primary_key=True),
    Column('url',String(64)),
    Column('title',String(128),nullable=True),  #新闻标题
    Column('body',Text),                        #新闻内容
    Column('time',String(64))                   #发布时间
)
# Column类型有：
#     TIMESTAMP
#     TIME
#     DATETIME
#     DATE
#     CHAR
#     BOOLEAN

#创建数据表 如果存在则pass
metadata.create_all(engine)
# #链接数据库
conn = engine.connect()

# i = sns_sseinfo.insert()
# list = dict(time='2017-10-10',ask='aa',anwser='11',dm='11')
# print(i)
# r = conn.execute(i,list)
